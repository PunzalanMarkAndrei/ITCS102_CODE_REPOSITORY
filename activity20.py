
from getpass import getpass

u = "Punzalan"
p = "mariel" 

isLogin = False #trigger

while isLogin == False:

    user = input("please input username --> ")
    password = getpass("please input password --> ")

    if user == u and password == p:
        print("ACCESS GRANTED")
        isLogin = True
    else:
        print("ACCESS DENIED")
        isLogin = False