#open several search results

import requests
import sys
import webbrowser
import bs4

print('Searching...') # display text while downloading
res = requests.get('https://pypi.org/search/?q=' + '+'.join(sys.argv[1:]))
res.raise_for_status()

#get top search links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#open tab for each resultss
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)