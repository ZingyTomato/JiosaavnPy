"""Example to retrieve playlist info using the playlist_id.
A playlist's playlist_id can be found using the example in `search_playlists.py` and collecting the playlist_id
from the JSON result."""

from jiosaavnpy import jiosaavn

def main():
    jio = JioSaavn() ## Initiate the main class.
    playlist_id = input("Enter the playlist_id: ") ## See `search_playlists.py`
    playlist_info = jio.playlist_info(playlist_id) 
    return print(playlist_info)

if __name__ == "__main__":
    main()