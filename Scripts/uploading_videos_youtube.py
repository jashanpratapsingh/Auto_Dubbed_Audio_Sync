import os
import json
import google.auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video_to_youtube(video_path, title, description, tags, category_id, privacy_status, channel_id):
    api_service_name = "youtube"
    api_version = "v3"

    # Load credentials from the environment
    credentials, _ = google.auth.default()

    youtube = build(api_service_name, api_version, credentials=credentials)

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": privacy_status
        },
        "contentDetails": {
            "videoType": "short"
        }
    }

    media = MediaFileUpload(video_path)

    response = youtube.videos().insert(
        part="snippet,status,contentDetails",
        body=request_body,
        media_body=media
    ).execute()

    return response

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(script_directory, "final_videos", "video_English.mp4")
    title = "My Uploaded Video"
    description = "This is a test video"
    tags = ["test", "upload", "video"]
    category_id = "22"  # Example category ID for Entertainment
    privacy_status = "public"
    channel_id = "UCABCXYZ123"  # Replace with the YouTube channel ID

    response = upload_video_to_youtube(video_path, title, description, tags, category_id, privacy_status, channel_id)
    video_id = response.get('id')
    if video_id:
        print(f"Video uploaded successfully. Video ID: {video_id}")
    else:
        print("Video upload failed.")

if __name__ == '__main__':
    main()