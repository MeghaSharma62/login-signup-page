import json
import re

print("Welcome to my login-signup")
user=input("Do you want to \n1.)signup\n2.)login: ")
if user=="signup":
    username=input("Enter your username: ")
    print("Create a strong password Use specail characters.")
    password1=input("Enter ur password: ")
    if re.search ("[a-z A-Z]",password1) and re.search ("[@%$#!]",password1) and re.search ("[0-9]",password1) :
        password2=input("Enter your password agian: ")  
        if password1==password2:
            print("Confirm password: ")
            date_of_birth=input("enter your date of birth: ")
            contact=int(input("Enter your moblie number: "))
            email=input("enter your email id: ")
            dic=[{"username":username,"password":password1,"re_password":password2,"date_of_birth":date_of_birth
            ,"contact":contact,"email":email},],
            buy=open("data signup.json","a")
            json.dump(dic,buy,indent=4)

        else:
            print("password not matching")
    else:
        print("weak password please use specail charcters")
else:
    if user=="login":
        username=input("enter your username: ")
        password=input("enter your password: ")
        if ["username"]==username and ['password']==password:
                with open("data signup.json","r") as file1:
                        json.load(file1)
                        # a=file1.read()
                        # b=json.loads(a)    
                print("login successful")
        else:
                print("wrong username")
    else:
        print("Wrong id")