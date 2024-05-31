def performbubblesort(nums):
    n=len(nums)
    fixedindex=n-1
    while fixedindex>0:
        for i in range(fixedindex):
            if nums[i] > nums[i+1]:
                temp=nums[i]
                nums[i]=nums[i+1]
                nums[i+1]=temp
        print(nums)
        fixedindex=fixedindex-1


nums=[1,6,4,3,2,9,6]
print("Before sorting : ",nums)

performbubblesort(nums)
print("after sorting : ", nums )