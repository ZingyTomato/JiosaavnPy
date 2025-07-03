from typing import Optional, List, Dict, TypedDict


class ThumbnailDict(TypedDict):
    quality: Dict[str, str]


class ArtistDict(TypedDict):
    artist_id: str
    name: str
    artist_url: str
    thumbnails: ThumbnailDict


class Artists:
    def search_artists(self, search_query: str, limit: Optional[int] = None) -> List[ArtistDict]:
        """Searches Jiosaavn for artists.
        Returns a JSON list of all the artists."""
        if limit is None:
            limit = 5  ## Default to 5 results.
        SEARCH_URL = self.endpoints.SEARCH_ARTISTS_URL.replace("&n=20", f"&n={limit}")
        response = self.requests.get(SEARCH_URL + search_query).json()
        return [self.format_json_search_artists(i) for i in response.get("results", [])]

    def format_json_search_artists(self, artist_json: dict) -> ArtistDict:
        image = artist_json.get('image', '')
        artist: ArtistDict = {
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
        return artist