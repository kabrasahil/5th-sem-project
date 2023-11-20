import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = '48b2d90f2cd74403a7fee754d1c6ddbf'
client_secret = '1a0a5e46e1234480acca493d74adf194'


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Input genre and maximum monthly listeners
genre = 'hip hop' # Replace with your desired genre
max_listeners = 100

# Search for tracks with the specified genre
results = sp.search(q=f'genre:"{genre}"', type='track', limit=50)  # You can adjust the limit

# Filter tracks based on monthly listeners
filtered_tracks = []

for track in results['tracks']['items']:
    if track['popularity'] and track['popularity'] < max_listeners:
        filtered_tracks.append(track)

# Display the filtered tracks
if not filtered_tracks:
    print(f"No {genre} tracks found with less than {max_listeners} monthly listeners.")
else:
    print(f"Tracks in the {genre} genre with less than {max_listeners} monthly listeners:")
    for track in filtered_tracks:
        print(f"{track['name']} by {', '.join([artist['name'] for artist in track['artists']])} - {track['popularity']} monthly listeners")