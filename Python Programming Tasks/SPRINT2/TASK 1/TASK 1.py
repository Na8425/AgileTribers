# using return statement

def cub_number(num):
    return num ** 3
num = int(input("Enter a Number: "))
result=cub_number(num)
print(result)

# using break in a loop
while True :
    num = int(input("Enter a Number: "))
    if num < 0 :
        print("Given number in Negative")
        break
cube = num ** 3
print(cube)

# using continue 
print("Even Numbers from 1 to 20 :")
for i in range(1,21) :
    if (i % 2 !=0) :
        continue
    print(i)


# using continue and break 

sum = 0
while True :
    num=int(input("Enter a Number : "))
    if num < 0 :
        continue
    if num == 0 :
        break
    sum+=num
print("Sum is : ",sum)

# local scope in function

def square_number(n) :
    result = n*2 
    print("Square inside Function : ",result)

square_number(3)

print("Trying to access the variable from outside the function")
print(result)


# Global keyword 


counter = 0

def increment_counter():
    global counter
    counter += 1
    print("Counter:", counter)

increment_counter()
increment_counter()
increment_counter()




# Tuple 



fruits = ("apple", "banana", "cherry")
print("Second fruit:", fruits[1])
fruits_list = list(fruits)
fruits_list[1] = "orange"
fruits = tuple(fruits_list)

# working with Set 

set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}

print("Union: ",set1 | set2)
print("Intersection: ",set1&set2)
print("Difference: ",set1 - set2)


set1.add(9)
print("Set1 after adding Number",set1)

set2.remove(7)
print("set2 after removing the number: ",set2)

num=4
if num in set1 :
    print(num," is present in set")
else :
    print("Not present")    


# Tuple and set operations


my_tuple = (10, 20, 30, 40, 50)
print("Third element of tuple:", my_tuple[2])
my_set = set(my_tuple)
my_set.add(60)
print("Updated set:", my_set)


# List to set operations 



number_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_set = set(number_list)
another_set = {5, 6, 7, 8, 9}
print("Original list with duplicates:", number_list)
print("Unique elements : ", unique_set)
print("Common elements :", unique_set & another_set)
print("All elements :", unique_set | another_set)


# Working with Tuples, Sets, and Lists 



num_list = [10, 20, 30, 40, 50]
num_list.append(60)
print("Updated list:", num_list)
num_tuple = tuple(num_list)
print("Tuple:", num_tuple)
num_set = set(num_list)
print("Set with unique values:", num_set)


# Global variable VS Local variable
x = 10

def modify_global():
    global x
    x = x + 5
    print("Inside modify_global(), x =", x)

def local_scope_demo():
    y = 20
    print("Inside local_scope_demo(), y =", y)


modify_global()
local_scope_demo()


print("Outside functions, x =", x)

# Try to access local variable 'y' outside its function
print("Trying to access y outside local_scope_demo():")
print(y)  # This will cause an error
