'''first =int(input("enter the first number"))
another_first =int(input("enter the changed first number"))

second = float(input("enter the second number"))

third = int(input("enter the third number"))

add = first+second+third
div = second/third
remainder = first%third


diff = another_first-second


print(add)
print(div)
print(remainder)
print(diff)
'''
import tkinter

'''

list1= [2,3,5,1,106,'ray',True]

list2 = ['sun', False, 30,21.6]
list2.append('karl')
list2.pop()
list2.insert(1,"Emma")
print(list2)

list2.remove(False)


print(list2)

list3 = list1.copy()

print(list3)

# adding apple to list3



print("the final results")

list3.append("apple")
print(list1)
print(list3)

#appending using indexing

list3 = list1[-2:]
print(list3)

list4 = [1,2,3,4,5,6,7,8,9,10]
odds= list4[0:10:2]
even= list4[1:10:2]

print(even)
print(odds)
'''

'''
fruits = ['Banana', 'Pineapple', 'Orange', 'Mango']

fruits.insert(3,"Watermelon")
fruits.pop()
fruits.insert(0, "Cucumber")
print(fruits)

fruits2 = fruits[0:2]
print(fruits2)


list1 = [1,2,3,4,5]
list3= [1, [5, 2], [[3, 9, 7], 11, 8], 10]
tuple = tuple(list3)
print(tuple[2][0][0])
'''

'''

#number 1 checking if a pythoN list is empty or not

myList = []

if( len(myList)== 0):
    print("list is empty")

else:
    print("list is not empty")


#number 2: cloning a list

mylist1 = ["Abuja", "Benue", "calabar", "Delta","Europe"]

mylist2 = mylist1.copy()

print(mylist2)

#number3:
sampleList = ["Red","green","White","Black","Pink","Yellow"]
sampleList.pop(0)
sampleList.pop(3)

try:
    sampleList.pop(4)
except Exception as e:
    print("error")


print(sampleList)

sampleList = ["Red","green","White","Black","Pink","Yellow"]
'''

'''
car={
    "brand": "ford",
    "name": "Karl",
    "year": "2022"
}

print(car)

print(car["brand"])

print(car.get("name"))
'''

'''
for i in range(1,5):
    num = int(input("enter numbers"))
    squares = int(num*num)
    print("the square of ",num,"is", squares)
    for x in range(1):
        num = num
        square = num ** 2
        if square % 2 != 0:
            print(square, " is an odd number")
'''

'''
numList = []
oddList = []

for i in range(4):
    num = int(input("Enter a number: "))
    numList.append(num)
    print(numList)

squares = []

for x in numList:
    result=x**2
    squares.append(result)

print(squares)
'''


#number 2
'''
setsOfFruits = {"apple", "banana", "cherry"}

for i in setsOfFruits:
    item = input("input what you are searching for")
    if item not in i:
        print("the item you are looking for is not inside the list/set not inside")
        message= input("do you want to add what you were looking for to the list? yes or no?")
        if message == 'yes':
            setsOfFruits.add(item)
            print(setsOfFruits)
        elif message == 'no':
            print("okay. Once again the item is not in the list")

        else:
            print("please enter either yes or no")
        break

    else:
        print(f'{item} is inside the list/set')
        break
'''

#number 3
'''
numbers = {}

for i in range(1,16):

    squares = i*i

    numbers[i]= squares
print(numbers)
'''

#number 4



#Number5
'''

for i in range(200,401):
    if i%7==0 and i%5==0:
        print(i)
'''
'''
#number 6
for num in range(1, 51):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
'''

#number 7
'''

rows = 5
for i in range(0,rows):
    for j in range(0,i+1):
        print("*")
'''




'''
number = int(input("enter the number you want it's multiplication number "))
for i in range(1,12+1):
    print(f'{number} * {i} = {number*i}')
'''
'''
while True:
    number = int(input("enter the number you want it's multiplication number "))
    for i in range(1, 12 + 1):
        print(f'{number} * {i} = {number * i}')
    print("\n")
    '''
'''
day = input("enter day")



month = input("enter the month")
year = input("enter the year")

if day >=1 and day <=30 and :
    
message =  f'your birthday is {day}-- {month}-- {year}'
print(message)
'''
'''
day = int(input("enter day: "))
month = int(input("enter the month: "))
year = int(input("enter the year: "))


try:
    if (day >=1 and day <=30) and (month >=1 and month <=12):
        message = f"the next day is {day+1}-{month}-{year}"
        print(message)


except ValueError:
    print("input the right date")

'''


fruits = ['banana', 'orange', 'apple','orange']

for x in fruits:
    print(x)