import pyttsx3
from moviepy.editor import VideoFileClip, AudioFileClip


def get_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    return voices


def get_voice_id(voice_name):
    voices = get_voices()
    for voice in voices:
        if voice.name == voice_name:
            return voice.id
    return None


def text_to_speech(text, output_file, rate=150, volume=1, voice_id=None):
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty('rate', rate)  # Speed of speech
        engine.setProperty('volume', volume)  # Volume (0.0 to 1.0)
        if voice_id:  # Voice ID
            engine.setProperty('voice', voice_id)

        # Save the speech to a file
        print(f"Saving speech to file: {output_file}")
        engine.save_to_file(text, output_file)

        # Run the TTS engine
        print("Running TTS engine")
        engine.runAndWait()

        # Close the engine
        engine.stop()
    except Exception as e:
        print(f"Error in text_to_speech: {e}")
        return False


def add_audio_to_video(video_file, audio_file, output_file, crop_video=True):
    # Load the video file
    video = VideoFileClip(video_file)

    # Load the audio file
    audio = AudioFileClip(audio_file)

    # Set the audio of the video file
    video = video.set_audio(audio)

    # Crop the video to the length of the audio if cropVideo is True
    if crop_video:
        video = video.subclip(0, audio.duration)

    # Write the result to a new file
    video.write_videofile(output_file, codec='libx264', audio_codec='aac')

    audio.close()
    video.close()
