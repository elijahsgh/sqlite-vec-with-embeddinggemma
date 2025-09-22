# sqlite-vec-sqlmodel

## Demonstration searching bluesky posts

This is a project to use sqlmodel with sqlite-vec and EmbeddingGemma

https://alexgarcia.xyz/sqlite-vec/features/knn.html

```
[10:24:21] Check sqlite version                                                                                                                                     main.py:167
           sqlite version: 3.47.2                                                                                                                                   main.py:169
           Check sqlite-vec version                                                                                                                                 main.py:171
           sqlite-vec version: v0.1.6                                                                                                                               main.py:173
           Create all tables                                                                                                                                        main.py:175
           Load model google/embeddinggemma-300m                                                                                                                    main.py:178
Bluesky handle? (wired.com): 
[10:24:25] Fetching posts                                                                                                                                           main.py:184
[10:24:27] Indexing 100 posts                                                                                                                                       main.py:188
query (exit): LLMs
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Distance ┃ Content                                                                                                                                                          ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 0.50547  │ wired.com, 2025-09-21 23:27:00, https://bsky.app/profile/wired.com/post/3lzf276eehq2a                                                                            │
│          │ The last night of tech mogul Mike Lynch’s life has become fodder for conspiracy theories. For the first time, the whole story can be told.                       │
│ 0.52534  │ wired.com, 2025-09-15 20:52:30, https://bsky.app/profile/wired.com/post/3lyvorf54mr2h                                                                            │
│          │ Handmade in the Netherlands, the Moccamaster will kickstart your morning for years to come. www.wired.com/story/save-u...                                        │
│ 0.53191  │ wired.com, 2025-09-16 19:04:04, https://bsky.app/profile/wired.com/post/3lyxz6fgmpk24                                                                            │
│          │ “Only Murders in the Building,” “Tempest,” and “Alien: Earth” are just a few of the shows you should be watching on Hulu this month.                             │
│ 0.54422  │ wired.com, 2025-09-18 20:49:52, https://bsky.app/profile/wired.com/post/3lz57zhe4me2e                                                                            │
│          │ This is one of the biggest, baddest screens you can game on, and it's marked down to less than the smaller version. www.wired.com/story/save-d...                │
│ 0.55334  │ wired.com, 2025-09-17 10:33:18, https://bsky.app/profile/wired.com/post/3lyzn3y53lp2y                                                                            │
│          │ Located in China, Juno is a 17-country collaboration that will try to detect neutrinos and antineutrinos to learn more about their mass.                         │
│          │ www.wired.com/story/this-g...                                                                                                                                    │
└──────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
