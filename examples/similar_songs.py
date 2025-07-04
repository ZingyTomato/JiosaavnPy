"""Example to get similar songs. A song's track_id can be found using the example in `search_songs.py` and collecting the track_id
from the JSON result."""

from jiosaavnpy import jiosaavn

def main():
    jio = JioSaavn() ## Intialize the main class.
    track_id = input("Enter the track_id: ")
    song_results = jio.similar_songs(track_id)
    return print(song_results) ## Returns a list of recommended tracks.

if __name__ == "__main__":
    main()