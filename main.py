import sqlite3
import sqlite_vec

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

from sqlmodel import Field, SQLModel, Session, create_engine, select
from sqlalchemy import text, func
from sqlalchemy.exc import SQLAlchemyError
from sentence_transformers import SentenceTransformer

from atproto import Client

from typing import List

from datetime import datetime


class Settings(BaseSettings):
    bluesky_username: str
    bluesky_password: SecretStr
    sqlite_url: str = "sqlite:///"
    sqlite_database: str = ":memory:"
    model: str = "google/embeddinggemma-300m"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
conn = sqlite3.connect(settings.sqlite_database)


def sqlite_with_vec_creator() -> sqlite3.Connection:
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    conn.enable_load_extension(False)
    return conn


engine = create_engine(settings.sqlite_url, creator=sqlite_with_vec_creator)


def check_sqlite_version() -> str | None:
    sqlite_version = None

    with Session(engine) as session:
        try:
            result = session.exec(text("SELECT SQLITE_VERSION()"))
        except SQLAlchemyError as e:
            print(f"Error: {e}")
        else:
            sqlite_version = result.one()[0]

    return sqlite_version


def check_sqlite_vec_version() -> str | None:
    sql_vec_version = None

    with Session(engine) as session:
        try:
            result = session.exec(text("SELECT VEC_VERSION()"))
        except SQLAlchemyError as e:
            print(f"Error: {e}")
        else:
            sql_vec_version = result.one()[0]

    return sql_vec_version


class Item(SQLModel, table=True):
    __tablename__ = "items"
    id: str = Field(primary_key=True)
    link: str
    handle: str
    content: str
    created_at: datetime
    embedding: bytes | None = None


def load_database(posts: List[tuple[str, str, str, str, datetime]], model: SentenceTransformer):
    item_list = []

    for post_id, link, handle, content, created_at in posts:
        item_list.append(
            Item(id=post_id, link=link, handle=handle, content=content, created_at=created_at, embedding=model.encode_query(content))
        )

    with Session(engine) as session:
        session.add_all(item_list)
        session.commit()


def nearest_neighbor_query(query_str: str, model: SentenceTransformer):
    with Session(engine) as session:
        query_embedding = model.encode_query(query_str)

        subquery = (
            select(
                Item.handle,
                Item.created_at,
                Item.link,
                Item.content,
                func.vec_distance_cosine(Item.embedding, query_embedding).label(
                    "distance"
                ),
            )
        ).subquery()

        statement = (
            select(subquery.c.handle, subquery.c.link, subquery.c.content, subquery.c.distance, subquery.c.created_at)
#            .where(subquery.c.distance < 0.5)
            .order_by(subquery.c.distance, subquery.c.created_at.desc())
            .limit(5)
        )
        result = session.exec(statement).all()

        return [(row[0], row[1], row[2], row[3], row[4]) for row in result]

def fetch_bsky_posts(bsky_handle: str):
    client = Client()
    client.login(
        settings.bluesky_username, settings.bluesky_password.get_secret_value()
    )

    all_posts = []
    cursor = None
    limit = 100

    while len(all_posts) < 100:
        params = {"actor": bsky_handle, "limit": limit}
        if cursor:
            params["cursor"] = cursor
        
        if len(all_posts) + limit > 100:
            params["limit"] = 100 - len(all_posts)

        result = client.app.bsky.feed.get_author_feed(params=params)

        posts = [
            (
                f"{post.post.author.did}:{post.post.uri.split('/')[-1]}",  # Unique ID
                f"https://bsky.app/profile/{post.post.author.handle}/post/{post.post.uri.split('/')[-1]}",
                post.post.author.handle,
                post.post.record.text,
                datetime.fromisoformat(post.post.record.created_at.replace("Z", "+00:00")),
            )
            for post in result.feed
            if post.post.record.text and post.reply is None and post.reason is None
        ]
        all_posts.extend(posts)
        cursor = result.cursor
        if not cursor:
            break

    return all_posts


def main():
    from rich.prompt import Prompt
    from rich.console import Console
    from rich.table import Table

    console = Console()

    with console.status("Loading") as status:
        console.log("Check sqlite version")
        sqlite_version = check_sqlite_version()
        console.log(f"sqlite version: {sqlite_version}")

        console.log("Check sqlite-vec version")
        sql_vec_version = check_sqlite_vec_version()
        console.log(f"sqlite-vec version: {sql_vec_version}")

        console.log("Create all tables")
        SQLModel.metadata.create_all(engine)

        console.log(f"Load model {settings.model}")
        model = SentenceTransformer(settings.model)

    bsky_handle = Prompt.ask("Bluesky handle?", default="wired.com")

    with console.status("Fetching posts"):
        console.log("Fetching posts")
        posts = fetch_bsky_posts(bsky_handle)

    with console.status(f"Indexing {len(posts)} posts"):
        console.log(f"Indexing {len(posts)} posts")
        load_database(posts, model)

    query = Prompt.ask("query", default="exit")

    while query != "exit":
        results = nearest_neighbor_query(query, model)

        if not results:
            console.print("No results found")
        else:
            table = Table(show_header=True)
            table.add_column("Distance")
            table.add_column("Content")

            for handle, link, content, distance, created_at in results:
                table.add_row(f"{distance:0.5f}", f"{handle}, {created_at.strftime('%Y-%m-%d %H:%M:%S')}, {link}\n{content}")

            console.print(table)

        query = Prompt.ask("query", default="exit")


if __name__ == "__main__":
    main()
