import pytest
from jiosaavnpy.functions import Functions

funcs = Functions()

def test_decrypt_stream_url():
    # using dummy encrypted data (must match expected format if real decryption used)
    encrypted = "ID2ieOjCrwfgWvL5sXl4B1ImC5QfbsDyU+Aoir6Hz0CyHeNa39Pv2RTxdgjbEgs66Ixn4EmaXOCBmEK9iGz4WRw7tS9a8Gtq"  # base64 for 'dummy_encrypted'
    urls = funcs.decrypt_stream_url(encrypted, is_320kbps=True)
    assert isinstance(urls, dict)
    assert "low_quality" in urls

def test_format_stream_url():
    dummy_url = "https://preview.saavncdn.com/song_96_p.mp4"
    urls = funcs.format_stream_url(dummy_url, True)
    assert urls["very_high_quality"].endswith("_320.mp4")

def test_is_explicit():
    assert funcs.is_explicit(1) is True
    assert funcs.is_explicit(0) is False

def test_get_primary_artists():
    artists = [{"name": "Artist One"}, {"name": "Artist Two"}]
    assert funcs.get_primary_artists(artists) == "Artist One, Artist Two"

def test_get_featured_artists_none():
    assert funcs.get_featured_artists(None) is None
    
def test_get_primary_ids_urls():
    artist_json = [{"name": "A", "id": "1", "perma_url": "url"}]
    assert funcs.get_primary_artists_ids(artist_json) == "1"
    assert funcs.get_primary_artists_urls(artist_json) == "url"
    
def test_get_featured_artists_helpers():
    artist_json = [{"name": "B", "id": "2", "perma_url": "url2"}]
    assert funcs.get_featured_artists_ids(artist_json) == "2"
    assert funcs.get_featured_artists_urls(artist_json) == "url2"