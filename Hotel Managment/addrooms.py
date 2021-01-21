from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


def addroomss():
    RoomNO = custInfo1.get()
    RoomType = custInfo2.get()
    Status = custInfo3.get()
    
    
    
    insertCust = "insert into "+roomTable+" values('"+RoomNO+"','"+RoomType+"','"+Status+"')"
    try:
        cur.execute(insertCust)
        con.commit()
        messagebox.showinfo('Sucess',"Room Added successfully")
    except:
        messagebox.showinfo("Error","Room Already Exists")
        
    print(RoomNO)
    print(RoomType)
    print(Status)




    root.destroy()
def addrooms():
    global custInfo1, custInfo2, custInfo3, custInfo4, Canvas1, con, cur, roomTable,root

    root= Tk()
    root.title("Add Rooms")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    #Connection to database
    #ENTER YOUR USER NAME AND PASSWORD TO CONNECT TO DATABASE
    con = pymysql.connect(host="localhost",user="USERNAME",password="PASSWORD",database="Hotel_man")
    cur = con.cursor()

    #table connection
    roomTable= "rooms" #customer table
    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Rooms", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    #Room Number
    lb1 = Label(labelFrame,text="Room No :",bg='black',fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    custInfo1 = Entry(labelFrame)
    custInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
    

    #Room Type
    lb2 = Label(labelFrame,text="Room Type : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    custInfo2 = Entry(labelFrame)
    custInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
    
    #Status
    lb3 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
    


    custInfo3 = Entry(labelFrame)
    custInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

   
    #Submit Button
    SubmitBtn = Button(root,text="Add Room",bg='#d1ccc0', fg='black',command=addroomss)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
