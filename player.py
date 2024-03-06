from pygame import mixer
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from tkinter import filedialog
import mysql.connector

window = Tk()
window.title('Emotion Based Music Player')

height = 563
width = 500
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="#060F11")  

#add many songs to the playlist
def addsongs():
    #a list of songs is returned 
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    #loop through everyitem in the list
    for s in temp_song:
        songs_list.insert(END,s)
        
            
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
    
    
def Play():
    song=songs_list.get(ACTIVE)
    song=f'{song}'
    mixer.music.load(song)
    mixer.music.play()

#to pause the song 
def Pause():
    mixer.music.pause()

#to stop the  song 
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#to resume the song

def Resume():
    mixer.music.unpause()

#Function to navigate from the current song
def Previous():
    #to get the selected song index
    previous_one=songs_list.curselection()
    #to get the previous song index
    previous_one=previous_one[0]-1
    #to get the previous song
    temp2=songs_list.get(previous_one)
    temp2=f'{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate new song
    songs_list.activate(previous_one)
    #set the next song
    songs_list.selection_set(previous_one)

def Next():
    #to get the selected song index
    next_one=songs_list.curselection()
    #to get the next song index
    next_one=next_one[0]+1
    #to get the next song 
    temp=songs_list.get(next_one)
    temp=f'{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate newsong
    songs_list.activate(next_one)
     #set the next song
    songs_list.selection_set(next_one)
    
#initialize mixer 
mixer.init()

# ================Background Image ====================
backgroundImage = PhotoImage(file="assets\\player.png")
bg_image = Label(
    window,
    image=backgroundImage,
    bg="#060F11"
)
bg_image.place(x=0, y=0)

# Prev button
prev=Button(
    window,text='Prev',
    font=('Segoe UI',10),
    fg='#040B13',
    bg='#D7F9F2',
    activeforeground='white',
    activebackground="#D7F9F2",
    cursor='hand2',
    bd=0,width=22, command=Previous
)
prev.place(x=23, y=513, width=50, height=37)

# Pause button
pause=Button(
    window,text='Pause',
    font=('Segoe UI',10),
    fg='#040B13',
    bg='#D7F9F2',
    activeforeground='white',
    activebackground="#D7F9F2",
    cursor='hand2',
    bd=0,width=22, command=Pause
)
pause.place(x=122, y=513, width=50, height=37)

# Play button
play=Button(
    window,text='Play',
    font=('Segoe UI',10),
    fg='#040B13',
    bg='#D7F9F2',
    activeforeground='white',
    activebackground="#D7F9F2",
    cursor='hand2',
    bd=0,width=22, command=Play
)
play.place(x=193, y=513, width=50, height=37)

# Resume button
resume=Button(
    window,text='Resume',
    font=('Segoe UI',10),
    fg='#040B13',
    bg='#D7F9F2',
    activeforeground='white',
    activebackground="#D7F9F2",
    cursor='hand2',
    bd=0,width=22, command=Resume
)
resume.place(x=263, y=513, width=50, height=37)

# Stop button
stop=Button(
    window,text='Stop',
    font=('Segoe UI',10),
    fg='#040B13',
    bg='#D7F9F2',
    activeforeground='white',
    activebackground="#D7F9F2",
    cursor='hand2',
    bd=0,width=22, command=Stop
)
stop.place(x=333, y=513, width=50, height=37)

# Next button
nextbtn=Button(
    window,text='Next',
    font=('Segoe UI',10),
    fg='#040B13',
    bg='#D7F9F2',
    activeforeground='white',
    activebackground="#D7F9F2",
    cursor='hand2',
    bd=0,width=22, command=Next
)
nextbtn.place(x=430, y=513, width=50, height=37)

#create the listbox to contain songs

songs_list=Listbox(
    window,selectmode=SINGLE,
    bg="#060F11",
    fg="white",
    font=('Segoe UI',11),
    selectbackground="gray",
    selectforeground="white"
)
songs_list.grid(columnspan=9)
songs_list.place(x=80, y= 30, width=350, height=440)

#font is defined which is to be used for the button font 
defined_font = font.Font(family='Segoe UI')

#menu 
my_menu=Menu(window)
window.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)

window.resizable(False, False)
window.mainloop()