'''import numpy as np 

arr = np.array([10,20,30])
print(arr)

print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.mean(arr))
print("Even number list is: ",np.arange(2,10,2))
print("Odd number list is: ",np.arange(1,10,2))

n = int(input("Enter the size"))
ele = list(map(int,("enter ele").split()))
print("Array Ele are:",np.array(ele)) 
import numpy as np

arr = np.array([3,2,1])
print(np.max(arr))
nums = list(map(int,input().split()))
if len(set(nums)) >= 3:
    print(sorted(set(nums))[-3])
else:
    print(max(n(int,input(.)))'''

nums = list(map(int,input().split()))
inc = True 
dec = True 
for i in range(1,len(nums)):
    if nums[i] > nums[i+1]:
        inc = False 
    if nums[i] < nums[i+1]:
        dec = False
if inc or dec:
    print("Monotonic Array")
else:
    print("Not Monotonic Array")