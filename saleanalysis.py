import os
import common
import numpy as np
import plots
from matplotlib import pyplot as plt


def plot_menu():
    while True:
        os.system("cls")
        print('-' * 100)
        print("\n\tPlot Menu : \n\t\t[1] Pie Plot \n\t\t[2] Multi Plot \n\t\t[3] Exit")
        print('-' * 100)
        ch = int(input("Enter your Choice : "))
        print('-' * 100)

        if ch == 1:
            print("\n[1] According to Car Model \t[2] According to Car Color \t[3] According to Sale Count in Years")
            opt = int(input("Enter your Choice : "))

            if opt == 1:
                plots.pie_plt1()
                input("\nPress any key to Continue")

            elif opt == 2:
                plots.pie_plt2()
                input("\nPress any key to Continue")

            elif opt == 3:
                plots.pie_plt3()
                input("\nPress any key to Continue")

        elif ch == 2:
            print("\n[1] Bar Plot \t[2] Line Plot")
            opt = int(input("Enter your Choice : "))
            if opt == 1:
                print("\n[1] Individual Data Plot \t[2] Combined Data Plot")
                ch = int(input("Enter your Choice : "))
                if ch == 1:
                    plots.bar_plt1()
                    input("\nPress any key to Continue")
                elif ch == 2:
                    plots.bar_plt2()
                    input("\nPress any key to Continue")

            elif opt == 2:
                plots.line_plt()
                input("\nPress any key to Continue")

        elif ch == 3:
            break

        else:
            print("Invalid Choice...TRY AGAIN !!!")
            input("\nPress any key to Continue")
