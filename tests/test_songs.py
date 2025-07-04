import pytest
from jiosaavnpy import JioSaavn

@pytest.fixture
def client(monkeypatch):
    class MockResponse:
        def __init__(self, url):
            self.url = url

        def json(self):
            if "search.getResults" in self.url:
                # This is for search_songs
                return {
                    "results": [{
                        "id": "e0kCEwoC",
                        "title": "Never Gonna Give You Up",
                        "perma_url": "https://example.com/song",
                        "subtitle": "Rick Astley",
                        "image": "image_150x150.jpg",
                        "year": "1987",
                        "language": "english",
                        "play_count": "123456",
                        "explicit_content": 0,
                        "more_info": {
                            "album": "Whenever You Need Somebody",
                            "album_id": "26553699",
                            "album_url": "https://example.com/album",
                            "label": "BMG",
                            "duration": "213",
                            "copyright_text": "© 1987",
                            "320kbps": True,
                            "artistMap": {
                                "primary_artists": [{
                                    "name": "Rick Astley",
                                    "id": "512102",
                                    "perma_url": "https://example.com/artist"
                                }],
                                "featured_artists": []
                            }
                        }
                    }]
                }
            elif "song.getDetails" in self.url:
                # This is for song_info
                return {
                    "e0kCEwoC": {
                        "id": "e0kCEwoC",
                        "song": "Never Gonna Give You Up",
                        "primary_artists": "Rick Astley",
                        "primary_artists_id": "512102",
                        "featured_artists": "",
                        "featured_artists_id": "",
                        "perma_url": "https://example.com/song",
                        "album": "Whenever You Need Somebody",
                        "albumid": "26553699",
                        "album_url": "https://example.com/album",
                        "image": "image_150x150.jpg",
                        "year": "1987",
                        "release_date": "1987-01-01",
                        "language": "english",
                        "label": "BMG",
                        "play_count": "123456",
                        "explicit_content": 0,
                        "duration": "213",
                        "copyright_text": "© 1987",
                        "encrypted_media_url": "fakeurl",
                        "320kbps": True
                    }
                }
            else:
                return {}

    saavn = JioSaavn()
    saavn.requests.get = lambda url: MockResponse(url)
    return saavn

def test_search_songs(client):
    results = client.search_songs("rick")
    assert isinstance(results, list)
    assert results
    assert results[0]["title"] == "Never Gonna Give You Up"
    
def test_search_info(client):
    results = client.song_info("e0kCEwoC")
    assert isinstance(results, dict)
    assert results
    assert results["title"] == "Never Gonna Give You Up"

def test_format_json_info_songs(client):
    mock_song = {
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
    song = client.format_json_info_songs(mock_song)
    assert song["track_id"] == "song123"
    assert "release_date" in song