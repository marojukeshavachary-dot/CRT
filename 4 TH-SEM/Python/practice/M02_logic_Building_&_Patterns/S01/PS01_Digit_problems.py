'''
1) Write a python code to count the digit of number?
Ex: 15678-->output: 5

a = int(input())
b = len(str(a))
print(a)

sum of a given number
num = int(input())
sum = 0 
while num>0:
    sum += num%10 
    num //= 10 
print(sum)
'''
#product of a given number
'''
num = int(input())
sum = 1 
while num>0:
    sum *= num%10 
    num //= 10 
print(sum)
'''
#reverse of a given number
num = input()
print(num[::-1])