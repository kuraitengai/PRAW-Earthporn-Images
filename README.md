Using PRAW to download Reddit images
====================================

PRAW, an acronym for "Python Reddit API Wrapper", is a Python package that allows for simple access to Reddit's API.

About
-----
This script will look at the Earthport subreddit and look at the last 100 posts and look for landscape oriented images that are at least 2000 pixels wide. This is determined by stripping out the resolution from the post title.

There is also a file that will look at the location the images are saved to and delete any image that is older than 30 days. That way there is an always changing selection of backgrounds. I created a scheduled task to get new images one day each week then another task to run the cleanup file five minutes later to delete older images.

Installation
------------
PRAW is supported on Python 3.6+. The recommended way to install PRAW is via pip.

`pip install praw`

To install the latest development version of PRAW run the following instead:

`pip install --upgrade https://github.com/praw-dev/praw/archive/master.zip`

For instructions on installing Python and pip see "The Hitchhiker's Guide to Python" Installation Guides.

Quickstart
----------
Assuming you already have a credentials for a script-type OAuth application you can instantiate an instance of PRAW like so:

```python
import praw
reddit = praw.Reddit(client_id="CLIENT_ID", client_secret="CLIENT_SECRET",
                     password="PASSWORD", user_agent="USERAGENT",
                     username="USERNAME")
```

Documentation
-------------
PRAW's documentation is located at https://praw.readthedocs.io/.
