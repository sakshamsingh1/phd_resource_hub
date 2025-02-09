# File to download AudioSet dataset from Google

First, get the dataset split CSV of the videos you want to download from [Google](https://research.google.com/audioset/download.html).

Install yt-dlp using the command 
```python
python -m pip install yt-dlp
```

In `download_audioset.py`, place the path to your CSV in the variable `CSV_FILE` and where you want the videos to be stored in `OUT_DIR`.

Some videos will be age restricted, which requires a cookies.txt file, which you can get following the [yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp) GitHub.