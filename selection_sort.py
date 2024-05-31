def performselectionsort(nums):
    n=len(nums)
    fixedindex=n-1
    while fixedindex>0:
        maxeleindex=fixedindex
        for i in range(fixedindex):
            if nums[i] > nums[maxeleindex]:
                maxeleindex=i
        if maxeleindex != fixedindex:
            temp=nums[maxeleindex]
            nums[maxeleindex]=nums[fixedindex]
            nums[fixedindex]=temp
        print(nums)
        fixedindex=fixedindex-1


nums=[1,6,4,3,2,9,7]
print("Before sorting : ",nums)

performselectionsort(nums)
print("after sorting : ", nums )