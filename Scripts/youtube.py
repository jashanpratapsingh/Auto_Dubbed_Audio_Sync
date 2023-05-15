import os
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
from urllib.parse import parse_qs, urlparse

def download_youtube_and_generate_srt():
    def parse_video_id(url):
        # Parse the video ID from the URL
        query = urlparse(url)
        if 'youtu.be' in query.netloc:
            video_id = query.path[1:]
        elif '/shorts/' in query.path:
            video_id = query.path.split('/')[2]
        else:
            video_id = parse_qs(query.query)['v'][0]
        return video_id

    youtube_url = input("Enter the URL for the YouTube video: ")
    video_output_file = "video.mp4"
    srt_output_file = "subtitles.srt"

    query = urlparse(youtube_url)
    video_id = parse_video_id(youtube_url)

    # Create the root directory if it doesn't exist
    root_directory = os.path.dirname(os.path.abspath(__file__))
    outputs_directory = os.path.join(root_directory, "../Outputs")
    os.makedirs(outputs_directory, exist_ok=True)

    # Set the full path for the video output file
    video_output_path = os.path.join(outputs_directory, "video", video_output_file)

    # Download the YouTube video
    yt = YouTube(youtube_url)
    video = yt.streams.get_highest_resolution()
    video.download(output_path=os.path.join(outputs_directory, "video"), filename=video_output_file)

    # Get the transcript for the YouTube video
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Generate the SRT content
    srt_content = ""
    for i, segment in enumerate(transcript):
        start = segment['start']
        end = segment['start'] + segment['duration']
        text = segment['text']

        # Format the time in SRT format (HH:MM:SS,sss)
        start_time = '{:02d}:{:02d}:{:02d},{:03d}'.format(int(start // 3600),
                                                           int((start % 3600) // 60),
                                                           int(start % 60),
                                                           int((start * 1000) % 1000))
        end_time = '{:02d}:{:02d}:{:02d},{:03d}'.format(int(end // 3600),
                                                         int((end % 3600) // 60),
                                                         int(end % 60),
                                                         int((end * 1000) % 1000))

        # Add the SRT entry to the content
        srt_content += f"{i+1}\n{start_time} --> {end_time}\n{text}\n\n"

    # Set the full path for the SRT output file
    srt_output_path = os.path.join(outputs_directory, srt_output_file)

    # Save the SRT content to a file
    with open(srt_output_path, 'w', encoding='utf-8') as f:
        f.write(srt_content)