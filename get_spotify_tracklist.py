import spotipy
import spotipy.oauth2 as oauth2

def get_playlist(spotify, username, playlist_id):
	results = spotify.user_playlist(username, playlist_id,
									fields='tracks,next,name')
	tracks = results['tracks']

	tracklist = []
	while True:
		for item in tracks['items']:
			if 'track' in item:
				track = item['track']
			else:
				track = item
			try:
				#track_url = track['external_urls']['spotify']
				track_name = track['artists'][0]['name']+" - "+track['name']
				#file_out.write(track_url + '\n')
				#file_out.write(track_name + '\n')
				tracklist.append(track_name)
			except KeyError:
				print(u'Skipping track {0} by {1} (local only?)'.format(
						track['name'], track['artists'][0]['name']))
		# 1 page = 50 results
		# check if there are more pages
		if tracks['next']:
			tracks = spotify.next(tracks)
		else:
			break
	return tracklist

def get_album(spotify, album_id):
	tracklist = []
	results = spotify.album_tracks(album_id)
	tracks = results['items']

	for track in tracks:
		tracklist.append(track['artists'][0]['name'] + " - " + track['name'])

	return tracklist