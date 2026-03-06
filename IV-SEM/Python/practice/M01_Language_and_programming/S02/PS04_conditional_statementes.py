#read a number from user and check whether it is positive or negative or zero
'''
input : 10
output : +ve 

input : 0 
output : zero

input : -5
output : -ve
'''

n = int(input())
if n > 0:
    print("+ve")
elif n == 0:
    print("zero")
else:
    print("-ve")