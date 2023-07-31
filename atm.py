balance = 10000

while True:
    print("Welcome To Access Bank\n"
          "1.Deposit Money\n"
          "2.Withdraw\n"
          "3. Check Balance\n"
          "4.Exit\n")

    userInput = input("What operation do you want to perform: ")
    if userInput== "1":
        print("DEPOSIT!.")
        deposit =int(input("enter money: "))
        print("enter a figure above #1000")

        balance =  deposit+balance
        print(f"you have successfully deposited  #{deposit}")

    elif userInput == "2":
        while True:
            print("WITHDRAW")
            withdraw = int(input("How much do you want to withdraw: "))
            if balance <withdraw:
                print("insufficient Funds")
            else:
                balance= balance- withdraw
                print("Withdrawal Successful")
                break

    elif userInput == "3":
        print(f"your Balance is {balance}")

    elif userInput == "4":
        print("Thank you for Banking with us")
        break

    else:
        print("enter a valid choice")