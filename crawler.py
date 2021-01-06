# source for skeleton: https://stackoverflow.com/questions/18408307/how-to-extract-and-download-all-images-from-a-website-using-beautifulsoup
# Used to crawl the images from wikipedia

import re
import requests
from bs4 import BeautifulSoup


site = 'https://commons.wikimedia.org'
subpage = "/wiki/Audi"
response = requests.get(site + subpage)
folder = "audi"


soup = BeautifulSoup(response.text, 'html.parser')
# get all urls that point to image pages
urls = soup.findAll("a", {"class": "image"})
for url in urls:
    response = requests.get(site + url["href"])
    soup = BeautifulSoup(response.text, 'html.parser')

    # get all urls that point to the actual immages
    img_tags = soup.find_all('a', {"class": "mw-thumbnail-link"})

    # get the links in string format
    urls = [img['href'] for img in img_tags]

    # filter for 800px version of the image (there are other resolutions available)
    urls = [url for url in urls if "800px" in url]
    for url in urls:
        # filter valid urls
        filename = re.search(r'/(http(s?):)|([/|.|\w|\s])*\.(?:jpg|gif|png|JPG|PNG|GIF)', url)
        # last "/"  in filename
        begin = url.rfind("/")
        if not filename:
            print("Regex didn't match with the url: {}".format(url))
            continue
        with open("carBrands/mercedesBenz/" + url[begin + 1:], 'wb') as f:
            print("saving: " + url)
            if 'http' not in url:
                # sometimes an image source can be relative
                # if it is provide the base url which also happens
                # to be the site variable atm.
                url = '{}{}'.format(site, url)
            response = requests.get(url)
            if response.status_code == 200:
                f.write(response.content)
            else:
                print("error downloading")
