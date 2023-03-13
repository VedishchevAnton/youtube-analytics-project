import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.environ.get('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str):
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """
        Класс-метод, возвращающий объект для работы с YouTube API
        """
        return cls.youtube

    def to_json(self, file_name: str) -> None:
        """
        Метод, сохраняющий в файл значения атрибутов экземпляра `Channel`
        """
        with open(file_name, 'w', encoding='utf-8') as file_json:
            json.dump(self.__dict__, file_json, ensure_ascii=False)
