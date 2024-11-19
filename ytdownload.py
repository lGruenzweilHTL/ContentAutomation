from pytubefix import YouTube
from pytubefix.cli import on_progress
import logging


def download_yt(url, output_path):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        subtitles = yt.captions
        print(f"English subtitles:\n{subtitles['a.en']}")
        stream = yt.streams.get_highest_resolution()
        location = stream.download(output_path)
        print(f"Downloaded video to {output_path}")

        return location
    except Exception as e:
        logging.error(f"Failed to download video: {e}")
        raise
