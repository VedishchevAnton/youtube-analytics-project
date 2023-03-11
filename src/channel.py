import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.environ.get('API_KEY')

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        printout = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(printout, indent=2, ensure_ascii=False))
