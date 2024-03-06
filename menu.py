from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
import os
import customtkinter
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk


window = Tk()
window.title('Emotion Based Music Player')

height = 563
width = 1000
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="#040B13")  
# Load the image
image = Image.open("assets\\menu.png")
photo = ImageTk.PhotoImage(image)

# Create a label with the image
label = ctk.CTkLabel(window, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)

def select_files():
    file_paths = filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    for file_path in file_paths:
        add_file_to_database(file_path)

def add_file_to_database(file_path):
    # Creating connection to database 
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root!@#123",
        database="users_database"
    )
    # Extract the file information from the file path
    file_name = file_path.split("/")[-1]
    title = file_name.split(".")[0]
    cat = category_entry.get()

    # Execute an INSERT query to add the file information to the database
    cursor = conn.cursor()
    query = "INSERT INTO music_files (title, file_path, category) VALUES (%s, %s, %s)"
    values = (title, file_path, cat)
    cursor.execute(query, values)
    conn.commit()

    if query:
        messagebox.showinfo("Success!", f"{title} has been added successfully!")
    else:
        messagebox.showerror("Error", "Something went wrong, please try again!")

# ================Background Image ====================
# backgroundImage = PhotoImage(file="assets\\menu.png")
# bg_image = Label(
#     window,
#     image=backgroundImage,
#     bg="#040B13"
# )
# bg_image.place(x=0, y=0)

# Start Button
def startcam():
    import main
    
    
start=Button(
    window,text='Start Cam',
    font=('Segoe UI',12),
    fg='#040B13',
    bg='#D7F9F2',
    activeforeground='white',
    activebackground="#D7F9F2",
    cursor='hand2',
    bd=0,width=22, command=startcam
)
start.place(x=30, y=99, width=115, height=37)

# Category entry

category_entry=customtkinter.CTkEntry(master=window, width=220, placeholder_text='Enter song category')
category_entry.place(x=20, y=400)

# Add music Button
addbtn=Button(
    window,text='Add Songs',
    font=('Segoe UI',12),
    fg='#040B13',
    bg='#D7F9F2',
    activeforeground='white',
    activebackground="#D7F9F2",
    cursor='hand2',
    bd=0,width=22, command=select_files
)
addbtn.place(x=30, y=170, width=115, height=37)

def view_music():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root!@#123",
        database="users_database"
    )
    # Execute a SELECT query to check if the user exists
    cursor = conn.cursor()
    sql = "SELECT id, title, category FROM music_files"
    cursor.execute(sql)
    rows = cursor.fetchall()
    treeview.delete(*treeview.get_children())
#     # Iterate over the retrieved rows and insert them into the Listbox
    for row in rows:
#        # Loop thru the records and add them in the Treeview
        treeview.insert('', 'end', values=row)
# View Button
view=Button(
    window,text='View',
    font=('Segoe UI',12),
    fg='#040B13',
    bg='#D7F9F2',
    activeforeground='white',
    activebackground="#D7F9F2",
    cursor='hand2',
    bd=0,width=22, command=view_music
)
view.place(x=30, y=235, width=115, height=37)

def delete_row():
    # Bind select event to treeview
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root!@#123",
        database="users_database"
    )
    
    selected_item = treeview.selection()[0]
    id = treeview.item(selected_item)['values'][0]
    # Execute a SELECT query to check if the user exists
    cursor = conn.cursor()
    cursor.execute("DELETE FROM music_files WHERE id=%s", (id,))
    conn.commit()
    
    # Delete row from treeview
    treeview.delete(selected_item)
    
    messagebox.showinfo("Success", "Song successfully deleted!")

# Delete Button
delete=Button(
    window,text='Delete',
    font=('Segoe UI',12),
    fg='#040B13',
    bg='#D7F9F2',
    activeforeground='white',
    activebackground="#D7F9F2",
    cursor='hand2',
    bd=0,width=22, command=delete_row
)
delete.place(x=30, y=305, width=115, height=37)

# Exit Button
def exitbtn():
    window.destroy()
    import sign_in

exitbtn=Button(
    window,text='Sign out',
    font=('Segoe UI',12),
    fg='#040B13',
    bg='#D7F9F2',
    activeforeground='white',
    activebackground="#D7F9F2",
    cursor='hand2',
    bd=0,width=22,
    command=exitbtn
)
exitbtn.place(x=30, y=505, width=115, height=37)

    
# Create a Tkinter Listbox to display the data
# listbox = Listbox(
# window,
# selectmode=SINGLE,
# bg="#060F11",
# fg="white",
# font=('Segoe UI',11),
# selectbackground="gray",
# selectforeground="white"
# )
# listbox.place(x=300, y=45, width=670, height=480)

# Create a Treeview widget
treeview = ttk.Treeview(window)
# Define our columns
treeview['columns'] = ('ID','Title', 'Category')

# Pack the Treeview widget into the window
treeview.pack()
treeview.place(x=300, y=40, width=670, height=470)




window.resizable(False, False)
window.mainloop()