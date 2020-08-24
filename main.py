import sys
import SqlConnection
def menu():
    quit = 0;
    while(quit==0):
        print("*****MENU OPTIONS*****")

        choice = input("""
                              A: פונקציה שיוצרת שיחה חדשה.
                              B: פונקציה שמציגה את כל השיחות של לקוח לפי מספר טלפון.
                              C: פונקציה שמציגה את הסכום לתשלום של לקוח לכל הקווים שלו לפי ת"ז.
                              D: פונקציה שבודקת את מספר הקווים לכל מסלול.
                              E: פונקציה שבודקת קו האם חרג ממספר הדקות המותר.
                              F: Quit/Log Out
                              
                              Please enter your choice: """)

        if choice == "A" or choice == "a" or choice=="ש":
            SqlConnection.addTalking();
            print("succeed")
        elif choice == "B" or choice == "b" or choice=="נ":
            phone=input("enter phone: ")
            SqlConnection.getTalkingByPhone(phone);
            print("succeed")
        elif choice == "C" or choice == "c" or choice=="ב":
            yourCode=input("enter your code: ")
            SqlConnection.getcost(yourCode);
            print("succeed")
        elif choice == "D" or choice == "d" or choice=="ג":
            SqlConnection.getCountLinesOfAnyRoute()
            print("succeed")
        elif choice == "E" or choice == "e" or choice=="ק":
            phone = input("enter phone: ")
            SqlConnection.exceptionCheck(phone)
            print("succeed")
        elif choice == "F" or choice == "f" or choice=="כ":
            print("יציאה                              ")
            quit = 1;
            sys.exit
        else:
            print("You must only select either A,B,C, or D.")
menu()