import getpass

username = 'Mark'
password = 'maryel'

u = input('Input Username ---> ')
p = getpass.getpass('Input Password ---> ')

if username == u and p == password : 
       print("Access Granted")
else : 
      print("Access Denied")