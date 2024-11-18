import os

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
    output_path = config.output_path

    if use_url:
        # Download the YouTube video
        ytdownload.download_yt(url, video_path)

    # Generate the voiceover
    voice_id = tts.get_voice_id(voice)
    tts.text_to_speech(script, "voiceover.mp3", speech_speed, speech_volume, voice_id)

    # Add the voiceover to the video
    print("Adding voiceover to video")
    tts.add_audio_to_video(video_path, "voiceover.mp3", output_path)
    print("Audio addition complete")

    print("Generation complete!")

    # Open the output file in explorer
    os.system(f"start {output_path}")
