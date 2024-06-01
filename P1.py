#Student Management System
from tkinter import * 
from tkinter.messagebox import * 
from tkinter.scrolledtext import * 
from pyrebase import * 
import pandas as pd 
import matplotlib.pyplot as plt 
from datetime import datetime 
import pytz
import json
import csv

IST = pytz.timezone('Asia/Kolkata')
f=("Arial",30,"bold")

firebaseConfig = {
  "apiKey": "AIzaSyDs5uNEz3kR_ZAAl2EeXSiOD5iYXfQJZA4",
  "authDomain": "dipen-9c73d.firebaseapp.com",
  "databaseURL": "https://dipen-9c73d-default-rtdb.firebaseio.com",
  "projectId": "dipen-9c73d",
  "storageBucket": "dipen-9c73d.appspot.com",
  "messagingSenderId": "945407953765",
  "appId": "1:945407953765:web:3f999ba24434b87468ef8c"
};
 
fb =(pyrebase.initialize_app(firebaseConfig))
db = fb.database()

def f1():
	mw.withdraw() 
	aw.deiconify()
def f2(): 
	mw.withdraw()
	dw.deiconify()
def f3(): 
	mw.withdraw()
	vw.deiconify()
	vw_st_view.delete(1.0,END)
	data=db.child("Employee12").get()
	info=""
	if(data.pyres is not None):
		for d in data:
			info = info + str(d.val()) + "\n"
		vw_st_view.insert(INSERT,info)
	else: 
		showerror("Issue","No Data Found")
    
def f4(): 
	mw.withdraw()
	uw.deiconify()
def f5(): 
	mw.withdraw()
	cw.deiconify()
def f6(): 
	aw.withdraw() 
	mw.deiconify() 
def f7(): 
	dw.withdraw() 
	mw.deiconify() 
def f8():
	vw.withdraw() 
	mw.deiconify() 
def f9():
	uw.withdraw() 
	mw.deiconify() 
def f10(): 
	cw.withdraw() 
	mw.deiconify() 

def f11(): 
	try:
		id = aw_ent_id.get()
		if len(aw_ent_id.get())<=1:
			showerror("Issue","ID can not be left empty or it can not Contain a Single Digit")
		else:
			id = int(id)
			data = db.child("Employee12").get() 
			if id<=0:
				showerror("Issue","ID can not be negative or it can not be zero")
			else:
				if(data.pyres is not None) and (str(id) in data.val()):
					showerror("Issue","ID Already Exists") 
				else: 
					name=aw_ent_name.get()
					if len(aw_ent_name.get()) <= 1:
						showerror("Issue","Name can not be left empty or It can not contain a single Alphabet")
					else:
						if aw_ent_name.get().isalpha():
							salary=aw_ent_salary.get()
							if len(aw_ent_salary.get()) == 0:
								showerror("Issue","Salary can not be left empty")
							else:
								salary = int(salary)
								if salary<0:
									showerror("Issue","Salary can not be negative") 
								else:
									if salary<8000:
										showerror("Issue","Salary Should be Minimum 8K")
									else:
										info = {"id":id , "name":name , "salary":salary}
										db.child("Employee12").child(id).set(info)
										showinfo("Sucess","Employee Created")
						else:
							showerror("Issue","Name can not be an Number or special Characters")
	except ValueError: 
		showerror("Issue","ID or Salary should be an integer")	
	aw_ent_name.delete(0,END)
	aw_ent_id.delete(0,END) 
	aw_ent_salary.delete(0,END)
	aw_ent_id.focus()

def f12():
	try: 
		id = dw_ent_id.get()
		if len(dw_ent_id.get())<=1:
			showerror("Issue","ID can not be left Empty or it can not Contain A Single Digit")
		else:
			id=int(id)
			data = db.child("Employee12").get() 
			if id<=0: 
				showerror("Issue","ID can not be Negative or zero")
			else:
				if(data.pyres is not None) and (str(id) in data.val()):
					db.child("Employee12").child(id).remove()
					showinfo("Success","ID Deleted") 
				else:
					showerror("Issue","ID Does Not Exists")
	except ValueError:
		showerror("Issue","ID Should be an integer")
	dw_ent_id.delete(0,END)
	dw_ent_id.focus()

def f13(): 
	try:
		id=uw_ent_id.get()
		name=uw_ent_name.get()
		data = db.child("Employee12").get()
		if uw_ent_id.get().isalpha(): 
			showerror("Issue","ID can not be a Alphabet")
		else:
			id=int(id)
			if id<=0:
				showerror("Issue","ID can not be negative or it can not be zero")
			else:
				id=int(id)
				if len(uw_ent_name.get()) <= 1:
					showerror("Issue","Name Can not be left empty or it can not contain a single Alphabet")
				else:
					if uw_ent_name.get().isalpha():
						if(data.pyres is not None) and (str(id) in data.val()):
							try:
								newsalary=uw_ent_salary.get()
								if len(uw_ent_salary.get()) == 0:
									showerror("Issue","Salary can not be left empty") 
								else:
									newsalary=int(newsalary)
									if newsalary<0: 
										showerror("Issue","Salary can not be negative")
									else:
										if newsalary<8000:
											showerror("Issue","Salary Should be Minimum 8K")
										else:
											info = {"id":id , "name":name , "salary":newsalary}
											db.child("Employee12").child(id).set(info) 
											showinfo("Suceess","ID Updated")
							except ValueError:
								showerror("Issue","Salary can not be an Alphabet")
						else: 
							showerror("Issue","ID Does Not Exists")
					else:
						showerror("Issue","Name can not contain Numbers or Special Characters") 
	except ValueError:
		showerror("Issue","ID Should not be Left empty or It can not contain Special Characters or A Single Digit")
	uw_ent_id.delete(0,END) 
	uw_ent_name.delete(0,END) 
	uw_ent_salary.delete(0,END) 
	uw_ent_id.focus()

def f14():
	#data = pd.read_json("SAL.json")
	#data.to_csv("SAL.csv")
	data = pd.read_csv("SAL.csv")
	x = data['name'].tolist()
	y= data['salary'].tolist()
	plt.bar(x,y,color = "red")
	plt.xlabel("Name Of the Employee")
	plt.ylabel("Salary Per Month") 
	plt.title("Salary Graph of Top 5 Employees")
	plt.show()

def f15(): 
	ww.withdraw()
	lp.deiconify()

def f16(): 
	username=lp_ent_user.get() 
	password=lp_ent_pass.get()  
	if len(lp_ent_user.get()) == 0:
		showerror("Issue","Username can not be left empty")
	else:
		if len(lp_ent_pass.get())==0:
			showerror("Issue","Password can not be left empty")
		else:
			if (username=="Dipen123") and (password=="1234"): 
				lp.withdraw()
				mw.deiconify()
			else: 
				showerror("Issue","Inavalid Username or Password") 
	lp_ent_pass.delete(0,END) 
	lp_ent_user.delete(0,END) 
	lp_ent_user.focus()

def f17(): 
	raw_TS=datetime.now(IST) 
	date_now=raw_TS.strftime("%d %b %Y")
	time_now=raw_TS.strftime("%H:%M:%S %p") #I FOR 12HR FORMAT 
	lab_date_now.configure(text="Date:"+str(date_now))
	lab_time_now.configure(text="Time:"+str(time_now))
	lab_date_now.after(1000,f17) 

def f19():
	if lp_ent_pass.cget('show')=='*':
		lp_ent_pass.config(show='')
	else:
		lp_ent_pass.config(show='*')

'''Welcome Window'''
ww=Tk() 
ww.title("E.M.S. By Dipen") 
ww.geometry("800x600+100+0")
ww_lab_wel=Label(ww,text="Welcome User",font=f) 
ww_lab_wel.pack(pady=10)
lab_date_now=Label(ww,text="",font=f) 
lab_date_now.pack(pady=10) 
lab_time_now=Label(ww,text="",font=f) 
lab_time_now.pack(pady=10)
ww_lab_note=Label(ww,text="Make Sure That you Are Connected to a Good Internet",font=f,wraplength=700) 
ww_lab_note.pack(pady=10)
ww_btn_next=Button(ww,text="Next",font=f,command=f15) 
ww_btn_next.pack(pady=10)
f17()


'''Login Page'''
lp=Toplevel() 
lp.title("Login Page") 
lp.geometry("800x600+100+0") 
lp_lab_user=Label(lp,text="Enter Username",font=f) 
lp_lab_user.pack(pady=5) 
lp_ent_user=Entry(lp,font=f) 
lp_ent_user.pack(pady=5) 
lp_lab_pass=Label(lp,text="Enter Password",font=f) 
lp_lab_pass.pack(pady=5) 
lp_ent_pass=Entry(lp,font=f,show='*') 
lp_ent_pass.pack(pady=5)
lp_cb_xyz=Checkbutton(lp,text="Show Password",command=f19)
lp_cb_xyz.pack(pady=5)
lp_btn_submit=Button(lp,font=f,text="Submit",command=f16) 
lp_btn_submit.pack(pady=5)
lp.withdraw()

'''Main Window'''
mw=Toplevel()
mw.title("Main Window") 
mw.geometry("800x600+100+0") 
mw_btn_add = Button(mw,text="Add Employee",font=f,width=15,command=f1)
mw_btn_add.pack(pady=5) 
mw_btn_del = Button(mw,text="Delete Employee",font=f,width=15,command=f2) 
mw_btn_del.pack(pady=5) 
mw_btn_view = Button(mw,text="View Details",font=f,width=15,command=f3) 
mw_btn_view.pack(pady=5) 
mw_btn_update = Button(mw,text="Update",font=f,width=15,command=f4) 
mw_btn_update.pack(pady=5) 
mw_btn_chart = Button(mw,text="Graph",font=f,width=15,command=f5)
mw_btn_chart.pack(pady=5) 
mw_lab_lt=Label(mw,text="",font=f) 
mw_lab_lt.pack(pady=5)
mw.withdraw()

'''Add Window'''
aw=Toplevel()
aw.title("Add Employee") 
aw.geometry("800x600+100+0")
aw_lab_id=Label(aw,text="Enter Employee ID",font=f) 
aw_lab_id.pack()
aw_ent_id = Entry(aw,font=f) 
aw_ent_id.pack()
aw_lab_name=Label(aw,text="Enter Employee Name",font=f) 
aw_lab_name.pack()
aw_ent_name=Entry(aw,font=f) 
aw_ent_name.pack() 
aw_lab_salary= Label(aw,text="Enter Employee Salary",font=f) 
aw_lab_salary.pack() 
aw_ent_salary=Entry(aw,font=f) 
aw_ent_salary.pack()
aw_btn_save=Button(aw,text="Save",font=f,command=f11) 
aw_btn_save.pack(pady=10) 
aw_btn_back=Button(aw,text="Back",font=f,command=f6)
aw_btn_back.pack(pady=10)
aw.withdraw() 

'''Delete Window'''
dw=Toplevel()
dw.title("Delete Employee")
dw.geometry("800x600+100+0")
dw_lab_id=Label(dw,text="Enter Employee ID",font=f) 
dw_lab_id.pack(pady=10) 
dw_ent_id=Entry(dw,font=f) 
dw_ent_id.pack(pady=10) 
dw_btn_delete=Button(dw,text="Delete",font=f,command=f12) 
dw_btn_delete.pack(pady=10) 
dw_btn_back=Button(dw,text="Back",font=f,command=f7) 
dw_btn_back.pack(pady=10)
dw.withdraw()

'''View Window'''
vw=Toplevel() 
vw.title("View Employee") 
vw.geometry("800x600+100+0")
vw_st_view=ScrolledText(vw,font=f,height=5,width=120) 
vw_st_view.pack(pady=10) 
vw_btn_back=Button(vw,text="Back",font=f,command=f8) 
vw_btn_back.pack(pady=10) 
vw.withdraw()

'''Update Window''' 
uw=Toplevel() 
uw.title("Update Employee") 
uw.geometry("800x600+100+0")
uw_lab_id=Label(uw,text="Enter Employee ID",font=f) 
uw_lab_id.pack() 
uw_ent_id=Entry(uw,font=f) 
uw_ent_id.pack() 
uw_lab_name=Label(uw,text="Enter Employee Name",font=f) 
uw_lab_name.pack() 
uw_ent_name=Entry(uw,font=f) 
uw_ent_name.pack()
uw_lab_salary=Label(uw,text="Enter New Salary",font=f)
uw_lab_salary.pack() 
uw_ent_salary=Entry(uw,font=f) 
uw_ent_salary.pack()
uw_btn_update=Button(uw,text="Update",font=f,command=f13) 
uw_btn_update.pack(pady=10) 
uw_btn_back=Button(uw,text="Back",font=f,command=f9)
uw_btn_back.pack(pady=10)
uw.withdraw()

'''Chart Window'''
cw=Toplevel() 
cw.title("Salary Graph") 
cw.geometry("800x600+100+0")
cw_lab_not=Label(cw,text="Notice:",font=f)
cw_lab_not.pack()
cw_lab_abc=Label(cw,text="Make Sure that you have Updated your CSV File",font=f,wraplength=650)
cw_lab_abc.pack()
cw_btn_back=Button(cw,text="Click To See The Graph",font=f,command=f14)
cw_btn_back.pack(pady=10)
cw_btn_back=Button(cw,text="Back",font=f,command=f10)
cw_btn_back.pack(pady=10)
cw.withdraw()

ww.mainloop()