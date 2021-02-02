from tkinter import *
import tkinter.messagebox as all


def addcash():
    import tkinter.messagebox as conf
    user1 = userentry.get()

    def save():
        try:
            f = open(f"{user1} money.txt")
            baal = int(f.read())
            # f.close()
            abc = int(e1.get())
            bal = abc + baal
            bal = str(bal)
            f1 = open(f"{user1} money.txt", 'w')
            f1.write(bal + "\n")
            conf.showinfo("Submitted", f"Money {abc} is  added Successful")
            c=1

        except:

            if c == 1:
                exit()
            else:
                conf.showinfo("Invalid","Invalid Username")


    root = Tk()
    root.title("List Box")
    root.config(background="grey")
    root.geometry("550x300")

    l1 = Label(root, text="Enter Amount", font="lucida 20 bold", fg="black", borderwidth=10, relief=RIDGE)
    l1.grid(row=3, column=3, pady=50, padx=20)

    a1 = IntVar()

    e1 = Entry(root, textvariable=a1, font="lucida 15 bold", borderwidth=10, relief=RAISED)
    e1.grid(row=3, column=4)

    Button(root, text="Submit", font="lucida 15 bold", borderwidth=10, relief=RAISED, command=save).grid(row=5,
                                                                                                         column=4)

    root.mainloop()


def withdrow():
    import tkinter.messagebox as abcd
    root = Tk()
    root.title("List Box")
    root.config(background="grey")
    root.geometry("750x300")

    def wsubmit():
        import tkinter.messagebox as withd
        try:
            user2 = userentry.get()
            f = open(f"{user2} money.txt", 'r')
            ee = int(eentry.get())
            bal = int(f.read())
            f.close()
            bal = bal - ee
            if bal > 0:
                bal = str(bal)
                f = open(f"{user2} money.txt", 'w')
                f.write(bal)
                withd.showinfo("Withdrawal", f"Your Withdrawal Ammount is {ee}")
                c=1

            else:
                abcd.showinfo("Deny", "Insufficient Balance!!!")

        except:
            if c==1:
                exit()
            else:
                withd.showinfo("Invalid","Invalid Username")
                exit()
    a1 = IntVar()

    l1 = Label(root, text="Enter Withdrow Amount", font="lucida 20 bold", fg="black", borderwidth=10, relief=RIDGE)
    l1.grid(row=3, column=3, pady=50, padx=20)

    eentry = Entry(root, textvariable=a1, font="lucida 15 bold", borderwidth=10, relief=RAISED)
    eentry.grid(row=3, column=4)

    Button(root, text="Submit", font="lucida 15 bold", borderwidth=10, relief=RAISED, command=wsubmit).grid(row=5,
                                                                                                            column=4)

    root.mainloop()
def checkamount():
    import tkinter.messagebox as p

    # root=Tk()
    # root.geometry("200x250")
    # root.title("Your Balance")
    user2 = userentry.get()
    try:
        f = open(f"{user2} money.txt", 'r')
        bal = int(f.read())
        p.showinfo("balance",f"Total Amount is {bal}")
        c=1

    except:
        if c==1:
            exit()
        else:
            p.showinfo("Invalid","Invalid Username")


def User():
    root = Tk()
    root.geometry("715x350")
    root.title("Name")
    root.config(background="white")

    Button(root, text="Add Cash", font="lucida 20 bold", fg="white", bg="grey", borderwidth=20, relief=RAISED,
           command=addcash).grid(row=1, column=1,padx=3,pady=50)

    Button(root, text="Withdraw Cash", font="lucida 20 bold", fg="white", bg="grey", borderwidth=20, relief=RAISED,
           command=withdrow).grid(row=1, column=2,padx=3,pady=50)

    Button(root, text="Check Amount", font="lucida 20 bold", fg="white", bg="grey", borderwidth=20,
           relief=RAISED,command=checkamount).grid(row=1, column=3,padx=3,pady=50)

    Button(root, text="Log Out", font="lucida 20 bold", bg="grey", fg="white", borderwidth=20, relief=RAISED,
           command=exit).grid(row=2, column=2,padx=3,pady=50)
    def aboutus():
        import tkinter.messagebox as about
        about.showinfo("About Us ","This Application Is Created By Team Frost")
    def contactus():
        import tkinter.messagebox as contact
        contact.showinfo("Contact Us ", "If You Have Some internal issue then contact cscssingh123@gmail.com")

    menu1 = Menu(root)
    m1 = Menu(menu1, tearoff=0)
    m1.add_command(label="About us",command=aboutus)
    m1.add_command(label="Contact us",command=contactus)
    menu1.add_cascade(label="Help", menu=m1)

    root.config(menu=menu1)

    root.mainloop()


def newacc():
    root = Tk()
    import tkinter.messagebox as msd
    def save():
        print("Submitade")
        msd.showinfo("Successful","Your account Created Successful")
        print(f"{Fullname.get(), username.get(), userpass.get()}")
        f8 = open(f"{username.get()} money.txt", 'w')
        f8.write("0")
        with open("All data of user.txt", "a")as a:
            a.write(username.get() + " " + userpass.get() + " " + Fullname.get() + "\n")



    root.geometry("500x800")
    root.title("Create account")
    root.config(background="white")

    l1 = Label(root, text="Bank Mangement System", font="lucida 25 bold", fg="white", bg="black", padx=60, pady=10,
               relief=RIDGE)
    l1.grid(row=3, columnspan=5)

    l2 = Label(root, text="FullName", font="lucida 15 bold", fg="black",bg="grey",borderwidth=10, relief=RAISED)
    l2.grid(row=5, column=1,columnspan=1,pady=20)

    l3 = Label(root, text="Username", font="lucida 15 bold", fg="black",bg="grey", borderwidth=10, relief=RAISED)
    l3.grid(row=6, column=1,columnspan=1,pady=20)

    l4 = Label(root, text="Password", font="lucida 15 bold", fg="black",bg="grey",borderwidth=10, relief=RAISED)
    l4.grid(row=7, column=1,columnspan=1,pady=20)

    l5 = Checkbutton(root, text="Confirm", font="lucida 15 bold", fg="black",bg="grey", borderwidth=10, relief=RAISED)
    l5.grid(row=8, column=3, pady=20)

    a1 = StringVar()
    b1 = StringVar()
    c1 = StringVar()

    Fullname = Entry(root, textvariable=a1, font="lucida 15 bold", borderwidth=10, relief=RAISED)
    Fullname.grid(row=5, column=3)

    username = Entry(root, textvariable=b1, font="lucida 15 bold", borderwidth=10,relief=RAISED)
    username.grid(row=6, column=3)

    userpass = Entry(root, textvariable=c1, font="lucida 15 bold", borderwidth=10,relief=RAISED)
    userpass.grid(row=7, column=3)

    Button(root, text="Create Account", font="lucida 15 bold", fg="black", borderwidth=10, relief=RAISED,
           command=save,bg="grey").grid(column=3)

    root.mainloop()



def data():

        f = open("All data of user.txt")
        key = userentry.get()
        pas = userpass.get()
        if key !="" and pas !="":
            count = 1
            for line in f:
                line = line.rstrip()
                if line.startswith(key):
                    if pas in line:
                        print("Successful")
                        User()
                    else:
                        print("Wrong password!")
                        all.showinfo("Invalid", "Wrong Password")
                    count = 2
            if count == 1:
                print("Account not Found!!!")
                all.showinfo("Invalid", "Invalid Account")


root = Tk()
root.geometry("500x600")
root.title("Login Page")
root.config(background="white")

l1 = Label(root, text="Bank Mangement System", font="lucida 25 bold",fg="white",bg="black",padx=60,pady=10, relief=RIDGE)
l1.grid(row=3,columnspan=5)

l2 = Label(root, text="Username", font="lucida 15 bold", fg="black",bg="grey", borderwidth=10, relief=RAISED)
l2.grid(row=5, column=1,columnspan=1,pady=20)

l3 = Label(root, text="Password", font="lucida 15 bold", fg="black",bg="grey", borderwidth=10, relief=RAISED)
l3.grid(row=6, column=1,columnspan=1,pady=20)

a = StringVar()
b = StringVar()

userentry = Entry(root, textvariable=a, font="lucida 15", fg="black",borderwidth=10, relief=RAISED)
userentry.grid(row=5, column=3)
userpass = Entry(root, textvariable=b, font="lucida 15 bold", show="*",fg="black",borderwidth=10, relief=RAISED)
userpass.grid(row=6, column=3)

b1 = Button(root, text="Create New Account", font="lucida 15 bold", borderwidth=10, relief=RAISED,bg="grey", command=newacc)
b1.grid(column=3, pady=15)

b2 = Button(root, text="Login", font="lucida 15 bold", borderwidth=10, relief=RAISED,bg="grey", command=data)
b2.grid(column=3)


root.mainloop()
