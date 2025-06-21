# check a number is a positive or not

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Check whether a number is even or odd

num1 = int(input("Enter a number: "))
if num1 % 2 ==0 :
    print("EVEN")
else  :
    print("ODD")

#Compare two numbers and display which is greater or if they are equal

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both numbers are equal")


#Print numbers from 1 to 10 using a for loop

for i in range(1,11)     :
    print(i)

# Print even numbers from 1 to 20
for i in range(2,21,2) :
    print(i)

# Print odd numbers from 1 to 20

for i in range (1,21,2)    :
    print(i)

#Sum of numbers from 1 to 100


total = 0
for i in range(1, 101):
    total += i
print("Sum is:", total)


# Check whether a character is a vowel or consonant

ch=input("Enter a Character: ").lower()
if ch in "aeiou" :
    print("It is a Vowel")
else :
    print("Not a vowel")

#  Print the greatest of three numbers

a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)

#  Print the first 10 natural numbers

for i in range (1,11)  :
    print(i)

#  Check if the first and last numbers in a list are the same

numbers=[10,20,30,40,50]
if numbers[0] == numbers[-1] :
    print("First and Last Numbers are same")
else :
    print("Firstand LAst are Not same")


#  Print numbers divisible by 5 from a given list

number=[10,5,4,54,20,100]
for num in number :
    if num % 5 ==0 :
        print(num)

# Identify if a given year is a leap year

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Print numbers from 1 to 25 excluding multiples of 5

for i in range (1,26) :
    if i % 5 != 0 :
        print(i) 

# Separate positive and negative numbers from a list

list_a=[1,5,6,7,-5,-8,-9,-10]
positives=[]
negatives=[]
for num in list_a :
    if num >= 0 :
        positives.append(num)
    else :
        negatives.append(num)
print("Positve Numbers: ",positives)        
print("Negative Numbers: ",negatives)


# Draw patterns using nested loops 
#triangle
row=5
for i in range(1,row+1):
    for j in range(i) :
        print("* ",end=" ")
    print() 


#Square


rows = 4
for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()


# Grade calculator based on input marks using if-elif-else 

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F (Fail)")


# Calculate the factorial of each element in a list
nume=[3,4,5]
for num in nume :
    fact=1
    for i in range(1,num+1) :
        fact=fact*i
print("Factorial of ", num,"is ", fact)    

# IMPLEMENT FIZZBUZZ

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

