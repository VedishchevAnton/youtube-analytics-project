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
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        raise AttributeError("Channel_id' of 'Channel' object has no setter")

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

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.view_count + other.view_count

    def __sub__(self, other):
        return int(self.view_count) - int(other.view_count)



