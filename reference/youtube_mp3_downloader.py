from get_yt_link import *
import youtube_dl

if __name__ == "__main__":

	# PART 1: Grabbing Link from Search Results
	query = input()
	link = get_yt_link(query)
	print(link)

	#PART 2: Get Video Details
	r = None
	ydl = youtube_dl.YoutubeDL()
	with ydl:
		r = ydl.extract_info(link, download=False)

	options = {
		'format': 'bestaudio/best',
		'extractaudio': True,
		'audioformat': "mp3",
		'outtmpl': r['title']+".mp3",
		'noplaylist': True,
	}

	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([link])