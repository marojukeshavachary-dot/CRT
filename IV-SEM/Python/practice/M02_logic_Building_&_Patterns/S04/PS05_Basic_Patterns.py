'''
input : 4 
output :
* * * *
* * * *
* * * *
* * * * 

t = int(input())
for i in range(t):
    for j in range(t):
        print(" * ", end = " ")

    
    print(" ")
    
    
    input : 4
    output:
    * 
    * *
    * * * 
    * * * *
    
t = int(input())
for i in range(1,t+1):
    for j in range(i):
        print("*",end=" ")
    print()
    
intput:4
output:
* * * *
* * * 
* * 
*

t = int(input()) 
for i in range(t):
    for j in range(i-1, t-1):
        print("*", end=" ")
    print()   
    
    
    input:4
    output:
    1 
    2 3
    4 5 6
    7 8 9 10
    
    
    
t = int(input())
k =1

for i in range(1,t+1):
    for j in range(i):
        print(k,end=" ")
        k += 1
    print()
    
t = int(input())
k = 65
for i in range(t):
    for j in range(i+1):
        print(chr(k),end =" ")
        k += 1
        
        
        
    print()
    
    
    
t = int(input())

for i in range(t):
    for j in range(i+1):
        print(chr(65+j),end =" ")
    print()
    '''
    


t = int(input())
for i in range(t,):
    for j in range(t,i-1  ):
        print("*",end = " ")
    print()