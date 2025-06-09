import pencoreanalysis
import saleanalysis
import common
import os


def monitor_menu(user_name):
    while True:
        os.system("cls")
        print('-' * 100)
        print("\n\tMain Menu : \n\t\t[1] Add New Prospect \n\t\t[2] View All Prospect "
              "\n\t\t[3] Update Prospect \n\t\t[4] Search Prospect \n\t\t[5] Change Own Password  "
              "\n\t\t[6] Data Analysis \n\t\t[7] Sign Out ")
        print('-' * 100)
        ch = int(input("Enter your Choice : "))
        print('-' * 100)

        if ch == 1:
            common.insert_prosp()
            input("\nPress any key to Continue")

        elif ch == 2:
            common.view_all_prospects()
            input("\nPress any key to Continue")

        elif ch == 3:
            common.update_prospect()
            input("\nPress any key to Continue")

        elif ch == 4:
            common.search_prospect()
            input("\nPress any key to Continue")

        elif ch == 5:
            common.self_password(user_name)
            input("\nPress any key to Continue")

        elif ch == 6:
            saleanalysis.plot_menu()
            input("\nPress any key to Continue")

        elif ch == 7:
            return pencoreanalysis.main()
        else:
            print("Invalid Choice...TRY AGAIN !!!")
            input("\nPress any key to Continue")



