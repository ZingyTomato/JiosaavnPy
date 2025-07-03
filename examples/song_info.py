"""Example to retrieve song info using the track_id.
A song's track_id can be found using the example in `search_songs.py` and collecting the track_id
from the JSON result."""

from jiosaavnpy import jiosaavn

def main():
    jio = JioSaavn() ## Intialize the main class.
    track_id = input("Enter the track id: ") ## See `search_songs.py`
    song_info = jio.song_info(track_id) 
    return print(song_info)

if __name__ == "__main__":
    main()