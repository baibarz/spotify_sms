Spotify SMS Controller


Description


The Spotify SMS Controller is a Python application that allows users to control Spotify playback through SMS commands. It uses a GSM modem to receive SMS messages and the Spotify API to manage music playback.

Features
SMS Control: Users can send song requests via SMS.
Spotify Integration: Searches and plays songs from Spotify based on SMS requests.
Queue Management: Manages a queue of song requests.
Prerequisites
Python 3.x
GSM modem connected to the system
Spotify Developer Account and API credentials
Installation
1. Clone the Repository
bash
Copy code
git clone <repository-url>
cd spotify-sms-controller
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
Configuration
Update the spotify_controller.py with your Spotify Client ID, Client Secret, and Redirect URI.
Set the correct serial port in sms_handler.py for the GSM modem.
Usage
Initialize the Modem:
