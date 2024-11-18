import pytube


def download_yt(url, output_path):
    yt = pytube.YouTube(url)

    # Get the highest resolution stream available
    stream = yt.streams.get_highest_resolution()

    # Download the video
    stream.download(output_path)
