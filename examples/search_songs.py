"""Example to search for songs."""

from jiosaavnpy import jiosaavn

def main():
    jio = JioSaavn() ## Intialize the main class.
    song_name = input("Search for a Song: ")
    song_results = jio.search_songs(song_name, limit=5) ## Limit can be set to any int, defaults to 5 if not provided.
    track_id = song_results[0]['track_id'] ## Useful for track info in `song_info.py`.
    return print(song_results)

if __name__ == "__main__":
    main()