
unit = input("Enter what you want to convert to..F or C")


if(unit=="C"):
    fahrenheitValue = float(input("enter temperature in Fahrenheit"))
    celcius = (fahrenheitValue - 32) * 5 / 9
    print(celcius)

elif(unit =="F"):
    celciusValue = float(input("enter temperature in Celcius"))
    fahrenheit = (celciusValue * 9.0/5.0) + 32.0;
    print(fahrenheit)
else:
    print("enter the right Unit. K or C")


'''
num =12
evenCount = 0
oddCount = 0
for i in range(num):
    if i %2 ==0:
        evenCount+=1
        

    else:
        oddCount+=1
        print(f'the number of odd numbers are {oddCount}')
        
print(f'number of even numbers are {evenCount}')
print(f'the number of odd numbers are {oddCount}')
'''

'''
letter = input("enter the word")

numCount=0
letterCount=0
for i in letter:
    if(i>="0" and i<="9"):
        numCount+=1

    elif(i>="a" and i <="z"):
        letterCount +=1



print(letterCount)
print(numCount)
'''
'''
print("Password must have At least 1 letter between [a-z] and 1 letter between [A-Z].\n"
      "At least 1 number between [0-9].\n"
      "At least 1 character from [$#@]."
      "")

length = False
upper = False
number = False
symbol = ["$","%","&","@"]
digit = False
password = input("enter your password: ")

'''
'''
if length <=6 and length >=16:
    length =True

    for i in password:
        if password.isupper():
            upper=True

        if password.isdigit():
            digit = True


if length and upper and digit:
    print("password Valid")

else:
    print("password isnt valid")
'''