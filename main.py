import random
passlen= int(input("enter the password length:"))
s= "abcdefghijklmnopqrstuvwxyz"
t= "!@#$%^&*?"
u= "1234567890"
v= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p= "".join(random.sample(s+t+u+v, passlen))
print (p)
