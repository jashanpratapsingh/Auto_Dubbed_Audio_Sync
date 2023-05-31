import os
from pydub import AudioSegment

import os
from pydub import AudioSegment

def combine_audio_with_background_music():
    # Set the paths for background music, input directory, and output directory
    background_music_path = os.path.join(os.path.dirname(__file__), "background.mp3")
    audios_directory = os.path.join(os.path.dirname(__file__), "../Outputs/video")
    output_directory = os.path.join(os.path.dirname(__file__), "../Outputs/video/merged_audios")

    # Load the background music
    background_music = AudioSegment.from_file(background_music_path)

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Process each AAC audio file
    for file_name in os.listdir(audios_directory):
        if file_name.endswith(".aac"):
            audio_path = os.path.join(audios_directory, file_name)

            # Load the AAC audio
            audio = AudioSegment.from_file(audio_path, format="aac")

            # Adjust the length of the audio to match the background music
            audio = audio[:len(background_music)]

            # Combine the audio with the background music
            combined_audio = audio.overlay(background_music)

            # Set the output file path
            output_path = os.path.join(output_directory, file_name)

            # Save the merged audio as MP3
            combined_audio.export(output_path, format="mp3")

            print(f"Merged audio saved: {output_path}")

