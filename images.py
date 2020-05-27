from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

# Search images put search results in new directory

def start_search():
    search = input("Search for:")
    params = {"q": search}
    r = requests.get("http://www.bing.com/images/search", params=params)
    dir_name = search.replace(" ", "_").lower()

    # If directory name not a directory, make one
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    # New request for each items url, get file in format we can read
    for item in links:
        # Avoid error causing to not run
        try:
            img_obj = requests.get(item.attrs["href"])
            print("Getting:", item.attrs["href"])
            # Use last part of url as title, split at the / and take last index
            title = item.attrs["href"].split("/")[-1]
            # Open image and save image
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./" + dir_name + "/" + title, img.format)
            except:
                print("Could not save image")
        except:
            print("Could not request image")

    start_search()

start_search()

