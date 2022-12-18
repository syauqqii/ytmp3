# This program using API from website : api.akuari.my.id
# hehe :D thank you to author api page

from requests import get
from os import system
from json import loads
from argparse import ArgumentParser

if __name__ == "__main__":
	try:
		parser = ArgumentParser(description='YT to MP3')

		parser.add_argument('-U', '--url', dest='url', type=str, help='masukin url yt lah')

		args 	= parser.parse_args()
		
		if args.url is None:
			print("\n > Contoh penggunaan: ytmp3.py --url https://www.youtube.com/watch?v=M1YBy0F5y8c")
			exit(0)

		print("\n > Starting program!")
		url = args.url
		finalURL = f"https://api.akuari.my.id/downloader/youtube3?link={url}&type=360"
		print(" > Fromating URL success!")
		print(" > Process request to API!")
		request = get(finalURL).text
		print(" > Request to API success!")
		resultJSON = loads(request)
		print(" > Reading response from API success!")
		print(" > Process request to downloading file!")
		res = get(resultJSON['audio']['audio'])
		print(" > Download file success!")
		print(" > Preparing to write file into ur pc!")
		with open(f"{resultJSON['title']}.mp3", "wb") as file:
			file.write(res.content)
		print(" > Success to add file into ur PC!")
		print(f"\n > File : '{resultJSON['title']}.mp3', Size : '{resultJSON['audio']['audio']['size']}'")
	except KeyboardInterrupt:
		exit(0)
