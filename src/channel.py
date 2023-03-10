import json
import os
from googleapiclient.discovery import build
import isodate


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
        self.channel_id = channel_id
        self.api_key = os.environ.get('API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.playlist = self.youtube.playlists().list(channelId=channel_id,
                                                      part='contentDetails,snippet',
                                                      maxResults=50,
                                                      ).execute()
        self.printout = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        print(json.dumps(self.printout, indent=2, ensure_ascii=False))
