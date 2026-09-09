import json
import random
import string
from pathlib import Path  #data.json file ka path pata hona chahiye


class Bank:
    database = "data.json"
    data=[]

    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")

    @staticmethod
    def update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k = 3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        id=alpha+num+spchar
        random.shuffle(id)
        return "".join(id)

    #ceating a account
    def createaccount(self):
        info={ 
            "name":input("Tell your name : "),
            "age":int(input("Enter your age: ")),
            "email":input("Enetr your email : "),
            "pin":int(input("Enter your 4 digit pin : ")),
            "accountno.": Bank.__accountgenerate(),
            "balance": 0
        }
        if info['age']<18 or len(str(info['pin']))!=4:
            print("sorry you cant create your account")
        else:
            print("Your account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            
            Bank.data.append(info)
            Bank.update()

    def depositmoney(self):
        accnumber=input("please tell your account number")
        pin=int(input("please enter your pin"))

        #making a deep copy and making changes there
        userdata= [i for i in Bank.data if i['accountno.']==accnumber and i['pin']==pin]
        
        if userdata==False:
            print("Sorry no data found")
        else:
            amount=int(input("Enter the amount to be deposited"))
            if(amount>10000 or amount<0):
                print("sorry amout is either above 10000 or below 0")
            else:
                userdata[0]['balance']+=amount
                Bank.update()
                print("Amount deposited successfully")

    def withdrawmoney(self):
        accno=input("please tell your account number")
        pin=int(input("please enter your pin"))

        userdata=[i for i in Bank.data if i['accountno.']==accno and i['pin']==pin]

        if userdata==False:
            print("Sorry no data found")
        else:
            amount=int(input("Enter the amount to be withdrawn"))
            if(userdata[0]['balance']<amount):
                print("Insufficient balance")
            else:
                userdata[0]['balance']-=amount
                Bank.update()
                print("Withdraw successful")

    def showdetails(self):
        acc=input("Please enter your account number : ")
        pin=int(input("Pleaase enter your pin"))

        userdata=[i for i in Bank.data if i['accountno.']==acc and i['pin']==pin]

        if userdata==False:
            print("No data found!!")

        else:
            print("Account Details")
            # print(f"Name : {userdata[0]['name']}")
            # print(f"Age : {userdata[0]['age']}")
            # print(f"Email : {userdata[0]['email']}")
            # print(f"Account Number : {userdata[0]['accountno.']}")
            # print(f"Balance : {userdata[0]['balance']}")

            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        acc=input("Please enter your account number : ")
        pin=int(input("Pleaase enter your pin"))

        userdata=[i for i in Bank.data if i['accountno.']==acc and i['pin']==pin]

        if userdata==False:
            print("No data found!!")
        else:
            target=input("What do you want to update")
            




user=Bank()
print("press 1 for creating an account")
print("press 2 for depositing the money int he bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check=int(input("tell your response :-"))

if check==1:
    user.createaccount()


if check==2:
    user.depositmoney()

if check==3:
    user.withdrawmoney()

if  check==4:
    user.showdetails()

if check==5:
    user.updatedetails()