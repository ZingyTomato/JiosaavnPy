from typing import Optional, List, TypedDict, Dict
import html
import logging

logger = logging.getLogger(__name__)


class StreamURLs(TypedDict, total=False):
    low_quality: str
    medium_quality: str
    high_quality: str
    very_high_quality: str


class ThumbnailQuality(TypedDict):
    quality: Dict[str, str]


class TrackData(TypedDict):
    track_id: str
    title: str
    primary_artists: str
    primary_artists_ids: str
    primary_artists_urls: str
    featured_artists: Optional[str]
    featured_artists_ids: Optional[str]
    featured_artists_urls: Optional[str]
    track_url: str
    track_subtitle: str
    album_name: str
    album_id: str
    album_url: str
    thumbnails: ThumbnailQuality
    release_year: str
    release_date: Optional[str]
    track_language: str
    label: str
    play_count: str
    is_explicit: bool
    duration: str
    copyright_text: str
    stream_urls: StreamURLs | str


class Songs:
    def search_songs(self, search_query: str, limit: Optional[int] = None) -> List[TrackData]:
        if limit is None:
            limit = 5
        SEARCH_URL = self.endpoints.SEARCH_SONGS_URL.replace("&n=20", f"&n={limit}")
        response = self.requests.get(SEARCH_URL + search_query).json()
        return [self.format_json_search_songs(i) for i in response.get("results", [])]

    def song_info(self, track_id: str) -> TrackData:
        response = self.requests.get(self.endpoints.SONG_DETAILS_URL + track_id).json()
        return self.format_json_info_songs(response[track_id])

    def format_json_search_songs(self, track_json: dict) -> TrackData:
        primary_artist_location = track_json["more_info"]["artistMap"]["primary_artists"]
        featured_artist_location = track_json["more_info"]["artistMap"].get("featured_artists", [])

        thumbnails = {
            "quality": {
                "50x50": track_json["image"].replace("150x150", "50x50"),
                "150x150": track_json["image"],
                "500x500": track_json["image"].replace("150x150", "500x500"),
            }
        }

        track = TrackData(
            track_id=track_json["id"],
            title=html.unescape(track_json["title"]),
            primary_artists=self.get_primary_artists(primary_artist_location),
            primary_artists_ids=self.get_primary_artists_ids(primary_artist_location),
            primary_artists_urls=self.get_primary_artists_urls(primary_artist_location),
            featured_artists=self.get_featured_artists(featured_artist_location),
            featured_artists_ids=self.get_featured_artists_ids(featured_artist_location),
            featured_artists_urls=self.get_featured_artists_urls(featured_artist_location),
            track_url=track_json["perma_url"],
            track_subtitle=track_json["subtitle"],
            album_name=track_json["more_info"]["album"],
            album_id=track_json["more_info"]["album_id"],
            album_url=track_json["more_info"]["album_url"],
            thumbnails=thumbnails,
            release_year=track_json["year"],
            release_date=None,
            track_language=track_json["language"],
            label=track_json["more_info"]["label"],
            play_count=track_json["play_count"],
            is_explicit=self.is_explicit(track_json["explicit_content"]),
            duration=track_json["more_info"]["duration"],
            copyright_text=track_json["more_info"]["copyright_text"],
            stream_urls=""
        )

        try:
            track["stream_urls"] = self.decrypt_stream_url(
                track_json["more_info"]["encrypted_media_url"],
                track_json["more_info"]["320kbps"]
            )
        except KeyError:
            logger.warning("Missing stream URL")

        return track

    def format_json_info_songs(self, track_json: dict) -> TrackData:
        thumbnails = {
            "quality": {
                "50x50": track_json["image"].replace("150x150", "50x50"),
                "150x150": track_json["image"],
                "500x500": track_json["image"].replace("150x150", "500x500"),
            }
        }

        track = TrackData(
            track_id=track_json["id"],
            title=html.unescape(track_json["song"]),
            primary_artists=track_json["primary_artists"],
            primary_artists_ids=track_json["primary_artists_id"],
            primary_artists_urls="",  # Not present in info endpoint
            featured_artists=track_json["featured_artists"],
            featured_artists_ids=track_json["featured_artists_id"],
            featured_artists_urls="",  # Not present in info endpoint
            track_url=track_json["perma_url"],
            track_subtitle="",  # Not in song detail
            album_name=track_json["album"],
            album_id=track_json["albumid"],
            album_url=track_json["album_url"],
            thumbnails=thumbnails,
            release_year=track_json["year"],
            release_date=track_json["release_date"],
            track_language=track_json["language"],
            label=track_json["label"],
            play_count=track_json["play_count"],
            is_explicit=self.is_explicit(track_json["explicit_content"]),
            duration=track_json["duration"],
            copyright_text=track_json["copyright_text"],
            stream_urls=""
        )

        try:
            track["stream_urls"] = self.decrypt_stream_url(
                track_json["encrypted_media_url"],
                track_json["320kbps"]
            )
        except KeyError:
            logger.warning("Missing stream URL")

        return track