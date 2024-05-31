nums=list(map(int,input().split()))
target=int(input())
flag=-1
n=len(nums)
for i in range(n):
    if nums[i]==target:
        flag=i
        break
if flag==-1:
    print("not found")
else:
    print("target value:",flag)        
