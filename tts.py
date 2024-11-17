import pyttsx3
from moviepy.editor import VideoFileClip, AudioFileClip


def list_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"ID: {voice.id}\nName: {voice.name}\nLanguages: {voice.languages}\nGender: {voice.gender}\nAge: {voice.age}\n")


def text_to_speech(text, output_file, voice_id=None):
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

        # Set the voice if provided
        if voice_id:
            engine.setProperty('voice', voice_id)

        # Save the speech to a file
        engine.save_to_file(text, output_file)

        # Run the TTS engine
        engine.runAndWait()

        return True
    except Exception as e:
        return e


def add_audio_to_video(video_file, audio_file, output_file):
    # Load the video file
    video = VideoFileClip(video_file)

    # Load the audio file
    audio = AudioFileClip(audio_file)

    # Set the audio of the video file
    video = video.set_audio(audio)

    # Write the result to a new file
    video.write_videofile(output_file, codec='libx264', audio_codec='aac')
