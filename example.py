class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
    def check_balance(self):
        return f"available balance:{self.balance}"
    def credit_ammount(self,c_amount):
        self.balance+=c_amount
        return self.balance
    def debit_amount(self,d_amount):
        try:
            if d_amount<0:
                raise ValueError("Enter a valid amount")
            elif d_amount>self.balance:
                raise ValueError("Insufficient Balance")
            else:
                self.balance-=d_amount
                return f"available balance:{self.balance}"
        except (ValueError,TypeError) as e:
            return str(e)

a1=BankAccount("Nani","A101",5000)
print("Available services:\n 1.check balance\n 2.Deposit\n 3.withdraw")
service=input("How can i help you!: ")
services_list=["check balance","Deposit","withdraw"]
try:
    if service not in services_list:
        raise ValueError("Service Not Available")
    elif service=="check balance":
        print(a1.balance())
    elif service=="Deposit":
        value=int(input("Enter Amount: "))
        print(a1.credit_ammount(value))
    elif service=="withdraw":
            value=int(input("Enter Amount: "))
            print(a1.debit_amount(value))
except (ValueError,TypeError) as e:
    print(str(e))
        