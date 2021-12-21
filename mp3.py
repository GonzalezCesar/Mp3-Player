from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
# from pygame.mixer import pause

root = Tk()
root.title('MusicPlayer')
root.iconbitmap('C:/Users/MILAGROS/Desktop/fulfilled projects/Mp3 music player/descarga.ico')
root.geometry("500x400")

pygame.mixer.init()

def play_time():
    if stopped:
        return 
    current_time = pygame.mixer.music.get_pos() / 1000
    
    #slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}')

    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    #current_song = song_box.curselection()
    
    song = song_box.get(ACTIVE)
    song = f'C:/Users/MILAGROS/Desktop/fulfilled projects/Mp3 music player/audio/{song}.mp3'
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    current_time +=1
    
    if int(my_slider.get()) == int(song_length):
        status_bar.config(text=f'Time Elapsed: {converted_song_length} ')
    elif paused:
        pass
    elif int(my_slider.get()) == int(current_time):
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    
    else:
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))
        
        converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))
        
        status_bar.config(text=f'Time Elapsed: {converted_current_time} of  {converted_song_length} ')

        next_time = int(my_slider.get()) +1
        my_slider.config(value=next_time)

    #status_bar.config(text=f'Time Elapsed: {converted_current_time} of  {converted_song_length} ')
    
    
    #my_slider.config(value=int(current_time))

    status_bar.after(1000, play_time)

def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    
    song = song.replace("C:/Users/MILAGROS/Desktop/fulfilled projects/Mp3 music player/audio/", "")
    song = song.replace(".mp3", "")
    
    song_box.insert(END, song)

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

    for song in songs:
        song = song.replace("C:/Users/MILAGROS/Desktop/fulfilled projects/Mp3 music player/audio/", "")
        song = song.replace(".mp3", "")
        song_box.insert(END, song)

def play():
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = f'C:/Users/MILAGROS/Desktop/fulfilled projects/Mp3 music player/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    play_time()

    #slider_position = int(song_length)
    #my_slider.config(to=slider_position, value=0)

    #current_volume = pygame.mixer.music.get_volume()
    #slider_label.config(text=current_volume * 100)

global stopped 
stopped = False

def stop():
    status_bar.config(text='')
    my_slider.config(value=0)

    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    status_bar.config(text='')

    global stopped
    stopped = True

def next_song():
    status_bar.config(text='')
    my_slider.config(value=0)
   
    next_one = song_box.curselection()
    
    next_one = next_one[0]+1 
    
    song = song_box.get(next_one)
    song = f'C:/Users/MILAGROS/Desktop/Mp3 music player/audio/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #
    song_box.selection_clear(0, END)

    #
    song_box.activate(next_one)

    song_box.selection_set(next_one, last=None)

def previous_song():
    status_bar.config(text='')
    my_slider.config(value=0)
    
    next_one = song_box.curselection()
    
    next_one = next_one[0]-1
    
    song = song_box.get(next_one)
    
    song = f'C:/Users/MILAGROS/Desktop/Mp3 music player/audio/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)

    song_box.activate(next_one)

    song_box.selection_set(next_one, last=None)
    
def delete_song():
    stop()
    song_box.delete(ANCHOR)
    
    pygame.mixer.music.stop()

def delete_all_songs():
    stop()
    song_box.delete(0, END)

    pygame.mixer.music.stop()




global paused
paused = False

def pause(is_paused):
    global paused 
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False 
    else:
        pygame.mixer.music.pause()
        paused = True
    
def slide(x):
    #slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
    song = song_box.get(ACTIVE)
    song = f'C:/Users/MILAGROS/Desktop/Mp3 music player/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    
    #current_volume = pygame.mixer.music.get_volume()
    #slider_label.config(text=current_volume * 100)

master_frame = Frame(root)
master_frame.pack(pady=20)

song_box = Listbox(master_frame, bg="black", fg="green", width="70", selectbackground="gray", selectforeground="black")
song_box.grid(row=0, column=0)

back_btn_img = PhotoImage(file='imagebuttons/back.png')
forward_btn_img = PhotoImage(file='imagebuttons/forward.png')
play_btn_img = PhotoImage(file='imagebuttons/play.png')
pause_btn_img = PhotoImage(file='imagebuttons/pause.png')
stop_btn_img = PhotoImage(file='imagebuttons/stop.png')

controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=7.5)


back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One song to playlist", command=add_song)

add_song_menu.add_command(label="Add Many songs to playlist", command=add_many_songs)

remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Song From Playlist", command=delete_all_songs)

status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2, column=0, pady=10)

volume_slider = ttk.Scale(volume_frame, from_=1, to=0, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10)

#slider_label = Label(root, text="0")
#slider_label.pack(pady=10)

root.mainloop()