# 🎶 jiosaavnpy: Unofficial JioSaavn API Client

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLV3-green.svg)](https://github.com/ZingyTomato/JiosaavnPy?tab=GPL-3.0-1-ov-file#readme) [![PyPI Version](https://img.shields.io/pypi/v/jiosaavnpy.svg)](https://pypi.org/project/jiosaavnpy/)

A Python 3 library for accessing JioSaavn's music catalog through their unofficial API. This library emulates JioSaavn web client requests without requiring authentication.

## ✨ Features

### 🔍 Search Capabilities

-   **Songs**: Search for songs with customizable result limits.
-   **Albums**: Search for albums with customizable result limits.
-   **Artists**: Search for artists with customizable result limits.
-   **Playlists**: Search for playlists with customizable result limits.

### 📊 Entity Information

-   **Song Details**: Get comprehensive track information.
-   **Album Information**: Retrieve album metadata and track listings.
-   **Artist Profiles**: Access artist details, top songs, and albums.
-   **Playlist Contents**: Fetch playlist metadata and track lists.

### 🎵 Audio Streaming

-   Multiple quality options (48kbps to 320kbps).
-   Direct streaming URLs for all tracks.
-   Thumbnail images in various resolutions (50x50, 150x150, 500x500).

## 📋 Requirements

-   Python 3.7 or higher.
-   Internet connection for API requests.

## 🔨 Installation

```bash
pip install jiosaavnpy

```

## 🚀 Quick Start

```python
from jiosaavnpy import JioSaavn

# Initialize the client
jio = JioSaavn()

# Search for songs
results = jio.search_songs("Never gonna give you up", limit=5)
print(results[0]['title'])  # "Never Gonna Give You Up"

# Get detailed song information
track_id = results[0]['track_id']
song_details = jio.song_info(track_id)
print(song_details['stream_urls']['high_quality'])

```

## 📖 Usage Examples

### Searching for Songs

```python
from jiosaavnpy import JioSaavn

def search_songs_example():
    """Search for songs and display results."""
    jio = JioSaavn()
    
    query = input("Enter song name: ")
    results = jio.search_songs(query, limit=10)
    
    for i, song in enumerate(results, 1):
        print(f"{i}. {song['title']} - {song['primary_artists']}")
     including streaming URLs
    return results

# Run the example
songs = search_songs_example()

```

### Getting Song Information

```python
from jiosaavnpy import JioSaavn

def get_song_details():
    """Retrieve detailed information about a specific song."""
    jio = JioSaavn()
    
    # Use track_id from search results
    track_id = "e0kCEwoC"  # Never Gonna Give You Up
    song_info = jio.song_info(track_id)
    
    print(f"Title: {song_info['title']}")
    print(f"Artist: {song_info['primary_artists']}")
    print(f"Album: {song_info['album_name']}")
    print(f"Duration: {song_info['duration']} seconds")
    print(f"Year: {song_info['release_year']}")
    
    return song_info

# Run the example
details = get_song_details()

```

### Working with Albums

```python
from jiosaavnpy import JioSaavn

def explore_album():
    """Search for albums and get detailed information."""
    jio = JioSaavn()
    
    # Search for albums
    albums = jio.search_albums("Whenever You Need Somebody", limit=3)
    
    if albums:
        album_id = albums[0]['album_id']
        album_details = jio.album_info(album_id)
        
        print(f"Album: {album_details['album_name']}")
        print(f"Artist: {album_details['primary_artists']}")
        print(f"Tracks: {len(album_details['tracks'])}")
        
        # List all tracks
        for track in album_details['tracks']:
            print(f"  - {track['title']}")

# Run the example
explore_album()

```

Check out [`examples`](https://github.com/ZingyTomato/JiosaavnPy/tree/main/examples) for more usage examples.

## 📚 API Reference

### Search Methods

#### `search_songs(search_query, limit=5)`

Search for songs by name, artist, or lyrics.

**Parameters:**

-   `search_query` (str): Search term for songs.
-   `limit` (int, optional): Number of results to return (default: 5).

**Returns:** List of song dictionaries with metadata.

#### `search_albums(search_query, limit=5)`

Search for albums by name or artist.

**Parameters:**

-   `search_query` (str): Search term for albums.
-   `limit` (int, optional): Number of results to return (default: 5).

**Returns:** List of album dictionaries.

#### `search_artists(search_query, limit=5)`

Search for artists by name.

**Parameters:**

-   `search_query` (str): Artist name to search for.
-   `limit` (int, optional): Number of results to return (default: 5).

**Returns:** List of artist dictionaries.

#### `search_playlists(search_query, limit=5)`

Search for playlists by name or description.

**Parameters:**

-   `search_query` (str): Playlist name to search for.
-   `limit` (int, optional): Number of results to return (default: 5).

**Returns:** List of playlist dictionaries.

### Information Methods

#### `song_info(track_id)`

Get detailed information about a specific song.

**Parameters:**

-   `track_id` (str): Unique identifier for the track

**Returns:** Dictionary with comprehensive song information

#### `album_info(album_id)`

Get detailed information about a specific album.

**Parameters:**

-   `album_id` (str): Unique identifier for the album

**Returns:** Dictionary with album information and track list

#### `artist_info(artist_token, song_limit=5, album_limit=5)`

Get detailed information about a specific artist.

**Parameters:**

-   `artist_token` (str): Unique identifier for the artist
-   `song_limit` (int, optional): Number of top songs to include (default: 5)
-   `album_limit` (int, optional): Number of top albums to include (default: 5)

**Returns:** Dictionary with artist information, top songs, and albums

#### `playlist_info(playlist_id)`

Get detailed information about a specific playlist.

**Parameters:**

-   `playlist_id` (str): Unique identifier for the playlist

**Returns:** Dictionary with playlist information and track list

### Other Methods

#### `similar_songs(track_id)`

Get related songs based on its `track_id`. 

**Parameters:**

-   `track_id` (str): Unique identifier for the track.

## 📋 Response Format

### Song Object

```json
{
  "track_id": "e0kCEwoC",
  "title": "Never Gonna Give You Up",
  "primary_artists": "Rick Astley",
  "primary_artists_ids": "512102",
  "album_name": "Whenever You Need Somebody",
  "album_id": "26553699",
  "duration": "213",
  "release_year": "1987",
  "track_language": "english",
  "play_count": "199567",
  "is_explicit": false,
  "thumbnails": {
    "quality": {
      "50x50": "https://c.saavncdn.com/...",
      "150x150": "https://c.saavncdn.com/...",
      "500x500": "https://c.saavncdn.com/..."
    }
  },
  "stream_urls": {
    "low_quality": "https://aac.saavncdn.com/...48.mp4",
    "medium_quality": "https://aac.saavncdn.com/...96.mp4",
    "high_quality": "https://aac.saavncdn.com/...160.mp4",
    "very_high_quality": "https://aac.saavncdn.com/...320.mp4"
  }
}

```

## ⚠️ Important Notes

-   **Unofficial API**: This library uses JioSaavn's internal API endpoints and is not officially supported.
-   **Geographic Restrictions**: Non-English tracks may not be available when accessed from non-Indian IP addresses.
-   **Rate Limits**: There are no known rate limits as of now (?).

## 🤝 Contributing

Contributions are welcome! There may be certain endpoints which have not been fully covered yet.