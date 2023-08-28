import random
print("WELCOME TO RANDOM PASSWORD GENERATOR")
string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*@#$&()"
length = int(input("enter your password length = "))
password =""
for i in range(length):
    password += random.choice(string)
    
print( "your password generated is ",password)
    