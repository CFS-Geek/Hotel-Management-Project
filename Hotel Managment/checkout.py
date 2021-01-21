from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

#ENTER YOUR USER NAME AND PASSWORD TO CONNECT TO DATABASE
con = pymysql.connect(host="localhost",user="USERNAME",password="PASSWORD",database="hotel_man")
cur = con.cursor()

# Enter Table Names here
roomTable = "rooms" # to check the room details
issueTable = "issued_rooms" #to add is room is issued


allRoomNo = [] #List To store all Book IDs

def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    RoomNo = bookInfo1.get()

    extractRoomNo = "select RoomNo from "+issueTable
    try:
        cur.execute(extractRoomNo)
        con.commit()
        for i in cur:
            allRoomNo.append(i[0])
        
        if RoomNo in allRoomNo:
            checkAvail = "select status from "+roomTable+" where RoomNo = '"+RoomNo+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Room Number not present")
    except:
        messagebox.showinfo("Error","Can't fetch Room Number's")
    
    
    issueSql = "delete from "+issueTable+" where RoomNo = '"+RoomNo+"'"
  
    print(RoomNo in allRoomNo)
    updateStatus = "update "+roomTable+" set status = 'avail' where RoomNo = '"+RoomNo+"'"
    try:
        if RoomNo in allRoomNo and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Checked Out  Successfully")
        else:
            allRoomNo.clear()
            messagebox.showinfo('Message',"Please check the Room No")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allRoomNo.clear()
    root.destroy()
    
def checkout(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Check Out")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Check Out", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Room No : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()