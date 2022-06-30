import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()


root=Tk()
root.title('Kartikey Singh Rajawat Music player')
mixer.init()

songstatus=StringVar()
songstatus.set("choosing")


#playlist---------------
playlist=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial black',15),width=43)
playlist.grid(columnspan=5)
os.chdir(r'C:\Users\HP\Downloads\music-player-python-code\songs')
songs=os.listdir()
for s in songs:

    playlist.insert(END,s)

playbtn=Button(root,text="PLAY",command=playsong)
playbtn.config(font=('arial black',20),bg="purple",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="PAUSE",command=pausesong)
pausebtn.config(font=('arial black',20),bg="red",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="STOP",command=stopsong)
stopbtn.config(font=('arial black',20),bg="green",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="RESUME",command=resumesong)
Resumebtn.config(font=('arial black',20),bg="black",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()
