import pytube


def download_yt(url, output_path):
    try:
        # Create a YouTube object
        yt = pytube.YouTube(url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Download the video
        file_path = stream.download(output_path)

        return True
    except Exception as e:
        return e
