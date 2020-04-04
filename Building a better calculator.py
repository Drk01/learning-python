num1 = float(input('Insert the first number: '))
op = input('Insert the operation: ')
num2 = float(input('Insert the second number: '))

if op == "+":
    print('Addition result is: ' + str(num1 + num2))
elif op == "-":
    print('Subtraction result is: ' + str(num1 - num2))
elif op == "/":
    print('Division result is: ' + str(num1 / num2))
else:
    print('Multiplication result is: ' + str(num1 * num2))
