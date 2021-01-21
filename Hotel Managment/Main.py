from tkinter import*
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox

from pymysql import DBAPISet, cursors
from Customerlist import*
from Checkin import*
from addrooms import*
from add_customer_details import*
from roomlist import*
from checkout import*




#Connect to myql
#ENTER YOUR USER NAME AND PASSWORD TO CONNECT TO DATABASE
con = pymysql.connect(host="localhost",user="USERNAME",password="PASSWORD")
cur =con.cursor()
mycursor = con.cursor()
#creating a database if not exist;
cursor = con.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Hotel__man")
#connecting to databse
cursor = con.cursor()
cursor.execute("USE Hotel__man")
#Creating tables
mycursor.execute("CREATE TABLE cust (FNAME VARCHAR(20) PRIMARY KEY NOT NULL, LNAME VARCHAR(20) NOT NULL, PHNO int NOT NULL)")
mycursor.execute("CREATE TABLE issued_rooms (RoomNo int AUTO_INCREMENT PRIMARY KEY NOT NULL, issuedto VARCHAR(30) NOT NULL, status VARCHAR(30) NOT NULL)")
mycursor.execute("CREATE TABLE rooms (RoomNo int AUTO_INCREMENT PRIMARY KEY NOT NULL, RoomType VARCHAR(30) NOT NULL, status VARCHAR(30) NOT NULL)")
mycursor = con.cursor()



root = Tk()
root.title("Hotel Managment")
root.minsize(width=400,height=400)
root.geometry("600x500")
same=True
n=0.25

# Adding a background image
background_image =Image.open("bg.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Shrey's Hotel", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# add customer details
btn1 = Button(root, text="Add Customer Details", bg='Black',fg='white',command =add_customer_details)
btn1.place(relx=0.28,rely=0.3,relwidth=0.45,relheight=0.1)


#Check in
btn2 = Button(root, text="Check In", bg='Black',fg='white',command=checkinn)
btn2.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)


#check out
btn3 = Button(root,text="Check Out",bg='black', fg='white',command=checkout)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

# View Customer List
btn4 = Button(root,text="View Customer List",bg='black', fg='white',command = View)
btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)


#Add Room(Connect it to rooms table)
btn5 = Button(root,text="Add Rooms",bg='black', fg='white',command = addrooms)
btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

#Room List
btn6 = Button(root,text="Room List",bg='black', fg='white',command = View_Room)
btn6.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)





root.mainloop()
