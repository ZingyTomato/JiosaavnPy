"""Example to retrieve album info using the album_id.
An album's album_id can be found using the example in `search_albums.py` and collecting the album_id
from the JSON result."""

from jiosaavnpy import jiosaavn

def main():
    jio = JioSaavn() ## Initiate the main class.
    album_id = input("Enter the album_id: ") ## See `search_albums.py`
    album_info = jio.album_info(album_id)
    return print(album_info)

if __name__ == "__main__":
    main()