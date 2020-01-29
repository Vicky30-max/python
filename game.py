import random 
val=random.randint(1,3)
n=3
for i in range(n):
    user=int(input("enter ur num:"))
    if (user==val):
        print("congrats")
    else:
         print("oops!sorry")
