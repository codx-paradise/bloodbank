import sqlite3
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk

main=Tk()

main.title("Blood Bank System")
main.resizable(0,0)
main.geometry('1100x600')

#images
logo2=ImageTk.PhotoImage(file='/home/ak/Downloads/bloodbank/logo2.jpg')
homebg=ImageTk.PhotoImage(file='/home/ak/Downloads/bloodbank/home.jpg')
bgimg=ImageTk.PhotoImage(file="/home/ak/Downloads/bloodbank/bg.png")
accicon= ImageTk.PhotoImage(file="/home/ak/Downloads/bloodbank/account.png")
lgimg=ImageTk.PhotoImage(file='/home/ak/Downloads/bloodbank/padlock.png')
ssimg=ImageTk.PhotoImage(file='/home/ak/Downloads/bloodbank/logo.png')
c2img=ImageTk.PhotoImage(file='/home/ak/Downloads/bloodbank/login.png')
bloodimg=ImageTk.PhotoImage(file='/home/ak/Downloads/bloodbank/blood.png')

def Doner():
    donerfrm=Frame(main).place(x=0,y=0)
    label1=Label(donerfrm,bg='white',width=1100,height=600).place(x=0,y=0)
    menu()
    label4=Label(main,image=logo2,bd=0).place(x=950,y=10)  
    
    detailfrm=LabelFrame(donerfrm,bg='#ffd580',width=350,height=400).place(x=220,y=110)
    label2=Label(donerfrm,text='Doner Details   ',font=("",28,'bold'),bg='white',fg='#c70039').place(x=450,y=20)

    donerid=StringVar()
    name=StringVar()
    bgroup=StringVar()
    gender=StringVar()
    mobile=StringVar()
    address=StringVar()

    def clear():
        donerid.set("")
        name.set("")
        bgroup.set("")
        gender.set("")
        mobile.set("")
        address.set("")
    
    def add():
        conn = sqlite3.connect("/home/ak/Downloads/bloodbank/database.db")
        cur = conn.cursor()
        cur.execute(
                "INSERT INTO doner values(?,?,?,?,?,?)",
                (donerid.get(),name.get(),mobile.get(),bgroup.get(),gender.get(),address.get()))
        conn.commit()
        conn.close()
        show_all()
        clear()
        messagebox.showinfo("Success", "Doner Details Insert Successfully")
    
    def update():
        conn = sqlite3.connect("/home/ak/Downloads/bloodbank/database.db")
        cur = conn.cursor()
        cur.execute(
                "UPDATE doner set name=?,mobile=?,bg=?,gender=?,address=? where "
                "id=?",
                (name.get(),mobile.get(),bgroup.get(),gender.get(),address.get(),donerid.get()))
        conn.commit()
        conn.close()
        show_all()
        clear()
        messagebox.showinfo("Success", "Doner Details Updated Successfully")
    
    def delete():
        conn = sqlite3.connect("/home/ak/Downloads/bloodbank/database.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM doner where id=?",
                        (donerid.get()))
        conn.commit()
        conn.close()
        show_all()
        clear()
        messagebox.showinfo("Success", "Records Deleted Successfully")
    
    addbtn=Button(donerfrm,text='Add',width=15,command=add).place(x=500,y=530)
    updatebtn=Button(donerfrm,text='Update',width=15,command=update).place(x=650,y=530)
    deletebtn=Button(donerfrm,text='Delete',width=15,command=delete).place(x=800,y=530)
    clearbtn=Button(detailfrm,text='Clear',width=15,command=clear).place(x=320,y=450)

    label=Label(detailfrm,text="ID :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=225,y=150)
    label=Label(detailfrm,text="Name :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=225,y=200)
    label=Label(detailfrm,text="Gender :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=225,y=250)
    label=Label(detailfrm,text="Mobile :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=225,y=300)
    label=Label(detailfrm,text="Blood Group :",font=("",10,'bold'),bg='#ffd580',width=12).place(x=222,y=350)
    label=Label(detailfrm,text="Address :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=225,y=400)
    
    idtxt=Entry(detailfrm,textvariable=donerid,width=20,justify='center',font=("",10,'bold'),highlightcolor='#c70039',highlightthickness=2,bd=0,highlightbackground='gray').place(x=350,y=150,height=25)
    nametxt=Entry(detailfrm,textvariable=name,width=20,justify='center',font=("",10,'bold'),highlightcolor='#c70039',highlightthickness=2,bd=0,highlightbackground='gray').place(x=350,y=200,height=25)
    gentxt=Entry(detailfrm,textvariable=gender,width=20,justify='center',font=("",10,'bold'),highlightcolor='#c70039',highlightthickness=2,bd=0,highlightbackground='gray').place(x=350,y=250,height=25)
    mobtxt=Entry(detailfrm,textvariable=mobile,width=20,justify='center',font=("",10,'bold'),highlightcolor='#c70039',highlightthickness=2,bd=0,highlightbackground='gray').place(x=350,y=300,height=25)
    exptxt=Entry(detailfrm,textvariable=bgroup,width=20,justify='center',font=("",10,'bold'),highlightcolor='#c70039',highlightthickness=2,bd=0,highlightbackground='gray').place(x=350,y=350,height=25)
    qualtxt=Entry(detailfrm,textvariable=address,width=20,justify='center',font=("",10,'bold'),highlightcolor='#c70039',highlightthickness=2,bd=0,highlightbackground='gray').place(x=350,y=400,height=25)
    
    def dn_info(ev):
        viewInfo = dn_tree.focus()
        dn_data = dn_tree.item(viewInfo)
        row = dn_data['values']
        donerid.set(row[0])
        name.set(row[1])
        mobile.set(row[2])
        bgroup.set(row[3])
        gender.set(row[4])
        address.set(row[5])

    def show_all():
        conn = sqlite3.connect("/home/ak/Downloads/bloodbank/database.db")
        cur = conn.cursor()
        cur.execute("select * from doner")
        rows = cur.fetchall()
        if len(rows) != 0:
            dn_tree.delete(*dn_tree.get_children())
            for row in rows:
                dn_tree.insert('', END, values=row)
            conn.commit()
        conn.close()
    
    scrollbary = Scrollbar(detailfrm, orient=VERTICAL)
    dn_tree = ttk.Treeview(detailfrm)
    dn_tree.place(x=600, y=110, width=450, height=400)
    dn_tree.configure( yscrollcommand=scrollbary.set)
    dn_tree.configure(selectmode="extended")
    scrollbary.configure(command=dn_tree.yview)
    scrollbary.place(x=1055, y=110, width=10, height=400)
    
    dn_tree.configure(columns=("id","name","mobile","bg"))
    dn_tree.heading("id", text="Id", anchor=N)
    dn_tree.heading("name", text="Name",anchor=CENTER)
    dn_tree.heading("mobile", text="Mobile",anchor=CENTER)
    dn_tree.heading("bg", text="Blood Group",anchor=CENTER)

    dn_tree.column("#0", stretch=NO, minwidth=0, width=0)
    dn_tree.column("#1", stretch=NO, minwidth=0, width=50, anchor=CENTER)
    dn_tree.column("#2", stretch=NO, minwidth=0, width=200, anchor=CENTER)
    dn_tree.column("#3", stretch=NO, minwidth=0, width=200, anchor=CENTER)
    dn_tree.column("#4", stretch=NO, minwidth=0, width=200, anchor=CENTER)
    dn_tree.bind("<ButtonRelease-1>", dn_info)
    show_all()  

def ser():
    donerfrm=Frame(main).place(x=0,y=0)
    label1=Label(donerfrm,bg='white',width=1100,height=600).place(x=0,y=0)
    menu()
    label4=Label(main,image=logo2,bd=0).place(x=950,y=10)  
    
    detailfrm=LabelFrame(donerfrm,bg='#ffd580',width=350,height=400).place(x=220,y=110)
    label2=Label(donerfrm,text='Search Doner',font=("",28,'bold'),bg='white',fg='#c70039').place(x=450,y=20)

    donerid=StringVar()
    name=StringVar()
    bgroup=StringVar()
    gender=StringVar()
    mobile=StringVar()
    address=StringVar()
    searchbg=StringVar()

    def clear():
        donerid.set("")
        name.set("")
        bgroup.set("")
        gender.set("")
        mobile.set("")
        address.set("")
    
    
    label3=Label(donerfrm,text='Enter Location :',font=("",15,'bold'),bg='white').place(x=600,y=120)
    searchtxt=Entry(donerfrm,width=18,bd=0,textvariable=searchbg,highlightbackground='orange',highlightcolor='green',highlightthickness=2,font=("",10,'bold')).place(x=830,y=120,height=30)

    clearbtn=Button(detailfrm,text='Clear',width=15,command=clear).place(x=320,y=450)

    label=Label(detailfrm,text="          ID :",font=("",10,'bold'),bg='#ffd580').place(x=230,y=150)
    label=Label(detailfrm,text="      Name :",font=("",10,'bold'),bg='#ffd580').place(x=230,y=200)
    label=Label(detailfrm,text="     Gender :",font=("",10,'bold'),bg='#ffd580').place(x=230,y=250)
    label=Label(detailfrm,text="     Mobile :",font=("",10,'bold'),bg='#ffd580').place(x=230,y=300)
    label=Label(detailfrm,text="Blood Group :",font=("",10,'bold'),bg='#ffd580').place(x=230,y=350)
    label=Label(detailfrm,text="    Address :",font=("",10,'bold'),bg='#ffd580').place(x=230,y=400)
    
    idtxt=Entry(detailfrm,textvariable=donerid,state='readonly',width=20,font=("",10,'bold'),highlightthickness=0,bd=0).place(x=350,y=150,height=25)
    nametxt=Entry(detailfrm,textvariable=name,state='readonly',width=20,font=("",10,'bold'),highlightthickness=0,bd=0).place(x=350,y=200,height=25)
    gentxt=Entry(detailfrm,textvariable=gender,state='readonly',width=20,font=("",10,'bold'),highlightthickness=0,bd=0).place(x=350,y=250,height=25)
    mobtxt=Entry(detailfrm,textvariable=mobile,state='readonly',width=20,font=("",10,'bold'),highlightthickness=0,bd=0).place(x=350,y=300,height=25)
    exptxt=Entry(detailfrm,textvariable=bgroup,state='readonly',width=20,font=("",10,'bold'),highlightthickness=0,bd=0).place(x=350,y=350,height=25)
    qualtxt=Entry(detailfrm,textvariable=address,state='readonly',width=20,font=("",10,'bold'),highlightthickness=0,bd=0).place(x=350,y=400,height=25)
    
    def dn_info(ev):
        viewInfo = dn_tree.focus()
        dn_data = dn_tree.item(viewInfo)
        row = dn_data['values']
        donerid.set(row[0])
        name.set(row[1])
        mobile.set(row[2])
        bgroup.set(row[3])
        gender.set(row[4])
        address.set(row[5])

    def Search():
        conn = sqlite3.connect("/home/ak/Downloads/bloodbank/database.db")
        cur = conn.cursor()
        cur.execute("select * from doner where address=?",[searchbg.get()])
        rows = cur.fetchall()
        dn_tree.delete(*dn_tree.get_children())
        
        for row in rows:
            dn_tree.insert('', END, values=row)
        conn.commit()
        conn.close()
    
    scrollbary = Scrollbar(detailfrm, orient=VERTICAL)
    dn_tree = ttk.Treeview(detailfrm)
    dn_tree.place(x=600, y=260, width=450, height=250)
    dn_tree.configure( yscrollcommand=scrollbary.set)
    dn_tree.configure(selectmode="extended")
    scrollbary.configure(command=dn_tree.yview)
    scrollbary.place(x=1055, y=260, width=10, height=250)
    
    dn_tree.configure(columns=("id","name","mobile","bg"))
    dn_tree.heading("id", text="Id", anchor=N)
    dn_tree.heading("name", text="Name",anchor=CENTER)
    dn_tree.heading("mobile", text="Mobile",anchor=CENTER)
    dn_tree.heading("bg", text="Blood Group",anchor=CENTER)

    dn_tree.column("#0", stretch=NO, minwidth=0, width=0)
    dn_tree.column("#1", stretch=NO, minwidth=0, width=50, anchor=CENTER)
    dn_tree.column("#2", stretch=NO, minwidth=0, width=200, anchor=CENTER)
    dn_tree.column("#3", stretch=NO, minwidth=0, width=200, anchor=CENTER)
    dn_tree.column("#4", stretch=NO, minwidth=0, width=200, anchor=CENTER)
    dn_tree.bind("<ButtonRelease-1>", dn_info)  
    
    searchbtn=Button(donerfrm,text='Search',width=15,command=Search).place(x=750,y=180)

def About():
    label1=Label(main,width=1100,height=600,bg='white').place(x=0,y=0)
    menu()
    label4=Label(main,image=logo2,bd=0).place(x=950,y=10)
    
    label2=Label(main,text='Compatible Blood Type Doners',font=("",20,'bold'),bg='white',fg='red').place(x=350,y=70)
    
    label3=Label(main,text='\t Blood Type\t Donate Blood To \t   Receive Blood To',font=("",13,'bold'),bg='white',fg='#c70039').place(x=200,y=160)
    
    label4=Label(main,text='A+ \t\t\t   A+,AB+ \t\t A+,A-,O+,O-',font=("",10,'bold'),width=63).place(x=300,y=200)
    label5=Label(main,text='O+'+'\t\t\t'+'A+,B+,O+,AB+'+'\t\t'+'O+,O-\t',font=("",10,'bold'),width=63).place(x=300,y=240)
    label6=Label(main,text='B+ \t\t\t   B+,AB+ \t\t B+,B-,O+,O-',font=("",10,'bold'),width=63).place(x=300,y=280)
    label7=Label(main,text='AB+ \t\t\t   AB+ \t\t\t Everyone',font=("",10,'bold'),width=63).place(x=300,y=320)
    label8=Label(main,text='A- \t\t\t   A+,A-,AB+,AB- \t\t A-,O-',font=("",10,'bold'),width=63).place(x=300,y=360)
    label9=Label(main,text='O- \t\t\t   Everyone \t\t O-',font=("",10,'bold'),width=63).place(x=300,y=400)
    label10=Label(main,text='B- \t\t\t   B+,B-,AB+,AB- \t\t B-,O-',font=("",10,'bold'),width=63).place(x=300,y=440)
    label11=Label(main,text='AB- \t\t\t   AB+,AB- \t\t AB-,A-,B-,O-',font=("",10,'bold'),width=63).place(x=300,y=480)

def Home():
    label1=Label(main,bg='white',width=1200,height=600).place(x=0,y=0)
    menu()
    label2=Label(main,image=homebg,bg='white').place(x=350,y=80) 
    label1=Label(main,text='Donate blood , Donate Smile !',font=("",20,'bold'),fg='gray',bg='white').place(x=430,y=500)

def login():
    lbl1=Label(main,width=1100,height=610,bg='white').place(x=0,y=0)
    lbl2=Label(main,text='Blood Bank System',font=("",25,'bold'),bg='white',fg='red').place(x=400,y=30)
    label2=Label(main,bg='white',image=c2img).place(x=100,y=100)
    
    def login_all():
        conn = sqlite3.connect("/home/ak/Downloads/bloodbank/database.db")
        cur = conn.cursor()
        find_user = 'SELECT * FROM login WHERE user = ? and pass= ?'
        cur.execute(find_user, [(username_entry.get()), (password_entry.get())])
        result= cur.fetchone()
        
        if result!=None:
            Home()
            
        else:
            messagebox.showerror("Failed", "Wrong Login details, please try again.")
    
    def click(*args):
        username_entry.delete(0,'end')
    
    def click2(*args):
        password_entry.delete(0,'end')
    
    lbl11=Label(main,text="______________________________",font=("",15,'bold'),bg='white',fg='gray').place(x=650,y=260)
    lbl11=Label(main,text="______________________________",font=("",15,'bold'),bg='white',fg='gray').place(x=650,y=350)
    
    lbl11=Label(main,image=accicon,bg='white').place(x=660,y=250)
    lbl11=Label(main,image=lgimg,bg='white').place(x=660,y=340)
        
    username_entry = Entry(main,bd=0, bg="white", fg="gray",font=("", 10,'bold'))
    username_entry.place(x=700, y=255, width=200, height=20)
    username_entry.config(highlightbackground="white", highlightcolor="white")
    username_entry.insert(0,"Username")

    password_entry = Entry(main,bd=0, bg="white", fg="gray", font=("", 10,'bold'), show="•")
    password_entry.place(x=700, y=345, width=200, height=20)
    password_entry.config(highlightbackground="white", highlightcolor="white")
    password_entry.insert(0,"Password")

    username_entry.bind("<Button-1>",click)
    password_entry.bind("<Button-1>",click2)

    loginButton = Button(main, text='Login',fg='white',bg='red',bd=0, font=("", 12, "bold"),cursor='hand2', command=login_all)
    loginButton.place(x=680, y=420, width=250, height=35)
    loginButton.config(highlightbackground="red", highlightthickness=2)

def dashboard():
    label1=Label(main,bg='white',width=1200,height=600).place(x=0,y=0)
    menu()
    label4=Label(main,image=logo2,bd=0).place(x=950,y=10)
    
    label2=Label(main,text='Dashboard ',font=("",25,'bold'),bg='white',fg='#c70039').place(x=500,y=20)
    label1=Label(main,text='Available Blood per group in Liters',font=("",13,'bold'),bg='white').place(x=250,y=90)
  
    fr3=LabelFrame(main,bg='lightgray',width=270,height=90,bd=0).place(x=300,y=150)
    label1=Label(fr3,text="A+ ",image=bloodimg,compound='right',bg='lightgray',font=("",28)).place(x=460,y=150)
    label1=Label(fr3,text='8',bg='lightgray',font=("",22)).place(x=350,y=175)

    fr3=LabelFrame(main,bg='lightgray',width=270,height=90,bd=0).place(x=300,y=250)
    label1=Label(fr3,text="B+ ",image=bloodimg,compound='right',bg='lightgray',font=("",28)).place(x=460,y=250)
    label1=Label(fr3,text='10',bg='lightgray',font=("",22)).place(x=350,y=275)

    fr3=LabelFrame(main,bg='lightgray',width=270,height=90,bd=0).place(x=300,y=350)
    label1=Label(fr3,text="O+ ",image=bloodimg,compound='right',bg='lightgray',font=("",28)).place(x=460,y=350)
    label1=Label(fr3,text='5',bg='lightgray',font=("",22)).place(x=350,y=375)

    fr3=LabelFrame(main,bg='lightgray',width=270,height=90,bd=0).place(x=300,y=450)
    label1=Label(fr3,text="AB+",image=bloodimg,compound='right',bg='lightgray',font=("",28)).place(x=450,y=450)
    label1=Label(fr3,text='7',bg='lightgray',font=("",22)).place(x=350,y=475)

    fr3=LabelFrame(main,bg='lightgray',width=270,height=90,bd=0).place(x=700,y=250)
    label1=Label(fr3,text="B- ",image=bloodimg,compound='right',bg='lightgray',font=("",28)).place(x=860,y=250)
    label1=Label(fr3,text='2',bg='lightgray',font=("",22)).place(x=750,y=275)

    fr3=LabelFrame(main,bg='lightgray',width=270,height=90,bd=0).place(x=700,y=350)
    label1=Label(fr3,text="O- ",image=bloodimg,compound='right',bg='lightgray',font=("",28)).place(x=860,y=350)
    label1=Label(fr3,text='8',bg='lightgray',font=("",22)).place(x=750,y=375)

    fr3=LabelFrame(main,bg='lightgray',width=270,height=90,bd=0).place(x=700,y=450)
    label1=Label(fr3,text="AB-",image=bloodimg,compound='right',bg='lightgray',font=("",28)).place(x=860,y=450)
    label1=Label(fr3,text='0',bg='lightgray',font=("",22)).place(x=750,y=475)

    fr3=LabelFrame(main,bg='lightgray',width=270,height=90,bd=0).place(x=700,y=150)
    label1=Label(fr3,text="A- ",image=bloodimg,compound='right',bg='lightgray',font=("",28)).place(x=860,y=150)
    label1=Label(fr3,text='9',bg='lightgray',font=("",22)).place(x=750,y=175)

def menu():
    mnfrm=LabelFrame(main,bg='red',bd=0,width=200,height=600).place(x=0,y=0)
    lg=Label(mnfrm,image=bgimg,bg='red').place(x=50,y=10)
    
    btn1=Button(mnfrm,text='Home',font=("",10,'bold'),bg='red',cursor='hand2',command=Home,fg='white',bd=0,highlightthickness=0,activebackground='red').place(x=10,y=150)
    btn1=Button(mnfrm,text='Dashboard',font=("",10,'bold'),cursor='hand2',command=dashboard,bg='red',fg='white',bd=0,highlightthickness=0,activebackground='red').place(x=10,y=200)
    btn1=Button(mnfrm,text='Doner',font=("",10,'bold'),cursor='hand2',command=Doner,bg='red',fg='white',bd=0,highlightthickness=0,activebackground='red').place(x=10,y=250)
    btn1=Button(mnfrm,text='Search',font=("",10,'bold'),cursor='hand2',command=ser,bg='red',fg='white',bd=0,highlightthickness=0,activebackground='red').place(x=10,y=300)
    btn1=Button(mnfrm,text='About',font=("",10,'bold'),cursor='hand2',command=About,bg='red',fg='white',bd=0,highlightthickness=0,activebackground='red').place(x=10,y=350)
    btn1=Button(mnfrm,text='Developer',font=("",10,'bold'),cursor='hand2',command=Dev,bg='red',fg='white',bd=0,highlightthickness=0,activebackground='red').place(x=10,y=400)
    btn1=Button(mnfrm,text='Logout',font=("",10,'bold'),cursor='hand2',command=login,bg='red',fg='white',bd=0,highlightthickness=0,activebackground='red').place(x=10,y=450)

def Dev():
    label1=Label(main,bg='white',width=1200,height=600).place(x=0,y=0)
    menu()
    label4=Label(main,image=logo2,bd=0).place(x=950,y=10)
    label1=Label(main,image=ssimg,bg='white').place(x=250,y=100)
    
    label1=Label(main,text='AK MOORTHI',font=("",28,'bold'),bg='white',fg='#3e5348').place(x=600,y=140)
    label1=Label(main,text='REG NO : C21PG188CSC012',font=("",15,'bold'),bg='white').place(x=550,y=330)        
    label1=Label(main,text='COURSE : MSC COMPUTER SCIENCE',font=("",15,'bold'),bg='white').place(x=550,y=400)
    label1=Label(main,text='TITLE     : BLOOD BANK SYSTEM',font=("",15,'bold'),bg='white').place(x=550,y=260)
    label1=Label(main,text='YEAR      : II-YEAR',font=("",15,'bold'),bg='white').place(x=550,y=470)


login()

main.mainloop()