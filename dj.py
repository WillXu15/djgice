#!/usr/bin/env python
import subprocess
import glob
import os
import pygame
import time

songs = ["moSFlvxnbgk.wav"]
pygame.mixer.init(22050, -16, 2, 2048)

def get_song(url):
    print "DOWNLOADING SONG"
    subprocess.call("youtube-dl -o '%(id)s.%(ext)s' -x --audio-format mp3 " +url, shell=True)
    load_song()

def load_song():
    print "LOADING SONG"
    song = max(glob.iglob('*.mp3'), key=os.path.getctime)
    process = "ffmpeg -i "+song+" "+song[:-4]+".wav"
    print process
    subprocess.call(process, shell=True)
    songs.append(song[:-4]+".wav")

def main():
#    get_song("https://www.youtube.com/watch?v=moSFlvxnbgk")
    while True:
        pygame.mixer.music.load(songs[0])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(15)

if __name__ == "__main__": main()
