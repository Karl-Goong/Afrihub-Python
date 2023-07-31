def add(num1, num2):
    result = num1 + num2
    print(result)


def sub(num1, num2):
    result = num1 - num2
    print(result)


def div(num1, num2):
    result = num1 / num2
    print(result)


def mul(num1, num2):
    result = num1 * num2
    print(result)


print("Welcome to the Basic Calculator: \n")


user_input = input("what do you want to do \n "
      "1.add \n "
      "2.subtract \n "
      "3.multiple \n "
      "4.divide")


if user_input == "1":
    num1 = int(input("Enter the first number"))
    num2 = int(input("enter the second number"))

    add(num1,num2)

elif user_input == "2":
    print("format = first number - second number")
    num1 = int(input("Enter the first number"))
    num2 = int(input("enter the second number"))

    sub(num1,num2)


elif user_input == "3":
    print("format = first number divided by second number")
    num1 = int(input("Enter the first number"))
    num2 = int(input("enter the second number"))

    div(num1,num2)



elif user_input == "4":

    num1 = int(input("Enter the first number"))
    num2 = int(input("enter the second number"))

    sub(num1,num2)

