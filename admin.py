import pencoreanalysis
import saleanalysis
import common
import os


def admin_menu(user_name):
    while True:
        os.system("cls")
        print('-' * 100)
        print("\n\tMain Menu : \n\t\t[1] Create User Account \n\t\t[2] View All User(Employees) "
              "\n\t\t[3] View All Prospect \n\t\t[4] Search Prospect \n\t\t[5] Change Password  "
              "\n\t\t[6] Data Analysis \n\t\t[7] Activate / Deactivate \n\t\t[8] Sign Out ")
        print('-' * 100)
        ch = int(input("Enter your Choice : "))
        print('-' * 100)

        if ch == 1:
            print("\n[1] Monitor \t[2] Admin")
            opt = int(input("Enter your Choice : "))
            if opt == 1:
                common.create_user("Monitor")
            elif opt == 2:
                common.create_user("Admin")
            input("\nPress any key to Continue")

        elif ch == 2:
            common.view_all_employees()
            input("\nPress any key to Continue")

        elif ch == 3:
            common.view_all_prospects()
            input("\nPress any key to Continue")

        elif ch == 4:
            common.search_prospect()
            input("\nPress any key to Continue")

        elif ch == 5:
            print("\n[1] Self \t[2] Other")
            opt = int(input("Enter your Choice : "))
            if opt == 1:
                common.self_password(user_name)
            elif opt == 2:
                common.others_password()
            input("\nPress any key to Continue")

        elif ch == 6:
            saleanalysis.plot_menu()
            input("\nPress any key to Continue")

        elif ch == 7:
            common.activate_deactivate()
            input("\nPress any key to Continue")

        elif ch == 8:
            return pencoreanalysis.main()

        else:
            print("Invalid Choice...TRY AGAIN !!!")
            input("\nPress any key to Continue")

