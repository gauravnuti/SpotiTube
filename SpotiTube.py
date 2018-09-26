import sys
import spotipy
import spotipy.oauth2 as oauth2
from get_spotify_tracklist import *
from get_yt_link import *
from download import *

# Spotify Playlists: URI has User and Playlist ID
# spotify:user:spotify:playlist:37i9dQZF1DX4dyzvuaRJ0n

# Spotify Albums:
# spotify:album:2yDJ5DNMFo3MnVPSwrJHhy 

def generate_token():
	""" Generate the token. Please respect these credentials :) """
	credentials = oauth2.SpotifyClientCredentials(
		client_id='37373b59fc3442f88b4880d7bcaff6ea',
		client_secret='2edca93ea10e41c8b7601d693acad192')
	token = credentials.get_access_token()
	return token

token = generate_token();
spotify = spotipy.Spotify(auth=token)

#print(get_album(spotify, "2yDJ5DNMFo3MnVPSwrJHhy"))
#print()
#print(get_playlist(spotify, 'spotify', '37i9dQZF1DX4dyzvuaRJ0n'))

uri = input("Enter URI: ")
uri = uri.split(":")
tracklist = []

try:
	if uri[1]=="user":
		print("\n"+"||||||||||||||||||||||||||||||||||||||")
		print("Playlist Details: ")
		print("User: " + uri[2])
		print("Playlist ID: " + uri[4])
		tracklist = get_playlist(spotify, uri[2], uri[4])
	elif uri[1]=="album":
		print("\n"+"||||||||||||||||||||||||||||||||||||||")
		print("Album Details: ")
		print("Album ID: " + uri[2])
		tracklist = get_album(spotify, uri[2])
except:
	print("Invalid URI!")
	sys.exit(0)

print("\n"+"||||||||||||||||||||||||||||||||||||||")
print("T R A C K L I S T")
for song in tracklist:
	print(song)

print("\n"+"||||||||||||||||||||||||||||||||||||||")
ch = input("Download All Songs (y/n): ")
if ch=='n' or ch=='N':
	sys.exit(0)

for song in tracklist:
	download(song)