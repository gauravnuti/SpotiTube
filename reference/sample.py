import spotipy
import spotipy.oauth2 as oauth2

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


def write_tracks(text_file, tracks):
    with open(text_file, 'a') as file_out:
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
                    file_out.write(track_name + '\n')
                except KeyError:
                    print(u'Skipping track {0} by {1} (local only?)'.format(
                            track['name'], track['artists'][0]['name']))
            # 1 page = 50 results
            # check if there are more pages
            if tracks['next']:
                tracks = spotify.next(tracks)
            else:
                break


def write_playlist(username, playlist_id):
    results = spotify.user_playlist(username, playlist_id,
                                    fields='tracks,next,name')
    text_file = u'{0}.txt'.format(results['name'], ok='-_()[]{}')
    print(u'Writing {0} tracks to {1}'.format(
            results['tracks']['total'], text_file))
    tracks = results['tracks']
    write_tracks(text_file, tracks)

def get_albums():
    results = spotify.album_tracks("2yDJ5DNMFo3MnVPSwrJHhy")
    tracks = results['items']

    for track in tracks:
        print(track['artists'][0]['name'] + " - " + track['name']) 

token = generate_token()
spotify = spotipy.Spotify(auth=token)

get_albums()

# example playlist
#write_playlist('spotify', '37i9dQZF1DX4dyzvuaRJ0n')