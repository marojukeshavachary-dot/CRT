'''
t = int(input())
for i in range(1,t+1):
    print(" "*(t-i)+" *"*i)
for j in range(t-1,0,-1):
    print(" "*(t-j)+" *"*j)
    

    
n = int(input())
s = 1
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(s,end=" ")
        s +=1
    print()
    
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(k) for k in range(1,i+1)]))    
    
    '''
   