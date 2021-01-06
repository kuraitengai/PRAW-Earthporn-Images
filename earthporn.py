# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:01:33 2019

@author: test
"""

import praw
import requests
import re
import pandas as pd

download_folder = 'C:/Users/LAPTOP/Pictures/Reddit/'

r = praw.Reddit(client_id='CLIENT_ID',
                client_secret='CLIENT_SECRET',
                user_agent='USERAGENT')

#print(r.read_only)

def checkDimensions(dimensions):
    width = int(dimensions.split('x')[0].strip())
    height = int(dimensions.split('x')[1].strip())
    if (width > 2000 and width / height > 1.1 and width / height < 1.7):
        return True

def parseAspectRatio(title):
    # Only match images with large dimensions
    regex = re.search(r'\d{4}x\d{4}', title)
    if (regex is not None):
        dimensions = regex.group(0)
        if (checkDimensions(dimensions)):
            return True
    else:
        return False

def downloadImages(urls):
    for url in urls:
        filename = url.split('/')[-1]
        req = requests.get(url, stream=True)
        with open(r'C:\Users\LAPTOP\Pictures\Reddit\''+filename, 'wb') as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    return

urls = []
titles = []
filenames = []

subreddit = r.subreddit('EarthPorn')
posts = subreddit.new(limit=100)
for post in posts:
    url = (post.url)
    title = (post.title)
    filename = url.split('/')[-1]
    if (parseAspectRatio(title)):
#        print(title,url)
        urls.append(url)
        titles.append(title)
        filenames.append(filename)

downloadImages(urls)

#print(urls)
#print(titles)
#print(filenames)

details = pd.DataFrame({'title': titles,
                        'filename': filenames,
                        'url': urls})

print(details.info())
print(details)
