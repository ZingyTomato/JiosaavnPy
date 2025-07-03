import requests
from jiosaavnpy import endpoints
from jiosaavnpy.songs.songs import Songs
from jiosaavnpy.albums.albums import Albums
from jiosaavnpy.playlists.playlists import Playlists
from jiosaavnpy.artists.artists import Artists
from jiosaavnpy.functions import Functions

class JioSaavn(Songs, Albums, Playlists, Artists, Functions): ## Inherit all classes.
    """Class containing all objects for jiosaavnpy. 
    Allows to perform various requests in order to search get info on: Songs, Albums, Playlists and Artists.
    
    Available options: 

    search_songs: Allows to search Jiosaavn for tracks.
    search_albums: Allows to search Jiosaavn for albums.
    search_playlists: Allows to search Jiosaavn for playlists.
    song_info: Retrieve info on a track using its track_id.
    album_info: Retrieve info on an album using its album_id.
    playlist_info: Retrieve info on a playlist using its playlist_id.
    """
    def __init__(self):
        self.requests = requests.Session() ## Use the same request session for all functions.
        self.endpoints = endpoints ## API endpoints.