import pygame
import os
from tkinter import *
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, window):
        pygame.init()
        pygame.mixer.init()
        window.geometry('320x150')
        window.title('Simple MP3 Player')
        window.resizable(0, 0)

        Load = Button(window, text='Load', width=10, font=('Times', 10), command=self.load)
        Play = Button(window, text='Play', width=10, font=('Times', 10), command=self.play)
        Pause = Button(window, text='Pause', width=10, font=('Times', 10), command=self.pause)
        Stop = Button(window, text='Stop', width=10, font=('Times', 10), command=self.stop)
        Vol = Scale(window, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, command=self.set_vol)
        Next = Button(window, text='Next', width=10, font=('Times', 10), command=self.next)
        Prev = Button(window, text='Prev', width=10, font=('Times', 10), command=self.prev)

        Vol.set(pygame.mixer.music.get_volume())

        Load.place(x=0, y=20)
        Play.place(x=110, y=20)
        Pause.place(x=220, y=20)
        Stop.place(x=110, y=60)
        Vol.place(x=220, y=60)
        Next.place(x=0, y=60)
        Prev.place(x=220, y=60)

        self.playlist = []
        self.current = 0

    def load(self):
        file_path = filedialog.askopenfilename()
        if file_path.endswith(".mp3"):
            self.playlist.append(file_path)
            print(self.playlist)

    def play(self):
        if self.playlist:  # a check if playlist is not empty
            pygame.mixer.music.load(self.playlist[self.current])
            pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def set_vol(self, v):
        volume = float(v)
        pygame.mixer.music.set_volume(volume)

    def next(self):
        if self.playlist:
            self.current += 1
            if self.current > len(self.playlist)-1:
                self.current = 0
            self.play()

    def prev(self):
        if self.playlist:
            self.current -= 1
            if self.current < 0:
                self.current = len(self.playlist)-1
            self.play()


root = Tk()
app = MusicPlayer(root)
root.mainloop()
       