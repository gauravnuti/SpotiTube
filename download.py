from get_yt_link import *
import youtube_dl

def download(track):

	# PART 1: Grabbing Link from Search Results
	link = get_yt_link(track)
	print(link)

	#PART 2: Get Video Details
	r = None
	ydl = youtube_dl.YoutubeDL()
	with ydl:
		r = ydl.extract_info(link, download=False)

	#PART 3: Set Options and Download
	options = {
		'format': 'bestaudio/best',
		'extractaudio': True,
		'audioformat': "mp3",
		'outtmpl': '/download/%(title)s.mp3',
		'noplaylist': True,
	}

	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([link])