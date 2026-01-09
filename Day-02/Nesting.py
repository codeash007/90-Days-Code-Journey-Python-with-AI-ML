username = input("Enter username:=")
password = input("Enter password")
if(username == "admin" and password == "pass"):
    print("Sucess")
else:
    if(username != "admin"):
        print("Wrong Username")
    else:
        print("Wrong password")        