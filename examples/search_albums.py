"""Example to search for albums."""

from jiosaavnpy import jiosaavn

def main():
    jio = JioSaavn() ## Initiate the main class.
    album_name = input("Search for an Album: ")
    album_results = jio.search_albums(album_name, limit=5) ## Limit can be set to any int, defaults to 5 if not provided.
    album_id = album_results[0]['album_id'] ## Useful for album info in `album_info.py`.
    return print(album_results)

if __name__ == "__main__":
    main()