# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:01:33 2019

@author: test
"""

import praw
from PIL import Image
from io import BytesIO
import requests
import os

download_folder = 'C:/Users/LAPTOP/Pictures/Reddit/'

r = praw.Reddit(client_id='CLIENT_ID',
                client_secret='CLIENT_SECRET',
                user_agent='USERAGENT')

subreddit_name = 'earthporn'

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

def get_percentages(ls_ct, non_ls_ct):
    total_count = ls_ct + non_ls_ct
    ls_pct = (ls_ct / total_count) * 100
    non_ls_pct = (non_ls_ct / total_count) * 100
    return ls_pct, non_ls_pct

def get_images(subreddit_name):
    ls_ct = 0
    non_ls_ct = 0
    
    for submission in r.subreddit(subreddit_name).new(limit=100):
        if submission.url.endswith(('jpg', 'jpeg', 'png', 'gif')):
            response = requests.get(submission.url)
            image = Image.open(BytesIO(response.content))
            
            width, height = image.size
            if (width > height and width > 2000 and width / height > 1.1 and width / height < 1.7):
                image_path = os.path.join(download_folder,submission.id + '.jpg')
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                    print(submission.id, width, height, '{}x{}'.format(width,height))
                ls_ct += 1
            else:
                print(submission.id, width, height, '{}x{}, Not a landscape image'.format(width,height))
                non_ls_ct += 1
        else:
            print('No matching images')
    
    ls_pct, non_ls_pct = get_percentages(ls_ct, non_ls_ct)
    
    print('Landscape images:', ls_ct, '({:.2f}%)'.format(ls_pct))
    print('Non-landscape images:', non_ls_ct, '({:.2f}%)'.format(non_ls_pct))

get_images(subreddit_name)
