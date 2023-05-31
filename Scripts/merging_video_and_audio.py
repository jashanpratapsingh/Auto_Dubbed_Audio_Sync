import os
from moviepy.editor import VideoFileClip, AudioFileClip

def combine_video_with_audio_and_srt():
    # Get the paths for audio directory and video file
    script_directory = os.path.dirname(os.path.abspath(__file__))
    audio_directory = os.path.join(script_directory, "../Outputs/video")
    video_file = os.path.join(script_directory, "../Outputs/video/video.mp4")

    # Create the output directory if it doesn't exist
    output_directory = os.path.join(script_directory, "../final_videos")
    os.makedirs(output_directory, exist_ok=True)

    # Iterate over the audio files in the directory
    for audio_filename in os.listdir(audio_directory):
        if audio_filename.endswith('.aac'):  # Check if the file is an audio file
            audio_path = os.path.join(audio_directory, audio_filename)

            # Extract language name and code from audio filename
            language_name = audio_filename.split(' - ')[1]
            language_code = audio_filename.split(' - ')[2].split('.aac')[0]

            # Set the output video file path
            output_filename = f"video_{language_name}.mp4"
            output_path = os.path.join(output_directory, output_filename)

            # Load the video and audio clips
            video_clip = VideoFileClip(video_file)
            audio_clip = AudioFileClip(audio_path)

            # Set the audio of the video clip to the loaded audio clip
            video_clip = video_clip.set_audio(audio_clip)

            # Find the corresponding SRT file
            srt_filename = f"video - {language_name} - {language_code}.srt"
            srt_path = os.path.join(audio_directory, srt_filename)

            # Check if the SRT file exists
            if os.path.exists(srt_path):
                # Load the SRT file and set it as the subtitle of the video clip
                video_clip = video_clip.set_subtitles(srt_path)

            # Write the combined video with audio and subtitles to the output file
            video_clip.write_videofile(output_path, codec='libx264')

            # Close the clips
            video_clip.close()
            audio_clip.close()

    print("Videos with audio and subtitles combined successfully!")