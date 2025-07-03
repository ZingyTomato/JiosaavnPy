import pytest
from jiosaavnpy import JioSaavn

@pytest.fixture
def client(monkeypatch):
    class MockResponse:
        def json(self):
            return {
                "results": [{
                    "id": "512102",
                    "name": "Mock Artist",
                    "perma_url": "https://example.com/artist",
                    "image": "image_50x50.jpg"
                }]
            }

    saavn = JioSaavn()
    saavn.requests.get = lambda url: MockResponse()
    return saavn

def test_search_artists(client):
    results = client.search_artists("mock", limit=1)
    assert isinstance(results, list)
    assert results
    artist = results[0]
    assert "artist_id" in artist
    assert "name" in artist
    
def test_format_json_search_artists(client):
    mock_artist = {
        "id": "512102",
        "name": "Rick Astley",
        "perma_url": "https://example.com/artist",
        "image": "image_50x50.jpg"
    }
    artist = client.format_json_search_artists(mock_artist)
    assert artist["artist_id"] == "512102"
    assert artist["name"] == "Rick Astley"