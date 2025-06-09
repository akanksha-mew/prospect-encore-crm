import pymysql as db
import monitor
import admin

conn = db.connect("localhost", "root", "", "prospencore")
cur = conn.cursor()


# login function________________________________________________________________________________________________________
def login():
    u_name = input("\nEnter Username : ")
    pwd = input("Enter password : ")

    qry = "select user_type from employees where user_name = %s and user_pass = %s and status = 'activated' "
    cur.execute(qry, (u_name, pwd))
    rs = cur.fetchall()

    if cur.rowcount == 1:
        if rs[0][0] == "Monitor":
            qry = "select full_name from employees where user_name = '" + u_name + "'"
            cur.execute(qry)
            rs = cur.fetchall()
            for i in rs:
                for j in i:
                    print("\nWelcome " + j)
            monitor.monitor_menu(u_name)

        elif rs[0][0] == "Admin":
            qry = "select full_name from employees where user_name = '" + u_name + "'"
            cur.execute(qry)
            rs = cur.fetchall()
            for i in rs:
                for j in i:
                    print("\nWelcome " + j)
            admin.admin_menu(u_name)
    else:
        print("\nInvalid Username or Password !!!\n")


# function for inserting new prospect___________________________________________________________________________________
def insert_prosp():
    pid = input("Enter Prospect Id : ")
    pname = input("Enter Prospect Name : ")
    pphone = input("Enter Prospect Phone : ")
    padd = input("Enter Prospect Address : ")
    pcarmodel = input("Enter Car Model : ")
    pcarcol = input("Enter Car Colour : ")
    vdate = input("Enter Visit date : ")
    vday = input("Enter Visit Day : ")
    bamnt = input("Enter Booking Amount : ")
    gen = input("Enter Gender (M/F) : ")
    igrp = input("Enter Income Group (H/L/M) : ")
    prior = input("Enter Priority (High/Low/Medium) : ")
    pmode = input("Enter Purchase Mode (Cash/Installment) : ")

    qry = "insert into prospect values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(qry, (pid, pname, pphone, padd, pcarmodel, pcarcol, vdate, vday, bamnt, gen, igrp, prior, pmode))
    conn.commit()


# function for viewing all data of prospect_____________________________________________________________________________
def view_all_prospects():
    qry = "select * from prospect"
    cur.execute(qry)
    rs = cur.fetchall()
    print("\nProsp_id\t\tProsp_name\t\t\tProsp_phone\t\t\tProsp_address\t\tInterested_model\tInterested_color"
          "\tVisit_date\t\t\tVisit_day\t\t\tBooking_amount\t\t\tGender\t\tIncome_group\t\tPriority\t\tPurchase_mode")
    print('-' * 300)

    for i in rs:
        for j in i:
            print(j, end="\t\t\t\t")
        print()


# function for update___________________________________________________________________________________________________
def update_prospect():
    print("\n[1] Phone \t[2] Model \t[3] Color \t[4] Priority")
    choice = int(input("\nEnter your Choice : "))
    print('-' * 100)
    pId = input("Enter Prospect Id you want to Update : ")
    print('-' * 100)

    if choice == 1:
        p_phn = input("Enter New Phone No. : ")
        qry = "update prospect set Prosp_phone=%s where Prosp_id = '" + pId + "'"
        cur.execute(qry, (p_phn,))
        conn.commit()

    elif choice == 2:
        i_mod = input("Enter New Model : ")
        qry = "update prospect set Interested_model=%s where Prosp_id = '" + pId + "'"
        cur.execute(qry, (i_mod,))
        conn.commit()

    elif choice == 3:
        i_col = input("Enter New Color : ")
        qry = "update prospect set Interested_color=%s where Prosp_id = '" + pId + "'"
        cur.execute(qry, (i_col,))
        conn.commit()

    elif choice == 4:
        prior = input("Enter New Priority (High/Low/Medium) : ")
        qry = "update prospect set Priority=%s where Prosp_id = '" + pId + "'"
        cur.execute(qry, (prior,))
        conn.commit()

    else:
        print("Invalid Input...TRY AGAIN !!!\n")


# function for viewing details__________________________________________________________________________________________
def view_details(features):
    qry = "select * from prospect where" + features
    cur.execute(qry)
    rs = cur.fetchall()

    if cur.rowcount > 0:
        print("\nProsp_id\t\tProsp_name\t\t\tProsp_phone\t\t\tProsp_address\t\tInterested_model\tInterested_color"
              "\tVisit_date\t\t\tVisit_day\t\t\tBooking_amount\t\t\tGender\t\tIncome_group\t\tPriority\t\tPurchase_mode")
        print('-' * 300)

        for i in rs:
            for j in i:
                print(str(j), end="\t\t\t\t")
            print()
    else:
        print("\nRecord NOT Found !!!")


# function for searching prospects______________________________________________________________________________________
def search_prospect():
        print("\n[1] By Priority \t[2] By Prospect Id")
        choice = int(input("\nEnter your Choice : "))
        print('-' * 100)

        if choice == 1:
            print("\n\t[1] High \t[2] Low \t[3] Medium")
            option = int(input("\nEnter your Choice : "))
            print('-' * 100)

            if option == 1:
                view_details(" Priority = 'high' ")

            elif option == 2:
                view_details(" Priority = 'low' ")

            elif option == 3:
                view_details(" Priority = 'medium' ")

            else:
                print("Invalid Choice")

        elif choice == 2:
            pid = input("Enter Prospect Id you want to search : ")
            view_details(" Prosp_id = '" + pid + "'")


# function to change self password______________________________________________________________________________________
def self_password(user_name):
    pwd = input("Enter New Password : ")
    re_pwd = input("Retype Password : ")

    if pwd == re_pwd:
        qry = "update employees set User_pass = %s where User_name = '" + user_name + "'"
        cur.execute(qry, (pwd,))
        conn.commit()
    else:
        print("\nPassword Doesn't Match !!!")


# function to change others password____________________________________________________________________________________
def others_password():
    u_name = input("Enter User Name : ")
    pwd = input("Enter New Password : ")
    re_pwd = input("Retype Password : ")

    if pwd == re_pwd:
        qry = "update employees set User_pass = %s where User_name = '" + u_name + "'"
        cur.execute(qry, (pwd,))
        conn.commit()
    else:
        print("\nPassword Doesn't Match !!!")


# function for viewing all data of employees____________________________________________________________________________
def view_all_employees():
    qry = "select * from employees"
    cur.execute(qry)
    rs = cur.fetchall()
    print("User_name\t\tUser_pass\t\tUser_Type\t\tFullname\t\tGender\t\t\tPhone\t\t\t\tEmail\t\t\t\t\tStatus")
    print('-' * 150)

    for i in rs:
        for j in i:
            print(j, end="\t\t\t")
        print()


# function for creating user account____________________________________________________________________________________
def create_user(user_type):
    u_name = input("Enter User Name : ")
    u_pass = input("Enter User Password : ")
    u_type = user_type
    fullname = input("Enter User Fullname : ")
    gender = input("Enter User Gender : ")
    phone = input("Enter User Phone : ")
    email = input("Enter User Email : ")
    status = input("Enter User Status (Activated/Deactivated) : ")

    qry = "insert into employees values(%s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(qry, (u_name, u_pass, u_type, fullname, gender, phone, email, status))
    conn.commit()


# function for activating deactivating account__________________________________________________________________________
def activate_deactivate():
    print("\n[1] Activate \t[2] Deactivate")
    ch = int(input("Enter your Choice : "))
    if ch == 1:
        u_name = input("Enter User Name : ")

        qry = "update employees set Status = 'Activated' where User_name = '" + u_name + "'"
        cur.execute(qry)
        conn.commit()

    elif ch == 2:
        u_name = input("Enter User Name : ")

        qry = "update employees set Status = 'Deactivated' where User_name = '" + u_name + "'"
        cur.execute(qry)
        conn.commit()


