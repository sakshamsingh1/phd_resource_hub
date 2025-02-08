import csv
import os
import subprocess

CSV_FILE = "eval_segments.csv"
OUT_DIR = "downloads_eval"  
NUM_WORKERS = 4
YT_DLP = "yt-dlp"

def download_clip(youtube_id, start, end, out_dir):
    out_path = os.path.join(out_dir, f"{youtube_id}.mp4")

    if os.path.exists(out_path):
        print(f"Skipping {youtube_id} (already downloaded).")
        return

    command = [
        YT_DLP,
        f"https://www.youtube.com/watch?v={youtube_id}",
        "--download-sections", f"*{start}-{end}",
        "-f", "mp4",
        "-o", out_path,
        #--cookies", "cookies.txt" comment this out if you had a cookies file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Downloaded: {youtube_id}")
    except subprocess.CalledProcessError as e:
        print(f"Failed: {youtube_id} - {e}")

def main(dataset_name):
    os.makedirs(OUT_DIR, exist_ok=True)

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for line in reader:
            if len(line) < 3 or line[0].startswith("#"):
                continue

            youtube_id = line[0]
            try:
                start_time = float(line[1])
                end_time = float(line[2])
            except ValueError:
                continue

            download_clip(youtube_id, start_time, end_time, OUT_DIR)

if __name__ == "__main__":
    main()

