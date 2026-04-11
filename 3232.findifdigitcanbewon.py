def canAliceWin(nums):
  single=0
  double=0
  for i in range(len(nums)):
    if nums[i]<=9:
      single+=nums[i]
    elif nums[i]<=99:
      double+=nums[i]
  return (single!=double) 
print(canAliceWin([1,2,3,4,10]))     