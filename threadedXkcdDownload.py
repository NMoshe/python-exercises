# Download xkcd comics using multithreading

import os
import requests
import bs4
import threading

os.makedirs('Xkcd', exist_ok=True)


def downloadXkcd(startComic, endComic):
    for urlNum in range(startComic, endComic):
        # download the page
        print(f'Downloading page {urlNum}...')
        res = requests.get(f'https://xkcd.com/{urlNum}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find url of image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic.')
        else:
            comicUrl = comicElem[0].get('src')
            # download comic
            print(f'Downloading image{comicUrl}...')
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()

        # save image
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()


# Create thread objects
downloadThreads = []  # list of thread objects
for i in range(1, 140, 10):  # loop 14 times, create 14 threads
    start = i
    end = i + 9
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
