def issorted(nums):
  left=0
  right=1
  size=len(nums)
  while right<size:
    if nums[left]>nums[right]:
      return False
    left+=1
    right+=1
  return True
print(issorted([1,2,3,3]))
print(issorted([9,3,2,1]))
print(issorted([10,20,30,40,50]))


