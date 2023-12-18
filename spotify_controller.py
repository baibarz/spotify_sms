import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re


# Spotify Credentials and Setup
SPOTIFY_CLIENT_ID = 'e13ceed3a5d84229954c8c49bb497124'
SPOTIFY_CLIENT_SECRET = '16fa064bf7b04f86ba7afefacc221b29'
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
        # Check for HTTP Spotify link for a playlist with optional parameters
        match = re.search(r'open\.spotify\.com/playlist/([a-zA-Z0-9]+)', query)
        if match:
            # Extract playlist ID and convert to URI
            playlist_id = match.group(1)
            playlist_uri = f'spotify:playlist:{playlist_id}'
            sp.start_playback(context_uri=playlist_uri)
        else:
            # Existing logic for track search
            results = sp.search(q=query, limit=1, type='track')
            tracks = results['tracks']['items']
            if tracks:
                track_uri = tracks[0]['uri']
                sp.start_playback(uris=[track_uri])
    except Exception as e:
        print(f"Error in search_and_play for '{query}': {e}")

def skip_current_track():
    try:
        sp.next_track()
        print("Skipped to next track.")
    except Exception as e:
        print(f"Error skipping track: {e}")
