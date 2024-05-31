def performinsertionsort(nums):
    n=len(nums)
    lastleleinsorted=0
    for firstindex in range(1,n):
        temp=nums[firstindex]
        prev=lastleleinsorted

        while prev>=0 and nums[prev]>temp:
            nums[prev+1]=nums[prev]
            prev=prev-1
        nums[prev+1]=temp
        lastleleinsorted=lastleleinsorted+1
        print(nums)

nums=[1,6,4,3,2,9,7]
print("Before sorting : ",nums)

performinsertionsort(nums)
print("after sorting : ", nums )