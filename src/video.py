import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
from googleapiclient.errors import HttpError

from src.setting import ENV_FILE

load_dotenv(ENV_FILE)


class Video:
    """
    Класс для видео YouTube канала
    """
    api_key = os.environ.get('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        try:
            self.video_id = video_id
            self.video_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                              id=video_id
                                                              ).execute()
            self.title = self.video_response['items'][0]['snippet']['title']
            self.link = f"https://www.youtube.com/watch?v={self.video_id}"
            self.view_count = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count = self.video_response['items'][0]['statistics']['likeCount']
        except HttpError:
            print("non-existent id")
        except IndexError:
            self.video_response = None
            self.title = None
            self.link = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return f"{self.title}"


class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id: str) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id
