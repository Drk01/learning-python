def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print('Num1 is bigger than others numbers')
    elif num2>=num1 and num2>=num3:
        print('Num2 is bigger than others numbers')
    else:
        print('Num3 is bigger than others numbers')

max_num(1,2,3)