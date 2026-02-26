nums=list(map(int,input().split()))
l=0 
for i in range(len(nums)):
    if nums[i]!=0:
      nums[i],nums[l]=nums[l],nums[i]
      l=l+1
print(nums)  
 