# def get_positive_input(user_input):
#     while True:
#         try:
#             value = float(input(user_input)).strip()
#             if value<=0:
#                 print(f"{user_input.split(':')[0]} can't be less than or equals to Zero")
#             else:
#                 return value
#         except ValueError:
#             print("Invalid Input! Please enter a numeric value.")

# def calculate_compound_interest(princepal,rate,time):
#     return princepal * pow((1+ rate/100),time)

# def main():
#     princepal = get_positive_input("Enter Princepal Amount : ")
#     rate = get_positive_input("Enter Rate of Interest")
#     time = get_positive_input("Enter Time Period")
#     total = calculate_compound_interest(princepal,rate,time)
#     print(f"The total balance after {time} year/s is {total:.2f}")

# if __name__ == "__main__":
#     main()

def get_positive_principal_input(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print(f"{prompt.split(':')[0]} can't be less than or equal to zero")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_positive_input(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value < 0:
                print(f"{prompt.split(':')[0]} can't be less than or equal to zero")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")            

def calculate_total(principal, rate, time):
    return principal * pow((1 + rate / 100), time)

def main():
    principal = get_positive_principal_input("Enter the Principal Amount: ")
    rate = get_positive_input("Enter the rate of interest: ")
    time = get_positive_input("Enter the time (in years): ")

    total = calculate_total(principal, rate, time)
    print(f"The total balance after {time} year/s is ${total:.2f}")

if __name__ == "__main__":
    main()
