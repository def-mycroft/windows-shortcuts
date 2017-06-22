import webbrowser
import time
import os

new = 2 # open in a new tab, if possible 

def open_filepath(filepath):
    os.startfile(filepath)
    time.sleep(0.5)

def open_url(url):
    webbrowser.open(url,new=new)
    time.sleep(0.5)