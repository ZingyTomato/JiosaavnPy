from typing import Optional, List, Dict, TypedDict

class ThumbnailDict(TypedDict):
    quality: Dict[str, str]

class ArtistDict(TypedDict):
    artist_id: str
    name: str
    artist_url: str
    artist_token: str
    thumbnails: ThumbnailDict

class ArtistInfoDict(TypedDict):
    artist_id: str
    name: str
    subtitle: str
    thumbnails: ThumbnailDict
    follower_count: int
    role: str
    is_verified: bool
    artist_language: str
    artist_type: str
    top_songs: Dict[str, str]
    top_albums: Dict[str, str]
    dedicated_playlists: Dict[str, str]
    featured_playlists: Dict[str, str]
    singles: Dict[str, str]
    latest_release: Dict[str, str]

class Artists:
    def search_artists(self, search_query: str, limit: Optional[int] = None) -> List[ArtistDict]:
        """
            Search for artists on JioSaavn.

            Args:
                search_query: Artist name or related keywords.
                limit: Max number of results to return (default: 5).

            Returns:
                A list of ArtistDict objects matching the query.
            """
            
        if limit is None:
            limit = 5  ## Default to 5 results.
        SEARCH_URL = self.endpoints.SEARCH_ARTISTS_URL.replace("&n=20", f"&n={limit}")
        response = self.requests.get(SEARCH_URL + search_query).json()
        return [self.format_json_search_artists(i) for i in response.get("results", [])]
    
    def artist_info(self, artist_id: str, song_limit: Optional[int] = None,
                    album_limit: Optional[int] = None) -> List[ArtistInfoDict]:
        """
            Get detailed info for a specific artist.

            Args:
                artist_id: The JioSaavn artist ID.
                Example: `512102`
                song_limit: Max number of top songs to return (default: 5).
                album_limit: Max number of top albums to return (default: 5).

            Returns:
                A list containing artist info, top songs, albums, playlists, and latest releases.
        """
            
        if song_limit is None:
            song_limit = 5  ## Default to 5 song results.
        if album_limit is None:
            album_limit = 5  ## Default to 5 album results.
        TEMP_INFO_URL = self.endpoints.ARTIST_DETAILS_URL.replace("&n_song=1", f"&n_song={song_limit}")
        INFO_URL = TEMP_INFO_URL.replace("&n_album=1", f"&n_album={album_limit}")
        response = self.requests.get(INFO_URL + artist_id).json()
        return [self.format_json_info_artists(response)]

    def format_json_search_artists(self, artist_json: dict) -> ArtistDict:
        image = artist_json.get('image', '')
        return {
            'artist_id': artist_json.get('id', ''),
            'name': artist_json.get('name', ''),
            'artist_url': artist_json.get('perma_url', ''),
            'thumbnails': {
                'quality': {
                    '50x50': image,
                    '150x150': image.replace("50x50", "150x150"),
                    '500x500': image.replace("50x50", "500x500")
                }
            }
        }
    
    def format_json_info_artists(self, artist_json: dict) -> ArtistInfoDict:
        image = artist_json.get('image', '')
        return {
            'artist_id': artist_json.get('artistId', ''),
            'name': artist_json.get('name', ''),
            'subtitle': artist_json.get('subtitle', ''),
            'role': artist_json.get('type', ''),
            'is_verified': artist_json.get('isVerified', ''),
            'artist_language': artist_json.get('dominantLanguage'),
            'artist_type': artist_json.get('dominantType', ''),
            'thumbnails': {
                'quality': {
                    '50x50': image.replace("150x150", "50x50"),
                    '150x150': image,
                    '500x500': image.replace("150x150", "500x500")
                }
            },
            'top_songs': [self.format_json_info_songs(i) for i in artist_json['topSongs']['songs']],
            'top_albums': [self.format_json_artists_albums(i) for i in artist_json['topAlbums']['albums']],
        }