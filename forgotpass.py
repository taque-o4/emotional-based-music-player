from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.title('Emotion Based Music Player')

height = 563
width = 500
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="#fff")  

def sign_in():
    
    # Creating connection to database 
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root!@#123",
    database="users_database"
    )
    
    username = username_entry.get()
    password = password_entry.get()
    reppass = repPassword_entry.get()
    
    if username == '' or password == '' or reppass == '':
        messagebox.showerror("Error","Please fill all the fields!")
    else:
        # Execute a SELECT query to check if the user exists
        cursor = conn.cursor()
        sql = "SELECT * FROM users WHERE username = %s"
        values = (username,)
        cursor.execute(sql, values)
        result = cursor.fetchone()

        # Return True if the user exists
        if result:
            
            if password != reppass:
                messagebox.showerror('Emotion Based Music Player', 'Password do not match')
            else:
                if (len(password) < 8):
                    messagebox.showerror('Emotion Based Music Player', 'Password cannot be less than 8 characters!')
                else:
                    cursor = conn.cursor()
                    query = "UPDATE users SET password = %s WHERE username = %s"
                    values = (password, username)
                    cursor.execute(query, values)
                    conn.commit()

                    # Check if the query affected any rows
                    if query:
                        messagebox.showinfo('Emotion Based Music Player', 'Password successfully reseted')
                        window.destroy()
                        import sign_in
                    else:
                        messagebox.showerror('Emotion Based Music Player', 'Something went wrong')
        else:
            messagebox.showerror('Emotion Based Music Player', 'User NOT found')

# ================Background Image ====================
backgroundImage = PhotoImage(file="assets\\forgot.png")
bg_image = Label(
    window,
    image=backgroundImage,
    bg="#fff"
)
bg_image.place(x=0, y=0)

# Form Entries
username_entry = Entry(
    window,
    bd=0,
    bg="#EFEFEF",
    highlightthickness=0,
    font=("Segoe UI Regular", 12 * -1),
)
username_entry.place(x=100, y=153, width=280, height=27)

password_entry = Entry(
    window,
    bd=0,
    bg="#EFEFEF",
    highlightthickness=0,
    font=("Segoe UI Regular", 12 * -1),
    show='*'
)
password_entry.place(x=100, y=213, width=280, height=27)

repPassword_entry = Entry(
    window,
    bd=0,
    bg="#EFEFEF",
    highlightthickness=0,
    font=("Segoe UI Regular", 12 * -1),
    show='*'
)
repPassword_entry.place(x=100, y=270, width=280, height=27)

# Sign Up Button
signin=Button(
    window,text='Reset',
    font=('Open Sans',16,'bold'),
    fg='white',
    bg='#7D90F7',
    activeforeground='white',
    activebackground="#7D90F7",
    cursor='hand2',
    bd=0,width=22,
    command=sign_in
)
signin.place(x=105, y=352, width=280, height=27)



window.resizable(False, False)
window.mainloop()