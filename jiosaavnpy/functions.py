from typing import List, Dict, Optional, Callable
from pyDes import des, ECB, PAD_PKCS5
import base64


class Functions:
    """Contains commonly used utility functions for processing JioSaavn metadata."""

    def decrypt_stream_url(self, stream_url: str, is_320kbps: bool) -> Dict[str, str]:
        try:
            des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
            enc_url = base64.b64decode(stream_url.strip())
            dec_url = des_cipher.decrypt(enc_url, padmode=PAD_PKCS5).decode('utf-8')

            return {
                'low_quality': dec_url.replace("_96.mp4", "_48.mp4"),
                'medium_quality': dec_url,
                'high_quality': dec_url.replace("_96.mp4", "_160.mp4"),
                'very_high_quality': dec_url.replace("_96.mp4", "_320.mp4") if is_320kbps else ""
            }

        except Exception as e:
            # You can log or print the error here if desired
            return {
                'low_quality': '',
                'medium_quality': '',
                'high_quality': '',
                'very_high_quality': ''
            }

    def is_explicit(self, value: int) -> bool:
        return value == 1

    def get_primary_artists(self, artist_json: List[dict]) -> str:
        return self._collect_artist_field(artist_json, "name")

    def get_primary_artists_ids(self, artist_json: List[dict]) -> str:
        return self._collect_artist_field(artist_json, "id")

    def get_primary_artists_urls(self, artist_json: List[dict]) -> str:
        return self._collect_artist_field(artist_json, "perma_url")

    def get_featured_artists(self, artist_json: Optional[List[dict]]) -> Optional[str]:
        return self._collect_artist_field(artist_json, "name") if artist_json else None

    def get_featured_artists_ids(self, artist_json: Optional[List[dict]]) -> Optional[str]:
        return self._collect_artist_field(artist_json, "id") if artist_json else None

    def get_featured_artists_urls(self, artist_json: Optional[List[dict]]) -> Optional[str]:
        return self._collect_artist_field(artist_json, "perma_url") if artist_json else None

    def _collect_artist_field(self, artist_json: List[dict], key: str) -> str:
        return ', '.join(str(artist.get(key, "")) for artist in artist_json)