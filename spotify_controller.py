# spotify_controller.py

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from queue import Queue

# Spotify Credentials and Setup
cache_path = '/home/spotify_sms/.spotipy_cache'
SPOTIFY_CLIENT_ID = 'your_spotify_client_id'  # Replace with your Spotify Client ID
SPOTIFY_CLIENT_SECRET = 'your_spotify_client_secret'  # Replace with your Spotify Client Secret
SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback'  # Replace with your Spotify Redirect URI

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
        results = sp.search(q=query, limit=1, type='track')
        tracks = results['tracks']['items']
        if tracks:
            track_uri = tracks[0]['uri']
            sp.start_playback(uris=[track_uri])
            print(f"Playing: {tracks[0]['name']} by {tracks[0]['artists'][0]['name']}")
    except Exception as e:
        print(f"Error in search_and_play: {e}")
