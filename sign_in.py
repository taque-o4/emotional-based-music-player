from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.title('Emotion Based Music Player')

height = 563
width = 1000
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
    
    if username == '' or password == '':
        messagebox.showerror("Error","Please fill all the fields!")
    else:
        # Execute a SELECT query to check if the user exists
        cursor = conn.cursor()
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(sql, values)
        result = cursor.fetchone()

        # Return True if the user exists
        if result:
            messagebox.showinfo('Emotion Based Music Player', 'Login successful')
            window.destroy()
            import menu
            
        else:
            messagebox.showerror('Emotion Based Music Player', 'Wrong username or password')

# ================Background Image ====================
backgroundImage = PhotoImage(file="assets\\login_bg.png")
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

# Forgot password
def forgotPass():
    
    window.destroy()
    import forgotpass
    
forgotPass = Button(
    text="Forgot password",
    fg="#206DB4",
    font=("Segoe UI Regular", 12 * -1),
    bg="#F4F5F6",
    bd=0,
    cursor="hand2",
    activebackground="#fff",
    activeforeground="#ffffff",
    command=forgotPass
)
forgotPass.place(x=190, y=265, height=20)

# Sign Up Button
signin=Button(
    window,text='Sign In',
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

# Don't have account
def switchSignup():
    window.destroy()
    import sign_up
    
switchSignup = Button(
    text="Sign Up",
    fg="#206DB4",
    font=("Segoe UI Regular", 12 * -1),
    bg="#F4F5F6",
    bd=0,
    cursor="hand2",
    activebackground="#fff",
    activeforeground="#ffffff",
    command=switchSignup
)
switchSignup.place(x=238, y=386, height=20)


window.resizable(False, False)
window.mainloop()