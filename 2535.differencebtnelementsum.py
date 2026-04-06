def differenceOfSum(nums):
  elementsum=0
  digitsum=0
  for n in nums:
    elementsum+=n
    for digit in str(n):
      digitsum+=int(digit)

  difference=abs(digitsum-elementsum)
  return difference  
print(differenceOfSum([1,15,6,3]))  

