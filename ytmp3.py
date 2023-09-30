# This program using API from website : api.akuari.my.id
# hehe :D thank you to author api page

from requests import get
from os import system, name
from json import loads
from argparse import ArgumentParser
from validators import url as checkLink
from re import compile

defaultColor = "\033[0m"
red = "\033[91m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"

def isYoutubeURL(url):
    ytLink = compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$')
    match = ytLink.match(url)
    return match is not None

def clearScreen():
    if name == "nt":
        system("cls")
    elif name == "posix":
        system("clear")
    else:
        return

if __name__ == "__main__":
    try:
        clearScreen()
        parser = ArgumentParser(description='YT to MP3')

        parser.add_argument('-U', '--url', dest='url', type=str, help='masukin url yt lah')

        args    = parser.parse_args()
        
        if args.url is None:
            print(f"\n {defaultColor}> {blue}Contoh penggunaan: {defaultColor}ytmp3.py {yellow}--url{defaultColor} https://{red}www.youtube.com{defaultColor}/watch?v=M1YBy0F5y8c{defaultColor}")
            exit(0)

        if not checkLink(args.url):
            print(f"\n > {red}URL {defaultColor}yang anda inputkan {red}tidak benar!{defaultColor}")
            print(f"\n {defaultColor}> {blue}Contoh penggunaan: {defaultColor}ytmp3.py {yellow}--url{defaultColor} https://{red}www.youtube.com{defaultColor}/watch?v=M1YBy0F5y8c{defaultColor}")
            exit(0)

        if not isYoutubeURL(args.url):
            print(f"\n > {red}URL {defaultColor}yang anda inputkan bukan URL {red}Youtube{defaultColor}!{defaultColor}")
            print(f"\n {defaultColor}> {blue}Contoh penggunaan: {defaultColor}ytmp3.py {yellow}--url{defaultColor} https://{red}www.youtube.com{defaultColor}/watch?v=M1YBy0F5y8c{defaultColor}")
            exit(0)

        print(f"\n > {blue}Starting program{defaultColor}!")
        url = args.url
        finalURL = f"https://api.akuari.my.id/downloader/yt1?link={url}"
        print(f" > {green}Fromating URL success{defaultColor}!")
        print(f" > {blue}Process request to API{defaultColor}!")
        request = get(finalURL).text
        print(f" > {green}Request to API success{defaultColor}!")
        resultJSON = loads(request)
        print(f" > {green}Reading response from API success{defaultColor}!")
        print(f" > {blue}Process request to downloading file{defaultColor}!")
        res = get(resultJSON['urldl_audio']['link'])
        print(f" > {green}Download file success{defaultColor}!")
        print(f" > {blue}Preparing to write file into ur pc{defaultColor}!")
        with open(f"{resultJSON['info']['title']}.mp3", "wb") as file:
            file.write(res.content)
        print(f" > {green}Success to add file into ur PC{defaultColor}!")
        print(f"\n > {yellow}File {defaultColor}: {green}'{resultJSON['info']['title']}.mp3'{defaultColor}, {yellow}Size : {green}'{resultJSON['urldl_audio']['link']['size']}'{defaultColor}")
    except KeyboardInterrupt:
        exit(0)
