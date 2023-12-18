# spotify_controller.py

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Credentials and Setup
SPOTIFY_CLIENT_ID = '2978daaf8a6845b9bd5036c89fe33179'
SPOTIFY_CLIENT_SECRET = '37d229b68df74e4ba187be68b61d9ff3'
SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback'

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope='user-read-playback-state user-modify-playback-state'))

def is_track_playing():
    try:
        playback_state = sp.current_playback()
        return playback_state is not None and playback_state['is_playing']
    except Exception as e:
        print(f"Error checking playback state: {e}")
        return False

def search_and_play(query):
    try:
        if "playlist:" in query:
            # Extract playlist URI and play
            playlist_uri = query.split("playlist:")[1].strip()
            sp.start_playback(context_uri=playlist_uri)
        else:
            # Search for a track
            results = sp.search(q=query, limit=1, type='track')
            tracks = results['tracks']['items']
            if tracks:
                track_uri = tracks[0]['uri']
                sp.start_playback(uris=[track_uri])
    except Exception as e:
        print(f"Error in search_and_play: {e}")

def skip_current_track():
    try:
        sp.next_track()
        print("Skipped to next track.")
    except Exception as e:
        print(f"Error skipping track: {e}")
