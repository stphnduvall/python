import youtube_dl
from youtube import youtube_search

# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#   ydl.download(['http://www.youtube.com/watch?v=XxGmgmelZV0'])

# This is for error catching
class ErrorLog(object):
  def debug(self, msg):
    pass

  def warning(self, msg):
    pass

  def error(self, msg):
    print(msg)

def my_hook(d):
  if d['status'] == 'finished':
    print('Done downloading, now converting ...')

ydl_opts = {
  'format': 'bestaudio/best',
  'outtmpl': 'music-cache/%(id)s.%(ext)s',
  'postprocessors': [{
  'key': 'FFmpegExtractAudio',
  'preferredcodec': 'mp3',
  'preferredquality': '192',
  }],
  'logger': ErrorLog(),
  'progress_hooks': [my_hook],
}

# This is the bit that gets a video and downloads it
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
  ydl.download(['http://youtube.com/watch?v=UHpeu9j_y4w'])