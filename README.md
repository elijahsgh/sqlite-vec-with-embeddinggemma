# sqlite-vec-sqlmodel

## Demonstration searching bluesky posts

This is a project to use sqlmodel with sqlite-vec and EmbeddingGemma

https://alexgarcia.xyz/sqlite-vec/features/knn.html

```
[10:28:04] Check sqlite version                                                                                                                                     main.py:167
           sqlite version: 3.47.2                                                                                                                                   main.py:169
           Check sqlite-vec version                                                                                                                                 main.py:171
           sqlite-vec version: v0.1.6                                                                                                                               main.py:173
           Create all tables                                                                                                                                        main.py:175
           Load model google/embeddinggemma-300m                                                                                                                    main.py:178
Bluesky handle? (wired.com): 
[10:28:08] Fetching posts                                                                                                                                           main.py:184
[10:28:09] Indexing 100 posts                                                                                                                                       main.py:188
query (exit): artificial intelligence
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Distance ┃ Content                                                                                                                                                          ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 0.44747  │ wired.com, 2025-09-18 10:32:14, https://bsky.app/profile/wired.com/post/3lz45iytvum2h                                                                            │
│          │ A wave of AI users presenting in states of psychological distress gave birth to an unofficial diagnostic label. Experts say it’s neither accurate nor needed,    │
│          │ but concede that it’s likely to stay. www.wired.com/story/ai-psy...                                                                                              │
│ 0.48820  │ wired.com, 2025-09-15 21:55:26, https://bsky.app/profile/wired.com/post/3lyvsbvv5li2h                                                                            │
│          │ At WIRED's AI Power Summit Monday, industry executives and officials discussed the impact artificial intelligence is having on every corner of society—and where │
│          │ it goes from here. www.wired.com/story/wired-...                                                                                                                 │
│ 0.49453  │ wired.com, 2025-09-22 13:06:47, https://bsky.app/profile/wired.com/post/3lzghz2awxn2e                                                                            │
│          │ Every fitness company has jumped on the AI-powered fitness subscription bandwagon. Should you?                                                                   │
│ 0.50068  │ wired.com, 2025-09-18 19:47:51, https://bsky.app/profile/wired.com/post/3lz54kkccb72h                                                                            │
│          │ Today on "Uncanny Valley," we talk about why the AI industry is investing in the development of humanoid robots, and what that means for us non-robots.          │
│          │ www.wired.com/story/uncann...                                                                                                                                    │
│ 0.51075  │ wired.com, 2025-09-18 17:05:32, https://bsky.app/profile/wired.com/post/3lz4tibqapg2h                                                                            │
│          │ Google weaving Gemini further into the popular Chrome browser is an inflection point for AI in our software, although some users will still be looking for the   │
│          │ “off” switch.                                                                                                                                                    │
└──────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
query (exit): 
```
