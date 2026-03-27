# Ochaco Uraraka: Rising — Opera GX Mod (schema 1)

**My Hero Academia** mod for Ochaco Uraraka: **pink** (quirk / personality) and **brown** (hair) GX colors, plus **broad web modding** modeled on the Ann Takamaki bucket layout (global layer + `sites-01` … `sites-06`).

## Web modding layout (Ann-style)

| File | Role |
|------|------|
| `webmodding/ochaco-uraraka.css` | Global: links, scrollbars, soft pink/brown mist (`https://*/*`) |
| `webmodding/sites-01-google-youtube.css` | Google suite + YouTube |
| `webmodding/sites-02-social.css` | Reddit, X, Facebook, Instagram, TikTok, Discord, Pinterest, Tumblr, LinkedIn, Threads |
| `webmodding/sites-03-dev.css` | GitHub, GitLab, Stack Overflow / Exchange, Hacker News |
| `webmodding/sites-04-shopping.css` | Amazon regions, eBay, PayPal, Apple |
| `webmodding/sites-05-media.css` | Netflix, Spotify, Twitch, BBC, CNN, IMDb, Medium |
| `webmodding/sites-06-productivity.css` | Wikipedia, Notion, Dropbox, Microsoft / Outlook / Yahoo, Steam, Craigslist, Indeed |

After editing CSS, reload the mod in **opera://extensions**. Turn **web modding** on for this mod in **Mods** if links/scrollbars do not pick up the theme.

Optional custom cursor asset: run `python scripts/generate_cursor.py` then add `webmodding/cursor-optional.css` to `page_styles` if you want the data-URL cursor (not enabled by default).

## Wallpaper & music

Bundled:

- **Video:** `wallpaper/Ochaco vs Himiko.mp4` (manifest path).
- **First frame:** `wallpaper/first_frame_ochaco.jpeg` — run `python scripts/extract_wallpaper_first_frame.py --frame N` after swapping the MP4.
- **Music:** `music/OCHAKO-URARAKA-VS-HIMIKO-TOGA.mp3`.

If your MP4 file is **empty or unfinished** (0 bytes / “moov atom not found”), re-export the clip or replace the file; until then a static loop may be generated from `ochacojpg.jpg` so the mod still loads.

## Icon

**`ochacojpg.jpg`** in the mod root → run `python scripts/generate_icon.py` for `icon_512.png`.

## Scripts

```bash
pip install Pillow opencv-python
python scripts/generate_wallpaper.py
python scripts/extract_wallpaper_first_frame.py
python scripts/generate_icon.py
python scripts/generate_cursor.py
```

## License

Fan-made tribute. My Hero Academia © Kohei Horikoshi / Shueisha.
