#!/bin/python3
"""
instascrape.py:
    Given a list of links to Instagram pages, attempts to download them.
"""
import requests
import shutil
from lxml import html
import os

def load_linkfile(fn = None):
    if fn is None:
        try:
            fn = [file for file in os.listdir() if file.endswith("links.txt")][0]
        except IndexError:
            raise FileNotFoundError("No link file provided.")
    with open(fn) as links_file:
        links = [_.strip() for _ in links_file.readlines()]
    return links

def extract_photo_url(link):
    # Only works for the first image in a gallery.
    # Will be deprecated once I figure out how to get all of them.
    r = requests.get(link)
    if r.status_code != 200:
        print("Request failed for {}.".format(link))
        return None
    try:
        img_ele = html.fromstring(r.content).xpath('//meta[@property="og:image"]')[0]
    except IndexError:
        print("No images found on {}.").format(link)
    img_url = img_ele.attrib['content']
    return img_url

def save_file(url, save_loc):
    response = requests.get(url, stream=True)
    response.raw.decode_content = True
    with open(save_loc, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    return

if __name__ == "__main__":
    photo_links = []
    for line in sys.stdin:
        photo_links.append(extract_photo_url(line))

        
    photo_links = []
    for link in links:
        photo_url = extract_photo_url(link)
        if photo_url is not None:
            photo_links.append(photo_url)
        else:
            print("Failed at {}.".format(photo_url))
            continue

    save_to = "gizmo_pics"
    for i, u in enumerate(photo_links):
        name = "gizmo_" + str(i).zfill(2) + ".jpg"
        save_file(u, os.path.join(save_to, name))
