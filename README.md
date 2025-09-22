# sqlite-vec-sqlmodel

## Demonstration searching bluesky posts

This is a project to use sqlmodel with sqlite-vec and EmbeddingGemma

https://alexgarcia.xyz/sqlite-vec/features/knn.html

```
$ uv run main.py 
[21:02:32] Check sqlite version                                                                                                                                     main.py:144
           sqlite version: 3.47.2                                                                                                                                   main.py:146
           Check sqlite-vec version                                                                                                                                 main.py:148
           sqlite-vec version: v0.1.6                                                                                                                               main.py:150
           Create virtual table                                                                                                                                     main.py:152
           Create all tables                                                                                                                                        main.py:155
           Load model google/embeddinggemma-300m                                                                                                                    main.py:158
Bluesky handle? (wired.com): 
[21:02:35] Fetching posts                                                                                                                                           main.py:164
2025-09-17T15:09:39.939Z
[21:02:36] Indexing posts                                                                                                                                           main.py:168
query (exit): AI
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Distance ┃ Text                                                                                                                                                             ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 0.38922  │ A wave of AI users presenting in states of psychological distress gave birth to an unofficial diagnostic label. Experts say it’s neither accurate nor needed,    │
│          │ but concede that it’s likely to stay. www.wired.com/story/ai-psy...                                                                                              │
│ 0.46055  │ A punt-plus plus                                                                                                                                                 │
│ 0.47036  │ Google weaving Gemini further into the popular Chrome browser is an inflection point for AI in our software, although some users will still be looking for the   │
│          │ “off” switch.                                                                                                                                                    │
│ 0.49610  │ Today on "Uncanny Valley," we talk about why the AI industry is investing in the development of humanoid robots, and what that means for us non-robots.          │
│          │ www.wired.com/story/uncann...                                                                                                                                    │
│ 0.50672  │ On its 20th anniversary, YouTube is venturing into an era of AI-generated video, and may never be the same.                                                      │
└──────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
