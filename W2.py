# Task1

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_a = list(map(lambda x: x**2, a)) 
print(squared_a)

a_sum = 0
for x in a:
    a_sum += x**2
print(a_sum)


# Task2
def operations():
    add = lambda x, y: x + y
    subtract = lambda x, y: x - y
    multiply = lambda x, y: x * y
    divide = lambda x, y: x / y if y != 0 else "Error"

    while True:
        choice = input("Number (1,2,3,4,5): ")
        if choice == '5':
            print("Exit")
            break
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        else:
            print("Choice")

operations()



# Task3
data = [
    {"name": "Orkhan", "age": 25, "salary": 700},
    {"name": "Ali", "age": 30, "salary": 1800},
    {"name": "Veli", "age": 35, "salary": 500},
    {"name": "Fidan", "age": 28, "salary": 1200},
    {"name": "Zeynab", "age": 40, "salary": 3000},
    {"name": "Flora", "age": 32, "salary": 5000},
    {"name": "Kerim", "age": 19, "salary": 300},
    {"name": "Flora", "age": 32, "salary": 5000},
    {"name": "Adil", "age": 49, "salary": 1660},
    {"name": "Asmar", "age": 22, "salary": 1200}
]
# Filter
filtered = list(filter(lambda x: x["age"] >= 30, data))

# Mean Salary
mean = sum(map(lambda x: x["salary"], data)) / len(data)

# Lowercase1
def to_lowercase(data):
    lowercase = map(lambda x: x["name"].lower(), data)
    return lowercase
fiters = to_lowercase(data)
# Lowercase 2
lowercase = list(map(lambda x: {**x, "name": x["name"].lower()}, data))

# Prints 
print('='*80)

print("Filtered  (Age >= 30):", filtered)
print('='*80)

print("Mean Salary:", mean)
print('='*80)

print(" Lowercase :", lowercase)
print('='*80)

print(fiters)