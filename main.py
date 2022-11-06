
import random

class bank(object):
    
    def __init__(self, owner, balance, password):
        self.owner = owner
        self.balance = balance
        self.password = password
              
    def display(self):
        print(f"Hello {self.owner}. This is your balance:{self.balance}$.")
           
    def deposit(self):
        while True:
            try:
                am=int(input("Enter how much you want to deposit: "))
                if am > 0:
                    self.balance += am
                elif am<0:
                    print("You cant deposit negative numbers, please try again")
                    mybank.deposit()
                break
            except ValueError as e:
                pass
                print("You have to type a number",e)
            
    def login(self,password):
        if password==self.password:
            print("Your password is correct")
            return True
        else:
            print("Incorrect password")
            return False

    def withdraw(self):
        while True:
            try:
                w=int(input("Enter the amount you want to withdraw: "))
                balance = self.balance
                if w < 0:
                    print("Dont type negative numbers please try again")
                    mybank.withdraw()
                elif w > balance:
                    print("You are trying to withdraw more than what you have in your account")
                    print(f"Your balance is {balance} try again")
                    print("")
                    mybank.withdraw()
                elif w <=balance:
                    self.balance = self.balance-w
                break
            except ValueError as e:
                pass
                print(e,"Type 0 if you want to go back")

# Input I emrit edhe pinit      
n1=str(input("Enter Your name: "))
print("")
while True:
    try:
        p=int(input("What do you want your pin to be: "))
        break
    except ValueError as e:
        print(e)
        continue

#Caktimi i parametrave nclass       
n=random.randint(1000,3000)
mybank=bank(n1,n,p)
while True:
    try:
        pss=int(input("Enter your pin: "))
        pa=mybank.login(pss)
        if pa==False:
            continue
        elif pa==True:
            pass
        while True:
            print("What do you want to do?")
            qu=input("Withdraw , Deposit, Display or Exit: ")
            print("")
            qu =qu.casefold()
            if qu == "withdraw":
                mybank.withdraw()
            elif qu == "display":
                mybank.display()
            elif qu == "exit":
                print("Thanks for choosing our bank, have a good day")
                exit()
            elif qu == "deposit":
                mybank.deposit()
            else:
                print("Wrong input")       
    except ValueError as e:
        print(e)
        continue  
