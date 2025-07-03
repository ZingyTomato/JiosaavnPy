import pytest
from jiosaavnpy import JioSaavn

@pytest.fixture
def client(monkeypatch):
    class MockResponse:
        def json(self):
            return {
                "results": [{
                    "id": "848372056",
                    "title": "Mock Playlist",
                    "subtitle": "Mocker",
                    "image": "image_150x150.jpg",
                    "perma_url": "https://example.com/playlist",
                    "explicit_content": 0,
                    "more_info": {
                        "song_count": "15",
                        "language": "english"
                    }
                }]
            }

    saavn = JioSaavn()
    saavn.requests.get = lambda url: MockResponse()
    return saavn

def test_search_playlists(client):
    results = client.search_playlists("mock")
    assert isinstance(results, list)
    assert results
    playlist = results[0]
    assert "playlist_id" in playlist
    assert "title" in playlist

def test_format_json_info_playlists(client):
    mock_playlist_data = {
        "listid": "848372056",
        "listname": "Mock Playlist",
        "follower_count": "10000",
        "perma_url": "https://example.com/playlist",
        "type": "chart",
        "image": "image_150x150.jpg",
        "list_count": "10",
        "songs": [
            {
                "id": "song123",
                "song": "Track One",
                "primary_artists": "Artist A",
                "primary_artists_id": "111",
                "featured_artists": "",
                "featured_artists_id": "",
                "perma_url": "https://example.com/song",
                "album": "Test Album",
                "albumid": "123456",
                "album_url": "https://example.com/test-album",
                "image": "mock_150x150.jpg",
                "year": "2022",
                "release_date": "2022-01-01",
                "language": "english",
                "label": "Test Label",
                "play_count": "1000",
                "explicit_content": 0,
                "duration": "210",
                "copyright_text": "© 2022",
                "encrypted_media_url": "ID2ieOjCrwfgWvL5sXl4B1ImC5QfbsDyU+Aoir6Hz0CyHeNa39Pv2RTxdgjbEgs66Ixn4EmaXOCBmEK9iGz4WRw7tS9a8Gtq",
                "320kbps": False
            }
        ]
    }
    playlist = client.format_json_info_playlists(mock_playlist_data)
    assert playlist["playlist_id"] == "848372056"
    assert "tracks" in playlist and isinstance(playlist["tracks"], list)