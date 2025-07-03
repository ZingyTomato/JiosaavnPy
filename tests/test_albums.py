import pytest
from jiosaavnpy import JioSaavn

@pytest.fixture
def client(monkeypatch):
    class MockResponse:
        def json(self):
            return {
                "results": [{
                    "id": "28439174",
                    "title": "Mock Album",
                    "image": "mock_150x150.jpg",
                    "language": "english",
                    "year": "2021",
                    "perma_url": "https://example.com/album",
                    "explicit_content": 0,
                    "more_info": {
                        "song_count": "10",
                        "artistMap": {
                            "artists": [
                                {"name": "Mock Artist", "id": "123", "perma_url": "https://example.com/artist"}
                            ]
                        }
                    }
                }]
            }

    saavn = JioSaavn()
    saavn.requests.get = lambda url: MockResponse()
    return saavn

def test_search_albums(client):
    results = client.search_albums("mock", limit=1)
    assert isinstance(results, list)
    assert results
    album = results[0]
    assert "album_id" in album
    assert "title" in album

def test_format_json_info_albums(client):
    mock_album_data = {
        "albumid": "123456",
        "title": "Test Album",
        "primary_artists": "Test Artist",
        "primary_artists_id": "321",
        "perma_url": "https://example.com/test-album",
        "image": "mock_150x150.jpg",
        "release_date": "2022-01-01",
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
                "320kbps": True
            }
        ]
    }
    album = client.format_json_info_albums(mock_album_data)
    assert album["album_id"] == "123456"
    assert "tracks" in album and len(album["tracks"]) == 1