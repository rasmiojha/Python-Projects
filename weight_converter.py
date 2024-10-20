def get_user_input():
    unit = input('Enter the uint:(lbs/kg)').strip()
    weight = float(input('Enter your weight :'))
    return unit,weight

def convert(unit,weight):
    if unit == 'kg':
        weight = round((weight * 2.2046226218),3)
        # print(f'Yuor weight in Pound is:{lbs}')
        return weight
    elif unit == 'lbs':
        print('Your weight in Kg is:', round(weight/2.2046226218,3))
        weight = round((weight / 2.2046226218),3)
        return weight
    else:
        print(f'Invalid Unit! {unit}')
        return None

unit,weight = get_user_input()
# weight = get_user_input()
convert(unit,weight)
print(f'Yuor weight in is:',convert(weight))