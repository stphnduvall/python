#!/usr/bin/python

import httplib2
import os
import re
import sys

from googleapiclient.discovery import build
from googleapiclient.discovery import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyCfPbKO8UCQcrwmnmijkpGwh9nITP6H-8M"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
   youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
   # Call the search.list method to retrieve results matching the specified term
   search_response = youtube.search().list(
     q=options,
     part="id,snippet",
     maxResults=1
   ).execute()
   videos = []
   # Add each result to the appropriate list, then display the lists of matching videos, channels, and playlists
   for search_results in search_response.get("items", []):
     if search_results["id"]["kind"] == "youtube#video":
       videos.append(
         {'title': search_results["snippet"]["title"], 'id': search_results["id"]["videoId"]}
       )
   print(videos)


if __name__ == "__main__":
  search = 'Bro safari the drop'
  try:
    youtube_search(search)
  except HttpError as e:
    print("An HTTP error {} occured:\n{}".format(e.resp.status, e.content))