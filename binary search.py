nums=list(map(int,input().split()))
target=int(input())
n=sorted(nums)
left=0
right=len(n)-1
flag=-1

while left<=right:
    mid=(left+right)//2
    if n[mid]==target:
        flag=mid
        break
    elif n[mid]>target:
        right=mid-1
    else:
        left=mid+1
if flag==-1:
    print("target not found")
else:
    print("target found at index:",flag)                