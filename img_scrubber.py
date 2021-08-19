import requests
import urllib
from urllib.request import urlretrieve
import os
import mimetypes

def getChannel():
    message = "Please enter the channel to be scrubbed.\nThis is the section of the URL after the last slash, ex:\nhttps://www.are.na/user-name/channelname\n"
    channel = input(message)
    return channel

def api(channel):
    contents = []
    new_results = True
    page = 1
    url = "http://api.are.na/v2/channels/" + channel
    # idk what i deleted here but it breaks here
    # ['length'] / ['per']
    return contents

def urlScraper(contents):
    urls = []
    for content in contents:
        urls.append(content['image']['original']['url'])
    return urls

def imgDownloader(urls, force = False):
    for i in urls:
        url = i
        position = str(urls.index(url))
        length = str(len(urls))
        destination_dir = "img"

        response = requests.get(url)
        content_type = response.headers['content-type']
        extension = mimetypes.guess_extension(content_type)

        filepath = os.path.join(destination_dir, position + extension)

        if force or not os.path.exists(filepath):
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
        
        print("Downloading file " + position + "/" + length)
        urllib.request.urlretrieve(url, filepath)

def main():
    channel = getChannel()
    contents = api(channel)
    urls = urlScraper(contents)
    imgDownloader(urls)

main()

# blocks_quant = len(contents)
# print(f"{blocks_quant} blocks found.")



# TODO figure out pagination