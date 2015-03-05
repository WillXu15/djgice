#!/usr/bin/env python
import subprocess
import glob
import os
import pygame
import time
from sys import argv
from rsongs import request_song

songs = []
pygame.mixer.init(22050, -16, 2, 2048)

def get_frozen():
    if "moSFlvxnbgk.wav" not in glob.glob('*.wav'):
        get_song("https://www.youtube.com/watch?v=moSFlvxnbgk")
    else:
        songs.append("moSFlvxnbgk.wav")

def get_song(url):
    print "DOWNLOADING SONG"
    subprocess.call("youtube-dl -o '%(id)s.%(ext)s' -x --audio-format mp3 " +url, shell=True)
    load_song()

def load_song():
    print "LOADING SONG"
    song = max(glob.iglob('*.mp3'), key=os.path.getctime)
    process = "ffmpeg -i "+song+" "+song[:-4]+".wav"
    subprocess.call(process, shell=True)
    songs.append(song[:-4]+".wav")

def main():
    while True:
        if len(songs) == 0:
            get_frozen()
        else:
            pygame.mixer.music.load(songs.pop())
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                song = request_song()
                if song is not None:
                    get_song(song)

if __name__ == "__main__": main()
