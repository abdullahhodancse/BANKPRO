import random

class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        

class Customer(User):
    def __init__(self, name, email, address, account_type, balance):
        super().__init__(name, email, address)
        self.account_type = account_type
        self.balance = balance
        self.auto_number = self.auto_account_number()
        self.transaction_history = []
        self.loan_count = 0

    def auto_account_number(self):
        return ''.join(str(random.randint(0, 9)) for _ in range(8))

    def deposit(self, amount):
        print(">>>>>>Deposit Your Money<<<<<<<\n")
        if amount < 50:
            print("You cannot deposit below 50 tk")
        else:
            self.balance += amount
            print(f'You deposited {amount}. Now your balance is={self.balance} taka')
            self.transaction_history.append(f'You Deposited {amount}... Now Your Balance is {self.balance}')

    def withdraw(self, withdraw_amount):
        print("<<<<<<Please withdraw your money>>>>>>>\n")
        if withdraw_amount < 50:
            print("You cannot withdraw less than 50 tk") 
        elif withdraw_amount > self.balance:
            print("Sorry, Insufficient Balance")
        else:
            print("Here is your money")
            self.balance -= withdraw_amount 
            print(f'You withdrew {withdraw_amount} taka. Your current balance is={self.balance} taka')
            self.transaction_history.append(f'You withdrew {withdraw_amount}... Now Your Balance is {self.balance}')   
    
    def take_loan(self, loan_amount):
        print("<<<<<<Loan>>>>>>\n")
        if self.loan_count < 2:
            self.balance += loan_amount
            self.loan_count += 1
            print(f'Here is your loan of {loan_amount} taka. Now your balance is {self.balance}')
            self.transaction_history.append(f'You took {loan_amount} taka loan and Your balance is {self.balance}')
        else:
            print("You cannot take another loan")    

    def transfer_fund(self, receiver, fund_amount):
        print("<<<<<<Transfer Balance>>>>>>\n")
        if isinstance(receiver, Customer):
            if fund_amount <= self.balance:
                self.withdraw(fund_amount)
                receiver.deposit(fund_amount)
                self.transaction_history.append(f'You transfer {fund_amount} taka to {receiver.name}')
                print(f'You sent {fund_amount} to {receiver.name}')
                print(f'Receiver name is: {receiver.name} and balance is: {receiver.balance}')
            else:
                print(f'You have insufficient balance. Your Balance is {self.balance}')    
        else:
            print("The account is not valid")        

    def available_balance(self):
        print(f'Your Balance Is {self.balance}')

    def view_transaction(self):
        print('Your transaction History\n')
        for transaction in self.transaction_history:
            print(transaction) 

    def __repr__(self):
        return f'Name: {self.name}, Email: {self.email}, Address: {self.address}, Account_type: {self.account_type}, Account_Number: {self.auto_number}, Balance: {self.balance}'

class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address) 
        self.accounts = []
        self.balance = 0
        self.loan = 0
        self.loan_enable = True

    def create_account(self, name, email, address, account_type, balance):
        new_customer = Customer(name, email, address, account_type, balance)
        self.accounts.append(new_customer)  
        print("Yes Admin!!! You created an account successfully")  
        return new_customer
    
    def delete_account(self, account_number):
        for account in self.accounts:
            if account.auto_number == account_number:
                self.accounts.remove(account)
                print(f'You deleted {account_number} successfully')
                return 
        print("Account not found.")

    def account_list(self):
        for account in self.accounts:
            if isinstance(account, Customer):
                print(f"Name: {account.name} and Account Number: {account.auto_number}") 

    def total_available_balance(self):
        total_balance = sum(account.balance for account in self.accounts if isinstance(account, Customer))
        print(f'The Total balance of the bank is {total_balance}')         

    def total_loan(self):
        total_loan = sum(account.balance for account in self.accounts if isinstance(account, Customer))
        print(f'The Total loan of the bank is {total_loan}')        

    def loan_permission(self):
        self.loan_enable = not self.loan_enable
        status = "enabled" if self.loan_enable else "disabled"
        print(f'Loan feature is now {status}')
        
    def __repr__(self):
        return f'Name: {self.name}, Email: {self.email}, Address: {self.address}, Balance: {self.balance}'

customer1 = Customer("Abdullah Hodan", "abdullahhodan448@gmail.com", "kishoreganj", "Saving", 500)
customer2 = Customer("Abdullah", "abdullahhodan@gmail.com", "kishoreganj", "Saving", 5200)

print(customer1)
print(customer2)

customer1.deposit(5000)
customer2.deposit(1000)
customer1.withdraw(2000)
customer1.take_loan(5000)
customer1.take_loan(5000)
customer1.take_loan(5000)
customer1.transfer_fund(customer2, 5000)
customer1.available_balance()
customer1.view_transaction()

admin = Admin("Abdullah Rohan", "ruhan123@xz.com", "kishoreganj")
admin.create_account("Tanbir", "tanbir123@.com", "Thanci", "saving", 1000)
admin.create_account("Tanbir12345", "tanbir1231234@.com", "Thanci2334", "saving", 100)
admin.account_list()
admin.total_loan()
admin.loan_permission()


