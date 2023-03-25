import os
from googleapiclient.discovery import build
import datetime


class PlayList:
    api_key = os.environ.get('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.playlist = self.youtube.playlists().list(id=self.__playlist_id, part='contentDetails,snippet',
                                                      maxResults=50, ).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"

    @property
    def playlist_id(self):
        return self.__playlist_id

    @playlist_id.setter
    def playlist_id(self, playlist_id):
        raise AttributeError("Playlist_id' of 'PlayLIst' object has no setter")




