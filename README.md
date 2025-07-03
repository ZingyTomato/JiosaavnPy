# 🎶 jiosaavnpy: An unofficial API for Jiosaavn

## Introduction

jiosaavnpy is a Python 3 library to send requests to the Jiosaavn API.
It emulates Jiosaavn web client requests without the need for any authentication.

## 📖 Table of Contents

* [`Features`](#-features)
* [`Installation`](#-installation)
* [`Usage`](#-usage)

* [`API`](#api)

  * [`API Methods`](#-api-methods)

* [`Caveats`](#-caveats)
* [`Contributing`](#-contributing)


## 🎧 Features

### 🔍 Searching:

* Search for Songs (can specify result limits)
* Search for Albums (can specify result limits)
* Search for Artists (can specify result limits)
* Search for Albums (can specify result limits)
* Search for Playlists (can specify result limits)

### Entity Information:

* Retrieve information about a specific Song (requires a `track_id`)
* Retrieve information about a specific Album (requires an `album_id`)
* Retrieve information about a specific Playlist (requires a `playlist_id`)
* Retrieve information about a specific Artist (requires a `artist_id`)

## Requirements

- Python 3.7 or higher - https://www.python.org

## 🔨 Installation

```sh
pip install jiosaavnpy
```

## 👨🏻‍💻 Usage

- To search for Songs:

```python
"""Example to search for songs."""

from jiosaavnpy import jiosaavn

def main():
    jio = JioSaavn() ## Intialize the main class.
    song_name = input("Search for a Song: ")
    song_results = jio.search_songs(song_name, limit=5) ## Limit can be set to any int, defaults to 5 if not provided.
    track_id = song_results[0]['track_id'] ## Useful for track info in example below.
    return print(song_results)

if __name__ == "__main__":
    main()
```

**Parameters:**

- `search_query` *(str)*: Name of the track.  
  Example: `"Never gonna give you up"`
- `limit` *(int, optional)*: Number of tracks to return.  
  Example: `1`, `5`, `10` (default is 5)

**Example response** (with `limit=1`):

```json
[
  {
    "track_id": "e0kCEwoC",
    "title": "Never Gonna Give You Up",
    "primary_artists": "Rick Astley",
    "primary_artists_ids": "512102",
    "primary_artists_urls": "https://www.jiosaavn.com/artist/rick-astley-/tgLD-55V-uc_",
    "featured_artists": "",
    "featured_artists_ids": "",
    "featured_artists_urls": "",
    "track_url": "https://www.jiosaavn.com/song/never-gonna-give-you-up/FVgAcjFHWHA",
    "track_subtitle": "Rick Astley - Whenever You Need Somebody",
    "album_name": "Whenever You Need Somebody",
    "album_id": "26553699",
    "album_url": "https://www.jiosaavn.com/album/whenever-you-need-somebody/Tr67aKPn6fU_",
    "thumbnails": {
      "quality": {
        "50x50": "https://c.saavncdn.com/694/Whenever-You-Need-Somebody-English-1987-20210329114358-50x50.jpg",
        "150x150": "https://c.saavncdn.com/694/Whenever-You-Need-Somebody-English-1987-20210329114358-150x150.jpg",
        "500x500": "https://c.saavncdn.com/694/Whenever-You-Need-Somebody-English-1987-20210329114358-500x500.jpg"
      }
    },
    "release_year": "1987",
    "track_language": "english",
    "label": "BMG Rights Management (UK) Ltd",
    "play_count": "199567",
    "is_explicit": false,
    "duration": "213",
    "copyright_text": "℗ 1987 Sony Music Entertainment UK Limited",
    "stream_urls": {
        "low_quality": "https://aac.saavncdn.com/768/6d5c0e88195f6048dc7e78a06eafde0d_48.mp4",
        "medium_quality": "https://aac.saavncdn.com/768/6d5c0e88195f6048dc7e78a06eafde0d_96.mp4",
        "high_quality": "https://aac.saavncdn.com/768/6d5c0e88195f6048dc7e78a06eafde0d_160.mp4",
        "very_high_quality": "https://aac.saavncdn.com/768/6d5c0e88195f6048dc7e78a06eafde0d_320.mp4"
        }
  }
]
```

- To get information on a specific Song:

```python
"""Example to retrieve song info using the track_id.
A song's track_id can be found using the example above and collecting the track_id from the JSON result."""

from jiosaavnpy import jiosaavn

def main():
    jio = JioSaavn() ## Intialize the main class.
    track_id = input("Enter the track id: ") ## The track_id from the previous example
    song_info = jio.song_info(track_id) 
    return print(song_info)

if __name__ == "__main__":
    main()
```

**Parameters:**

- `track_id` *(str)*: Can be found using search_songs() as `track_id`.  
  Example: `"e0kCEwoC"`

The JSON response is the same as `search_songs`.

Check out [`examples`](https://github.com/ZingyTomato/JiosaavnPy/tree/main/examples) for more usage examples.

# API

## 📙 API methods

### `search_songs`

**Parameters:**

- `search_query` *(str)*: Name of the track.  
  Example: `"Never gonna give you up"`
- `limit` *(int, optional)*: Number of tracks to return.  
  Example: `1`, `5`, `10` (default is 5)

### `song_info`

**Parameters:**

- `track_id` *(str)*: Can be found using search_songs() as `track_id`.  
  Example: `"e0kCEwoC"`

### `search_albums`

**Parameters:**

- `search_query` *(str)*: Name of the album.
- `limit` *(int, optional)*: Number of albums to return. 
  Example: `1`, `5`, `10` (default is 5)

### `album_info`

**Parameters:**

- `album_id` *(str)*: Can be found using search_albums() as `album_id`.  
  Example: `"28439174"`

### `search_artists`

**Parameters:**

- `search_query` *(str)*: Name of the artist.
- `limit` *(int, optional)*: Number of artists to return. 
  Example: `1`, `5`, `10` (default is 5)

### `search_playlists`

**Parameters:**

- `search_query` *(str)*: Name of the playlist.
- `limit` *(int, optional)*: Number of playlists to return. 
  Example: `1`, `5`, `10` (default is 5)

### `playlist_info`

**Parameters:**

- `playlist_id` *(str)*: Can be found using search_playlists() as `playlist_id`.  
  Example: `"848372056"`

## ❔ Caveats

* This is not an official or supported API.
* Non-English tracks are not returned by Jiosaavn if made from a non-Indian IP address.
* Any sort of rate limits are not publicly known (?).

## 🏥 Contributing

Pull requests are welcome. There are still some endpoints that have not yet implemented.