"""
A scipt for downloading videos or audio using Youtube-dl from a chrome bookmark file
with all unwanted bookmarks and header tags removed with grep
(it's probably porn)

Author: Me
Version: 2.0
Date: 8sep2019
"""

from __future__ import unicode_literals
import youtube_dl, os, pygrep, sys, datetime, platform, ffmpeg
from countdowntimer import *

#For use with pyinstaller
#Requires sys and os Libraries
def resource_path(relative_path):
# Get absolute path to resource, works for dev and for PyInstaller
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#os.chdir(os.path.dirname(__file__)) # for my own use
#print(os.getcwd())
# set to 0 for normal operation. 1 for test settings -> downloads a prebookmarked youtube link, then closes program.  Also checks existence of file structure for more questionable downloads (porn)
test = 0

pornpath = "\WHAT\FLASH\\" + str(datetime.datetime.now().year)
path = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome\User Data\Default\Bookmarks"


def exitProg():
    print("Closing in:")
    countdown(5)
    print("Goodbye")
    sys.exit()
    
def checkLinks(links):    
    if links == []:
        print("no links found for grep phrase")
        return False
    else:
        return True
    
def testing():
    links = [line.rstrip('\n') for line in pygrep.pygrep("youtube", path, 0)]
    if checkLinks(links) == True:
        downloadBookmarks(links, setOpts(""))
    else:
        exitProg()
        
def downloadBookmarks(links, ydl_opts):    
    count = 1
    for n in links:
        url = n.split('\"')[3]
        print("\ndownloading video " + str(count) + " of " + str(len(links)))
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            count += 1
            try:
                ydl.download([url])
            except:
                continue
            
# sets download options for youtube_dl.YoutubeDL object            
def setOpts(tog):
    foldername = "Downloaded with DownloadLinks"
    if tog == 'c':
        opts = {'listformats': True}
    elif tog == 'v':
        print("best or worst video quality?")
        tog = input()
        if tog == 'best':
            opts = {
            'format': 'best',
            'outtmpl': './' + foldername + '/%(title)s.%(ext)s'}
        else:
            opts = {
            'format': 'worst',
            'outtmpl': './' + foldername + '/%(title)s.%(ext)s'}
    elif tog == 'a':
        opts = {
        'format': 'best',
#           Uncomment to keep source video file
#            'keepvideo': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
        'outtmpl': './' + foldername + '/%(title)s.%(ext)s'}
    elif tog == "":  #the porn part. only works for my computer
        print("Drive Location?")
        loc = input()
        loc = loc + ":"
        if os.path.isdir(loc):
            fullpath = loc + pornpath
            print(loc + " Drive found")
            if os.path.isdir(fullpath):
                print(fullpath + " Directory found")
                os.chdir(fullpath)
            else:
                print("Directory " + fullpath + " not found. Creating")
                os.makedirs(fullpath)
                os.chdir(fullpath)
            if test == 0:
                opts = {'format': 'worst',
                'outtmpl': fullpath + '\\%(title)s.%(ext)s'}
            else:
    #           For Testing
                opts = {'listformats': True}
        else:
            print(loc + " Drive not found")
            if test == 0:
                exitProg()
    else:
        print("command not found")
        exitProg()
    return opts

def download():
    if test == 0:
        print("\nYoutube video and audio downloader v2.0")
        print("created by Tom Doratt, using ffmpeg [https://www.ffmpeg.org/] and youtube-dl [https://youtube-dl.org/]\n")
        print("Phrase to grep for?")
        phrase= input()
        print("Checking bookmarks at " + path)
        links = [line.rstrip('\n') for line in pygrep.pygrep(phrase, path, 0)]
        if checkLinks(links) == True:
            print("Video, Audio, or Check format? (v, a, or c)")
            tog = input()
            downloadBookmarks(links, setOpts(tog))
        else:
            exitProg()
    else:
        testing()

download()
exitProg()
