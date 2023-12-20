# Task2
# def operations():
#     add = lambda x, y: x + y
#     subtract = lambda x, y: x - y
#     multiply = lambda x, y: x * y
#     divide = lambda x, y: x / y if y != 0 else "Error"

#     while True:
#         choice = input("Number (1,2,3,4,5): ")
#         if choice == '5':
#             print("Exit")
#             break
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         if choice == '1':
#             print("Result:", add(num1, num2))
#         elif choice == '2':
#             print("Result:", subtract(num1, num2))
#         elif choice == '3':
#             print("Result:", multiply(num1, num2))
#         elif choice == '4':
#             print("Result:", divide(num1, num2))
#         else:
#             print("Choice")

# operations()

def cal():
    pulus = lambda x, y: x+y
    cixma = lambda x, y: x-y
    vurma = lambda x, y: x * y
    bolme = lambda x, y: x/y if  y != 0 else 'eror'
    
    while True:
        number_chooose=input('choose: ')
        if number_chooose == '5':
            print('EXIT')
            break
        
        
        num1 = float(input('num1: '))
        num2 = float(input('num2: '))
        
        if number_chooose =='1':
            print('num',pulus(num1,num2))
        elif number_chooose == '2':
            print('num',cixma(num1,num2))
        elif number_chooose == '3':
            print('num',bolme(num1,num2))
        elif number_chooose == '4':
            print('num',vurma(num1,num2))
        else:
            print('choise')
            
            
cal()