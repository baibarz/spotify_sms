# main.py

import threading
import time
from sms_handler import init_modem, send_at_command, delete_sms, send_sms_response
from spotify_controller import search_and_play, is_track_playing, skip_current_track
from queue import Queue

song_queue = Queue()
current_song_playing = False

def check_for_new_sms():
    global current_song_playing
    while True:
        messages = send_at_command('AT+CMGL="ALL"')
        for i, msg in enumerate(messages):
            try:
                decoded_msg = msg.decode('utf-8', 'ignore').strip()
                if '+CMGL' in decoded_msg:
                    parts = decoded_msg.split(',')
                    if len(parts) > 1 and '"REC UNREAD"' in parts[1]:
                        index = parts[0].split(':')[1].strip()
                        sender_number = parts[2].replace('"', '')
                        sms_content = messages[i + 1].decode('utf-8', 'ignore').strip()
                        handle_sms(sms_content, sender_number)
                        delete_sms(index)
            except IndexError as e:
                print(f"IndexError in message parsing: {e}")
            except Exception as e:
                print(f"Error in check_for_new_sms: {e}")
        time.sleep(2)

def handle_sms(sms_content, sender_number):
    global current_song_playing
    if 'skip' in sms_content.lower():
        skip_current_track()
        send_sms_response("Skipping current track.", sender_number)
    elif 'remove' in sms_content.lower():
        # Placeholder for future remove functionality
        send_sms_response("Remove functionality not implemented yet.", sender_number)
    else:
        song_queue.put((sms_content, sender_number))
        send_sms_response("Your request is added to the queue.", sender_number)

def play_music_from_queue():
    global current_song_playing
    while True:
        if not current_song_playing and not song_queue.empty():
            song_request, _ = song_queue.get()
            search_and_play(song_request)
            current_song_playing = True
        elif current_song_playing and not is_track_playing():
            current_song_playing = False
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
