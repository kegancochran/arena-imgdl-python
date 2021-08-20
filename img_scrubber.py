import requests
import urllib
from urllib.request import urlretrieve
import os
import mimetypes

def getChannel():
    message = "Please enter the slug of the channel to be scrubbed.\nThis is the section of the URL after the last slash, ex:\nhttps://www.are.na/user-name/slug\n"
    channel = input(message)
    return channel

def getUrls(channel):
    contents = []
    urls = []
    page = 1
    url = "http://api.are.na/v2/channels/" + channel
    new_contents = True
    print('Fetching channel data...')

    while new_contents:
        print('PAGE ' + str(page) + '...')
        response = requests.get(url + "?page=" + str(page)).json()
        new_contents = response['contents']
        contents.append(new_contents)
        for block in new_contents:
            urls.append(block['image']['original']['url'])
            print((block['image']['original']['url']))
        page += 1

    img_quant = str(len(urls))
    input(img_quant + ' images found. ' + 'Press enter to download. ')
    return urls

def imgDL(urls, force = False):
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
    urls = getUrls(channel)
    imgDL(urls)

main()