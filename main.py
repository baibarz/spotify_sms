# main.py

import threading
import time
from sms_handler import init_modem, send_at_command, delete_sms
from spotify_controller import search_and_play, is_track_playing
from queue import Queue

song_queue = Queue()
current_song_playing = False

def check_for_new_sms():
    global current_song_playing
    while True:
        # ... (implement the logic from your original code)
        time.sleep(2)

def play_music_from_queue():
    global current_song_playing
    while True:
        # ... (implement the logic from your original code)
        time.sleep(1)

# Initialize modem
init_modem()

# Start SMS checking in a separate thread
sms_thread = threading.Thread(target=check_for_new_sms)
sms_thread.daemon = True
sms_thread.start()

# Start music playback manager in a separate thread
music_thread = threading.Thread(target=play_music_from_queue)
music_thread.daemon = True
music_thread.start()

# Main program loop
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated by user")
