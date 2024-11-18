import os
import shutil
import ytdownload
import tts


def generate(config):
    print("Starting generation with config: ", config)
    script = config.script
    use_url = config.use_url
    url = config.url
    video_path = config.video_path
    voice = config.voice
    speech_speed = config.speech_speed
    speech_volume = config.speech_volume

    # Create the output folder
    path = create_folder(config.title)
    video_path_cp = os.path.join(path, "video.mp4")
    voiceover_path = os.path.join(path, "voiceover.mp3")
    output_path = os.path.join(path, "final.mp4")

    if use_url:
        # Download the YouTube video
        ytdownload.download_yt(url, video_path_cp)
    else:
        # Copy the video file to the output folder
        shutil.copy(video_path, video_path_cp)

    # Generate the voiceover
    voice_id = tts.get_voice_id(voice)
    tts.text_to_speech(script, voiceover_path, speech_speed, speech_volume, voice_id)

    # Add the voiceover to the video
    print("Adding voiceover to video")
    tts.add_audio_to_video(video_path_cp, voiceover_path, output_path)
    print("Audio addition complete")

    # Open the output file in explorer
    os.system(f"start {output_path}")

    print("Generation complete")

    # Exit the program
    exit(0)


def create_folder(title):
    path = os.path.join("gen", title)
    os.makedirs(path, exist_ok=False)
    return path
