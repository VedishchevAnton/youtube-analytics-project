import os
from googleapiclient.discovery import build
from datetime import timedelta
import isodate


class PlayList:
    api_key = os.environ.get('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id: str) -> None:
        self.__playlist_id = playlist_id
        self.playlist = self.youtube.playlists().list(id=playlist_id, part='contentDetails,snippet',
                                                      maxResults=50, ).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"
        self.playlist_videos = PlayList.youtube.playlistItems().list(playlistId=playlist_id,
                                                                     part='contentDetails',
                                                                     maxResults=50,
                                                                     ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = PlayList.youtube.videos().list(part='contentDetails,statistics',
                                                             id=','.join(self.video_ids)
                                                             ).execute()

    @property
    def playlist_id(self):
        return self.__playlist_id

    @playlist_id.setter
    def playlist_id(self, playlist_id):
        raise AttributeError("Playlist_id' of 'PlayList' object has no setter")

    @property
    def total_duration(self):
        """
        Метод получения суммарной длительность плейлиста
        """
        # https://developers.google.com/youtube/v3/docs/videos?hl=ru
        total_duration = timedelta(seconds=0)
        for video in self.video_response['items']:
            iso_8601 = video['contentDetails'][
                'duration']  # стандарт охватывающий всемирный обмен и передачу данных, связанных с датой и временем
            duration = isodate.parse_duration(iso_8601)
            total_duration += duration
        return total_duration
