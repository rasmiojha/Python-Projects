class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print(amount,"is debited from your account")
        print("Available balnce is ",self.get_balance())
    #credit method
    def credit(self,amount):
        self.balance += amount
        print(amount,"is credteed in your account")
        print("Available balance is ",self.get_balance())
    #show balance method 
    def get_balance(self):
        return self.balance

acc1 = Account(100000,1234)
acc1.debit(1000)
acc1.credit(20000) 

acc2=Account(7500000,1890765432)
acc2.debit(5000000)
acc2.credit(4500000)
# acc1 = credit(500)
print(acc1.balance)
# print(acc1.account_no)

# patient_name='John Smith'
# patient_age=20
# is_new_patient=True 
# print(patient_name)
# print(patient_age)
# print(is_new_patient)




