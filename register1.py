import tkinter as tk 
import mysql.connector 
from tkinter import *
import PIL 
from subprocess import call
#import _mysql
import sys

def mainpogo():
	call(["python", "mainlyguest.py"]) 

def submitact(): 
	gid = 108
	guser = Username.get() 
	gmob = Mobile.get() 
	gaddr = address.get()
	gpass = passcode.get()
	gmail = mail.get()
	# print(f"The name entered by you is {user} {passw} {addr}") 
	logintodb(gid,guser, gmob,gaddr,gpass,gmail) 


def logintodb(gid,guser,gmob,gaddr,gpass,gmail):

	try:
		conn = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="pass",
			database="force"
			) 
		mycursor = conn.cursor()
		query = "insert into register(id,username,mobile,address,passcode,gmail) values(%s,%s,%s,%s,%s,%s)"
		values = (gid,guser,gmob,gaddr,gpass,gmail)
		mycursor.execute(query,values)
		conn.commit()
		print("inserted data")

	except mysql.connector.Error as err :
		print(err)
		print("error code",err.errno)
		print("error occured",err.sqlstate)
		print("Message",err.mesg)	

	mycursor.close()
	conn.close()	
	
	

root = tk.Tk() 
root.geometry("600x600")
root.title("Registration") 
font11 = "-family {Segoe UI} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
# root.configure(background="#ffffff")
# root.configure(highlightbackground="#ffffff")
# root.configure(highlightcolor="black")
var = StringVar()
msg = Message(root,text="Hotel Blues Registration")
msg.configure(font=font11)
msg.pack()
C = Canvas(root, bg ="blue", height = 250, width = 300) 

#just name
# Frame1 = Frame(root)
# Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
# Frame1.configure(highlightcolor="black")
# Frame1.configure(width=995)
# Definging the first row 
lblfrstrow = tk.Label(root, text ="NAME :" ) 
lblfrstrow.place(x = 50, y = 120) 

Username = tk.Entry(root, width = 35) 
Username.place(x = 150, y = 120, width = 100) 

lblsecrow = tk.Label(root, text ="MOBILE NO :") 
lblsecrow.place(x = 50, y = 150) 

Mobile = tk.Entry(root, width = 35) 
Mobile.place(x = 150, y = 150, width = 100) 

lblthirow = tk.Label(root, text ="ADDRESS :") 
lblthirow.place(x = 50, y = 180) 

address = tk.Entry(root, width = 35) 
address.place(x = 150, y = 180, width = 100) 
#email
lblfifrow = tk.Label(root, text ="EMAIL ID :") 
lblfifrow.place(x = 50, y = 210) 

mail = tk.Entry(root, width = 35) 
mail.place(x = 150, y = 210, width = 100) 
#password block for log in
lblfourow = tk.Label(root, text ="PASSWORD :") 
lblfourow.place(x = 50, y = 240) 

passcode = tk.Entry(root, width = 35) 
passcode.place(x = 150, y = 240, width = 100) 
#fact that is tip
Message6 = Message()
Message6.place(relx=0.03, rely=0.45, relheight=0.04, relwidth=0.92)
Message6.configure(background="#d9d9d9")
Message6.configure(foreground="#000000")
Message6.configure(highlightbackground="#d9d9d9")
Message6.configure(highlightcolor="black")
Message6.configure(text='''YOU MAY SKIP THE REGISTRATION FOR NOW AND DIRECTLY PROCEED.''')
Message6.configure(width=791) 

submitbtn = tk.Button(root, text ="SAVE", 
					bg ='blue', command = submitact) 
submitbtn.place(x = 150, y = 300, width = 55)
#have to put if block to ensure log in is done
mainpage = tk.Button(root, text ="PROCEED", 
					bg ='blue', command = mainpogo) 
mainpage.place(x = 230, y = 300, width = 75) 

root.mainloop() 
