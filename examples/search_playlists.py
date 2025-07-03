"""Example to search for playlists."""

from jiosaavnpy import jiosaavn

def main():
    jio = JioSaavn() ## Initiate the main class.
    playlist_name = input("Search for a Playlist: ")
    playlist_results = jio.search_playlists(playlist_name, limit=5) ## Limit can be set to any int, defaults to 5 if not provided.
    playlist_id = playlist_results[0]['playlist_id'] ## Useful for playlist info in `playlist_info.py`.
    return print(playlist_results)

if __name__ == "__main__":
    main()