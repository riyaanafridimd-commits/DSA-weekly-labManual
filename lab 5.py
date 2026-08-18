'''def show_menu():
    print("\n Menu")
    print("1.check Balance")
    print("2.withdrawl cash")
    print("3.deposit cash")
    print("4.exit")
    print("---------")
def check_pin(enteredpin,correctpin):
    if enteredpin==correctpin:
        return True
    else:
        return False
def show_balance(balance):
    print("Your current Balance",balance)
def is valid_amount(amount,balance):
    if amount<=0:
        print("invalid amount! please enter positive value.")
        return False
    elif amount%100!=0:
        print("amount must be multiple of 100")
        return False
    elif amount>balance:
        print("insufficient balance! Your balance is Rs",balnce)
        return False
    else:
        return True
def withdraw(balnce, amount):
    balance= balnce-amount
    print("please collect Yoour amount Rs",amount)
    return balance
def deposit(deposit,amount):
    if (amount<=0):
        print("invalid deposit amount")
        return balnce
    balance= balance+amount
    print("Rs",amount,"deposit successful.")
    return balance

correctpin=123
balance=1,00,000
attempt=3
while attempts>0:
    enteredpin=int(input("enter Your correctpin")
    if checkpin(enteredpin,correctpin):
                   print("pin accepted",welcome)
                   break
    else:
        attempts= attempt-1
        print("wrong pin",attempts,"attempts left.")
        if attempts==0:
            print("card balance.please contact yor bank")
        else:
            while(True):
                show_menu()
                choice=int(input("enter your choice(1-4)")
                if(choice==1):
                           show_balance(balance)
                elif(choice==2):
                    amount=int(input("enter amount to withdraw")
                elif(choice==3):
                    amount=int(input("enter amount to deposit")
                    balance=deposit(balance,amount)
                    show_balance(balance)
                elif(choice=4):
                    print("thank you for using ATM")
                    break
                else:
                    print("invalid! choice please enter choice(1-4)")'''

def student1(rollno,name,m1,m2,m3):
     rollno=int(input("enter student rollnumber",rollno))
     name=input("enter student name:",name)
     m1=int(input("enter marks of subject 1:",m1))
     m2=int(input("enter marks of subject 2:",m2))
     m3=int(input("enter marks of subject 3:",m3))
def student2(rollno,name,m1,m2,m3):
     rollno=int(input("enter student rollnumber",rollno))
     name=input("enter student name:",name)
     m1=int(input("enter marks of subject 1:",m1))
     m2=int(input("enter marks of subject 2:",m2))
     m3=int(input("enter marks of subject 3:",m3))
def student3(rollno,name,m1,m2,m3):
     rollno=int(input("enter student rollnumber",rollno))
     name=input("enter student name:",name)
     m1=int(input("enter marks of subject 1:",m1))
     m2=int(input("enter marks of subject 2:",m2))
     m3=int(input("enter marks of subject 3:",m3)) 
def avg(m1,m2,m3):
    avg=(m1+m2+m3)/3

rollno=int(input("enter student rollnumber",rollno))
name=input("enter student name:",name)
m1=int(input("enter marks of subject 1:",m1))
m2=int(input("enter marks of subject 2:",m2))
m3=int(input("enter marks of subject 3:",m3))
   
