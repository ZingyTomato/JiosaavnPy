"""Example to search for artists."""

from jiosaavnpy import jiosaavn

def main():
    jio = JioSaavn() ## Initiate the main class.
    artist_name = input("Search for an Artist: ")
    artist_results = jio.search_artists(artist_name, limit=5) ## Limit can be set to any int, defaults to 5 if not provided.
    artist_id = artist_results[0]['artist_id'] ## Useful for album info in `album_info.py`.
    return print(artist_results)

if __name__ == "__main__":
    main()