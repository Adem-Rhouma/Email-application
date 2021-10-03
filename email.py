from tkinter import*
root=Tk()
root.title('Email application')
root.geometry("400x400")



a=1

Email_List=[]
password_list=[]
def Register_option():

    The_Button__Login__.forget()
    The_Button__Register__.forget()

    The_RegisterEmail.delete(0, END)
    The_RegisterPassword.delete(0, END)

    Email_Register.pack()
    The_RegisterEmail.pack()
    RegisterEmail_continue.pack()

def Email_Creation():

    if ( '@' not in The_RegisterEmail.get()) or (  '.' not in The_RegisterEmail.get()) :
        Invalid_Email.pack()
    elif The_RegisterEmail.get().index('.') < The_RegisterEmail.get().index('@'):
        Invalid_Email.pack()
    else:
        Success_Email_Register.pack()

        Success_Email_Register.pack_forget()
        Invalid_Email.pack_forget()
        The_RegisterEmail.forget()
        RegisterEmail_continue.forget()
        Email_Register.pack_forget()
        Password_Register.pack()

        The_RegisterPassword.pack()
        RegisterPassword_Continue.pack()


def Password_Creation():
    if len(The_RegisterPassword.get()) < 6:
        Invalid_Password.pack()
    else:
        Invalid_Password.pack()
        Sucess_Account_Created=Label(root, text="Account has been successfuly added to our data base")
        Sucess_Account_Created.pack()

        Email_List.append(The_RegisterEmail.get())
        password_list.append(The_RegisterPassword.get())

        Invalid_Password.pack_forget()
        RegisterPassword_Continue.forget()
        The_RegisterPassword.forget()
        Password_Register.pack_forget()
        Sucess_Account_Created.pack_forget()


        The_Button__Login__.pack()
        The_Button__Register__.pack()





def Login_option():
    The_Button__Login__.forget()
    The_Button__Register__.forget()


    Login_Email.pack()
    The_LoginEmailBox.pack()
    Login_Password.pack()
    The_LoginPasswordBox.pack()
    Login_Continue.pack()

def Login():
    if The_LoginEmailBox.get() not in Email_List:
        Invalid_Email.pack()

    elif The_LoginPasswordBox.get() not in password_list:
        Invalid_Password.pack()

    elif Email_List.index(The_LoginEmailBox.get()) != password_list.index(The_LoginPasswordBox.get()):
        Invalid_Password.pack()
    else:
        Sucess_Login=Label(root, text="you have successfuly logged in")
        Sucess_Login.pack()
        Invalid_Email.pack()


        Sucess_Login.pack_forget()
        Login_Email.pack_forget()
        Login_Password.forget()
        The_LoginPasswordBox.forget()
        Login_Continue.forget()
        The_LoginEmailBox.forget()
        The_LoginEmailBox.delete(0, END)
        The_LoginPasswordBox.delete(0, END)
        Invalid_Email.pack_forget()
        Invalid_Password.pack_forget()

        The_Button__Login__.pack()
        The_Button__Register__.pack()











Invalid_Password=Label(root, text="Invalid Password")

Invalid_Email=Label(root, text="Invalid email, please try again")
Success_Email_Register=Label(root, text="Email sucess test")

Password_Register=Label(root, text="please enter your Password here")
Email_Register=Label(root, text="please enter your new email here")

RegisterEmail_continue=Button(root, text="Continue", command=Email_Creation)
RegisterPassword_Continue=Button(root, text="Continue", command=Password_Creation)


The_LoginEmailBox=Entry(root, width=40)
The_LoginPasswordBox=Entry(root, width=40)

The_RegisterEmail=Entry(root, width=40)
The_RegisterPassword=Entry(root, width=40)

The_Button__Login__=Button(root, text="Login", command=Login_option)
The_Button__Login__.pack()

The_Button__Register__=Button(root, text="Register", command=Register_option)
The_Button__Register__.pack()

Login_Continue=Button(root, text="Continue", command=Login)

Login_Email=Label(root, text="Enter your email here")
Login_Password=Label(root, text="Enter your password here")

print('it worked!!')




root.mainloop()
