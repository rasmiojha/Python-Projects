def get_user_input():
    operator = input('Please enter the operator:(+ , - , * , /)')
    num1 = int(input('Enter the first Number:'))
    num2 = int(input('Enter the Second Number:'))
    return operator,num1,num2

def calculate(operator ,num1,num2):
    if operator == '+':
        sum = ( round(num1 + num2))
        print(sum)
    elif operator == '-':
        minus=(round(num1 - num2))
        print(minus)
    elif operator == '*':
        mul=(round(num1 * num2))
        print(mul)
    elif operator == '/':
        devision=(round(num1 / num2))
        print(devision)
    else:
        print('Invalid Operator')

operator,num1,num2=get_user_input()
calculate(operator ,num1,num2)