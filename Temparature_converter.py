unit = input('Enter the unit?(Celsius/Fahrenheit)').strip()
Temp = float(input('Enter the temparature to be converted:'))


if unit == 'Celsius':
    Temp = (Temp * (9/5)) + 32
    print(f'Temparature in Celcilus is {Temp}\N{DEGREE SIGN}')
elif unit == 'Fahrenhite':
    Temp = (Temp - 32)*5/9
    print(f'Temparature in Fahrenhite is {Temp}')
else:
    print(f'Invalid Unit!{unit}')