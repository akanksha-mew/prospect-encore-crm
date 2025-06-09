import common
import os


# __________________________PROSPECT__ENCORE__ANALYSIS______________________
def main():
    while True:
        os.system("cls")
        print(" Welcome to Prospect Encore Analysis ".center(50, '~'))
        print("\nDo you want to Login : \n[1] Yes \t[2] No")
        ch = int(input("\nEnter your choice : "))

        if ch == 1:
            common.login()
        elif ch == 2:
            print("Exit !!!")
            exit(0)
        else:
            print("Invalid Input...TRY AGAIN !!!\n")


if __name__ == "__main__":
    main()
