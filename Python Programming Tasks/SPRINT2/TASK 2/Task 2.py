# Basic dictionary 

Person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
Person['email'] = 'alice@example.com'
Person['age'] = 26
del Person['city']
print("Updated Person dictionary:", Person)

# Accessing and modifying 


fruits = {'apple': 10, 'banana': 5, 'cherry': 15}
print("Banana quantity:", fruits['banana'])
fruits['orange'] = 8
fruits['apple'] += 5
del fruits['cherry']
print("Final Fruits dictionary:", fruits)


# Counting word frequency

sentence = "Hello world hello"
words = sentence.lower().split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word frequency:", freq)

# merging two dictionaries  

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key in dict2:
        if key in result:
            result[key] += dict2[key]
        else:
            result[key] = dict2[key]
    return result

dict1 = {'apple': 5, 'banana': 3, 'orange': 7}
dict2 = {'banana': 2, 'orange': 3, 'grape': 4}
print("Merged dictionary:", merge_dicts(dict1, dict2))


# Nested dictionary processing

employees = {
    'E001': {'name': 'Alice', 'department': 'HR', 'salary': 50000},
    'E002': {'name': 'Bob', 'department': 'IT', 'salary': 60000},
    'E003': {'name': 'Charlie', 'department': 'Finance', 'salary': 55000}
}

def get_salary(employee_dict, emp_id):
    return employee_dict[emp_id]['salary']

def increase_salary(employee_dict, percentage):
    for emp in employee_dict:
        employee_dict[emp]['salary'] += employee_dict[emp]['salary'] * percentage // 100

increase_salary(employees, 10)
print("Updated employee details:", employees)


# sorting a dictionary 

marks = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}
sorted_marks = dict(sorted(marks.items(), key=lambda item: item[1], reverse=True))

print(sorted_marks)


# Multiplication Table (1 to 10) using Nested Loops  

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()


# Transpose of a 2D Matrix 



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = []

for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transposed.append(row)

print("Transposed Matrix:", transposed)


# Counting Prime Numbers in a 2D Matrix  



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

matrix = [[2, 4, 5], [7, 9, 11], [13, 16, 19]]
count = 0

for row in matrix:
    for num in row:
        if is_prime(num):
            count += 1

print("Total prime numbers:", count)


# Spiral Order Matrix Traversal  





def spiral_order(matrix):
    spiral = []
    n = len(matrix)
    
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            spiral.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            spiral.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral.append(matrix[i][left])
            left += 1

    return spiral

matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
result = spiral_order(matrix)

print("Spiral Order:", result)



# BMI Calculation  


weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)

print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
else:
    if bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obesity")



# Student graade classification 


score = int(input("Enter student score: "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'

print("Grade:", grade)

if grade in ['A', 'B', 'C']:
    print("Status: Pass")
else:
    print("Status: Fail")



#   Checking Palindromes in a 2D List  


matrix = [
    ["madam", "apple", "racecar"],
    ["level", "hello", "civic"],
    ["world", "deified", "rotor"]
]

for row in matrix:
    for word in row:
        if word == word[::-1]:
            print(word, "is a palindrome")
        else:
            print(word, "is not a palindrome")


#  Multiplication Table with Even Numbers Only  


for i in range(1, 11):
    for j in range(1, 11):
        product = i * j
        if product % 2 == 0:
            print(product, end=" ")
        else:
            print(" ", end=" ")
    print()
