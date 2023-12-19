import requests

song_name = "Shape of You"
artist_name = "Ed Sheeran"
access_token = 'MW-BTTou6c_I7wWo6Ux5FKzAykR-EITqJS3UsE6XvxJC1r3k2CnzhWabWXADp7zM'

headers = {'Authorization': 'Bearer ' + access_token}
response = requests.get(f"https://api.genius.com/search?q={song_name} {artist_name}", headers=headers)

print(response.json())
