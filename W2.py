#Task1
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_a = list(map(lambda x: x**2, a)) 
# print(squared_a)

# a_sum = 0
# for x in a:
#     a_sum += x**2
# print(a_sum)


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
