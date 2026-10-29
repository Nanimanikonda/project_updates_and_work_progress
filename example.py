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
 
       
a1=BankAccount("nani","A101",2000)
print(a1.check_balance())
print(a1.credit_ammount(1000))
print(a1.check_balance())
print(a1.debit_amount(1000))
print(a1.check_balance())
print(a1.debit_amount(3000))    