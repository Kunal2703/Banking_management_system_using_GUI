from tkinter import *
import os
from PIL import ImageTk, Image

master = Tk()
master.title('Banking Management System')
master.geometry("2560x1600")


def register():
    ##############
    global temp_first_name
    global temp_middle_name
    global temp_surname
    global temp_dob

    global temp_age
    global temp_gender

    global temp_full_address
    global temp_pin_code
    global temp_email_id
    global temp_mobile_no

    global temp_user_name

    global temp_password
    global notif

    ####################

    temp_first_name = StringVar()
    temp_middle_name = StringVar()
    temp_surname = StringVar()
    temp_dob = StringVar()

    temp_age = StringVar()
    temp_gender = StringVar()

    temp_full_address = StringVar()
    temp_pin_code = StringVar()
    temp_email_id = StringVar()
    temp_mobile_no = StringVar()

    temp_user_name = StringVar()

    temp_password = StringVar()

    register_screen = Toplevel(master)
    register_screen.title('Register')
    register_screen.geometry("600x600")

    Label(register_screen, text="Please enter your details below to register", font=('Arial', 15, "bold")).grid(row=0,
                                                                                                                sticky=N,
                                                                                                                pady=10)

    Label(register_screen, text="First Name*", font=('Arial', 20, "bold")).grid(row=1, column=0)
    Label(register_screen, text="Middle Name", font=('Arial', 20, "bold")).grid(row=2, column=0)
    Label(register_screen, text="Surname", font=('Arial', 20, "bold")).grid(row=3, column=0)
    Label(register_screen, text="Date of Birth*", font=('Arial', 20, "bold")).grid(row=4, column=0)

    Label(register_screen, text="Age", font=('Arial', 20, "bold")).grid(row=5, column=0)
    Label(register_screen, text="Gender*", font=('Arial', 20, "bold")).grid(row=6, column=0)

    Label(register_screen, text="Full Address*", font=('Arial', 20, "bold")).grid(row=7, column=0)
    Label(register_screen, text="Pin Code*", font=('Arial', 20, "bold")).grid(row=8, column=0)
    Label(register_screen, text="Email Address", font=('Arial', 20, "bold")).grid(row=9, column=0)
    Label(register_screen, text="Mobile Number*", font=('Arial', 20, "bold")).grid(row=10, column=0)

    Label(register_screen, text="Username*", font=('Arial', 20, "bold")).grid(row=11, column=0)
    Label(register_screen, text="Password*", font=('Arial', 20, "bold")).grid(row=12, column=0)
    notif = Label(register_screen, font=('Arial', 20, "bold"))
    notif.grid(row=13, sticky=N, pady=10)

    Entry(register_screen, textvariable=temp_first_name).grid(row=1, column=1)
    Entry(register_screen, textvariable=temp_middle_name).grid(row=2, column=1)
    Entry(register_screen, textvariable=temp_surname).grid(row=3, column=1)
    Entry(register_screen, textvariable=temp_dob).grid(row=4, column=1)

    Entry(register_screen, textvariable=temp_age).grid(row=5, column=1)
    Entry(register_screen, textvariable=temp_gender).grid(row=6, column=1)

    Entry(register_screen, textvariable=temp_full_address).grid(row=7, column=1)
    Entry(register_screen, textvariable=temp_pin_code).grid(row=8, column=1)
    Entry(register_screen, textvariable=temp_email_id).grid(row=9, column=1)
    Entry(register_screen, textvariable=temp_mobile_no).grid(row=10, column=1)

    Entry(register_screen, textvariable=temp_user_name).grid(row=11, column=1)
    Entry(register_screen, textvariable=temp_password, show="*").grid(row=12, column=1)


    def finish_reg():
        first_name = temp_first_name.get()
        middle_name = temp_middle_name.get()
        surname = temp_surname.get()
        dob = temp_dob.get()

        age = temp_age.get()
        gender = temp_gender.get()

        full_address = temp_full_address.get()
        pin_code = temp_pin_code.get()
        email_id = temp_email_id.get()
        mobile_no = temp_mobile_no.get()

        user_name = temp_user_name.get()
        password = temp_password.get()
        all_accounts = os.listdir()

        if first_name == "" or dob == "" or gender == "" or full_address == "" or pin_code == "" or mobile_no == "" or user_name == "" or password == "":
            notif.config(fg="red", text="All * mark are required")
            return

        for name_check in all_accounts:
            if user_name == name_check:
                notif.config(fg="red", text="Account already exists")
                return
            else:
                new_file = open(user_name, "w")
                new_file.write(first_name + '\n') #0
                #new_file.write(password + '\n')
                new_file.write(middle_name + '\n') #1
                new_file.write(surname + '\n') #2
                new_file.write(dob + '\n') #3
                new_file.write(age + '\n') #4
                new_file.write(gender + '\n') #5
                new_file.write(full_address + '\n') #6
                new_file.write(pin_code + '\n') #7
                new_file.write(email_id + '\n') #8
                new_file.write(mobile_no + '\n') #9
                new_file.write(user_name + '\n') #10

                new_file.write(password + '\n') #11

                new_file.write('0')
                new_file.close()
                notif.config(fg="green", text="Account has been created")

            register_screen.destroy()

    # Button(register_screen, text="Register", command=finish_reg, font=('Arial', 10, "bold"), bd=3, relief=RIDGE, fg='blue', bg='black').grid(row=13, sticky=N, pady=10)

    button3 = Button(register_screen, text="Register", command=finish_reg, font=('Arial', 20, "bold"), bd=3,
                     relief=RIDGE, fg='blue', bg='red', width=20)
    button3.place(x=220, y=455, width=200, height=50)


def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for user_name in all_accounts:
        if user_name == login_name:
            file = open(user_name, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[11]
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Account Details')
                account_dashboard.geometry("800x500")

                ##################################################################################################################
                lable1 = Label(account_dashboard, text="Account Dashboard", font=('Comic Sans MS', 40, "bold"),
                               fg='red')
                lable1.place(x=200, y=30)
                lable2 = Label(account_dashboard, text="Hello " + user_name + " !!" "\nWelcome To Your Dashboard",
                               font=('Arial', 25, "bold"), fg='green')
                lable2.place(x=200, y=100)

                button3 = Button(account_dashboard, text="Personal Details", font=('Arial', 20, "bold"), bd=3,
                                 relief=RIDGE, fg='blue', bg='red',
                                 width=20, command=personal_details)
                button3.place(x=310, y=200, width=200, height=50)

                button2 = Button(account_dashboard, text="Deposit", font=('Arial', 20, "bold"), bd=3, relief=RIDGE,
                                 fg='blue', bg='red',
                                 width=20, command=deposit)
                button2.place(x=310, y=300, width=200, height=50)

                button1 = Button(account_dashboard, text="Withdraw", font=('Arial', 20, "bold"), bd=3, relief=RIDGE,
                                 fg='blue', bg='red',
                                 width=20, command=withdraw)
                button1.place(x=310, y=400, width=200, height=50)
                Label(account_dashboard).grid(row=5, sticky=N, pady=10)
                ###########################################################################################################################################################################
                return
            else:
                login_notif.config(fg="red", text="Password incorrect!!")
                return
    login_notif.config(fg="red", text="No account found !!")


##################################################################################################################
def deposit():
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[12]
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')
    deposit_screen.geometry("450x250")
    Label(deposit_screen, text="Deposit Dashboard", font=('Arial', 25, "bold"),fg = "red").grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(deposit_screen, text="Current Balance : Rs." + details_balance, font=('Arial', 15, "bold"))
    current_balance_label.grid(row=1, sticky=W)
    Label(deposit_screen, text="Amount : ", font=('Arial', 15, "bold")).grid(row=2, sticky=W)
    deposit_notif = Label(deposit_screen, font=('Arial', 15, "bold"))
    deposit_notif.grid(row=4, sticky=N, pady=5)
    Entry(deposit_screen, textvariable=amount).grid(row=2, column=1)

    Button(deposit_screen, text="Finish", font=('Arial', 25, "bold"), command=finish_deposit).grid(row=3, column = 1)


def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text='Amount is required!', fg="red")
        return
    if float(amount.get()) <= 0:
        deposit_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[12]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs." + str(updated_balance), fg="green")
    deposit_notif.config(text='Balance Updated', fg='green')

def withdraw():
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[12]
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Withdraw')
    withdraw_screen.geometry("500x250")
    Label(withdraw_screen, text="Withdraw Dashboard", font=('Arial', 25, "bold"),fg = "red").grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(withdraw_screen, text="Current Balance : Rs." + details_balance, font=('Arial', 15, "bold"))
    current_balance_label.grid(row=1, sticky=W)
    Label(withdraw_screen, text="Amount : ", font=('Arial', 15, "bold")).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_screen, font=('Arial', 15, "bold"))
    withdraw_notif.grid(row=4, sticky=N, pady=5)

    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2, column=1)

    Button(withdraw_screen, text="Finish", font=('Arial', 25, "bold"), command=finish_withdraw).grid(row=3, column =1)


def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text='Amount is required!', fg="red")
        return
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[12]

    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text='Insufficient Funds!', fg='red')
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs. " + str(updated_balance), fg="green")
    withdraw_notif.config(text='Balance Updated', fg='green')

def personal_details():
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_first_name = user_details[0]
    details_middle_name = user_details[1]
    details_surname = user_details[2]
    details_dob = user_details[3]

    details_age = user_details[4]
    details_gender = user_details[5]

    details_full_address = user_details[6]
    details_pin_code = user_details[7]
    details_email_id = user_details[8]
    details_mobile_no = user_details[9]

    details_balance = user_details[12]

    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    personal_details_screen.geometry("350x380")

    Label(personal_details_screen, text="Personal Details", font=('Arial', 25, "bold"),fg='green').grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="First Name : " + details_first_name, font=('Arial', 15)).grid(row=1, sticky=W)

    Label(personal_details_screen, text="Middle Name : " + details_middle_name, font=('Arial', 15)).grid(row=2, sticky=W)
    Label(personal_details_screen, text="Surname : " + details_surname, font=('Arial', 15)).grid(row=3, sticky=W)
    Label(personal_details_screen, text="DOB : " + details_dob, font=('Arial', 15)).grid(row=4, sticky=W)

    Label(personal_details_screen, text="Age : " + details_age, font=('Arial', 15)).grid(row=5, sticky=W)
    Label(personal_details_screen, text="Gender : " + details_gender, font=('Arial', 15)).grid(row=6, sticky=W)

    Label(personal_details_screen, text="Full Address : " + details_full_address, font=('Arial', 15)).grid(row=7, sticky=W)
    Label(personal_details_screen, text="Pin Code : " + details_pin_code, font=('Arial', 15)).grid(row=8, sticky=W)
    Label(personal_details_screen, text="Email Id : " + details_email_id, font=('Arial', 15)).grid(row=9, sticky=W)
    Label(personal_details_screen, text="Mobile No. : " + details_mobile_no, font=('Arial', 15)).grid(row=10, sticky=W)

    Label(personal_details_screen, text="Balance : Rs. " + details_balance, font=('Arial', 15)).grid(row=11, sticky=W)

###########################################################################################################################################################################
def login():
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    login_screen = Toplevel(master)

    login_screen.title('Login')
    login_screen.geometry("400x200")

    Label(login_screen, text="Login to your account", font=('Arial', 15, "bold")).grid(row=0, sticky=N, pady=10)
    Label(login_screen, text="Username", font=('Arial', 20, "bold")).grid(row=1, sticky=W)
    Label(login_screen, text="Password", font=('Arial', 20, "bold")).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font=('Arial', 20, "bold"))
    login_notif.grid(row=4, sticky=N)

    Entry(login_screen, textvariable=temp_login_name).grid(row=1, column=1, padx=5)
    Entry(login_screen, textvariable=temp_login_password, show="*").grid(row=2, column=1, padx=5)

    button4 = Button(login_screen, text="Login", font=('Arial', 20, "bold"), bd=3, relief=RIDGE, fg='blue', bg='black',
                     width=20,
                     command=login_session)
    button4.place(x=200, y=120, width=120, height=25)


img = Image.open('/Users/kunalsingh/Desktop/Python_Internship/Python/Banking_management_system/Image_file/WhatsApp Image 2021-09-15 at 9.52.03 PM.jpeg')
img = img.resize((1700, 600))
img = ImageTk.PhotoImage(img)

Label(master, text="Bank of Kunal", font=('Comic Sans MS', 40, "bold"), fg='red').grid(row=0, sticky=N, pady=10)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

button1 = Button(master, text="Registration", font=('Arial', 20, "bold"), bd=3, relief=RIDGE, fg='blue', bg='red',
                 width=20,
                 command=register)
button1.place(x=775, y=720, width=200, height=50)
button2 = Button(master, text="Login", font=('Arial', 20, "bold"), bd=3, relief=RIDGE, fg='blue', bg='black', width=20,
                 command=login)
button2.place(x=775, y=800, width=200, height=50)

master.mainloop()
