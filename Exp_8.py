database = [
{"name":"Sakshi", "acc":123456, "ph":9008001001, "pin":6749, "balance":7800} ,
{"name":"Sarah", "acc":234567, "ph":9008001002, "pin":5903, "balance":6500} ,
{"name":"John", "acc":345678, "ph":9008001003, "pin":7832, "balance":9000} ,
{"name":"Nikki", "acc":456789, "ph":9008001004, "pin":4880, "balance":5500} ,
{"name":"Jimmy", "acc":567890, "ph":9008001005, "pin":2198, "balance":7400} ,
]

class Account:
    def __init__(self, name, acc_no, phone_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.phone_no = phone_no
        self.balance = balance

    def account_info(self):
        print('\nAccount Details: ')
        print(f'\nName: {self.name}\nAccount no: {self.acc_no}\nContact no: {self.phone_no}\n')

    def enquiry(self):
        print(f'\nYour Account balance is: Rs.{self.balance}')

    def pin_change(self,newpin):
        self.pin = newpin
        print(f"\nYour PIN is now {self.pin}")

    def deposit(self,dep_amt):
        self.balance += dep_amt
        print(f'\nDeposit Accepted! Your Current balance is Rs. {self.balance}')

    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print(f'\nWithdrawl Accepted! Your Current balance is Rs. {self.balance}')
        else:
            print('\nSorry! You have insuficient Balance.')

user_acc = int(input('Enter Account no: '))
attempt = 3
while attempt!=0:
    user_pin = int(input('Enter PIN: '))

    for user in database:
        if user.get('acc') == user_acc and user.get('pin') == user_pin:
            print (f"\nHello {user['name']}!")
            attempt=0
            userobj = Account(user['name'], user['acc'], user['ph'], user['balance'])

            print("\nPlease select the operation:\nAccount details (press 1)\nBalance Enquiry (press 2)\nChange PIN (press 3)\nMoney Deposit (press 4)\nMoney Withdrawl (press 5)")
            response = int(input("\nEnter your response: "))

            if response == 1:
                userobj.account_info()
            elif response == 2:
                userobj.enqiry()
            elif response == 3:
                newpin = int(input("\nEnter a new 4-digit PIN: "))
                userobj.pin_change(newpin)
                user['pin'] = newpin
            elif response == 4:
                dep_amt = int(input("\nEnter the amount to be deposited: "))
                userobj.deposit(dep_amt)
            elif response == 5:
                wd_amt = int(input("\nEnter the amount to be withdrawn: "))
                userobj.withdraw(wd_amt)

        elif user.get('acc') == user_acc and user.get('pin') != user_pin:
            print (f"{user['name']}, you have entered incorrect password. Try again!")
            attempt = attempt-1
            if attempt==0:
                print("You've entered inncorrect password 3 times. Your account is now blocked!")
                break
