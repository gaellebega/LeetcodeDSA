# meaining of the longest turblent subarray this is the subarray whcih have the signs like > then< then > then < like the same
# signs can not follow each other also the equal is not conted in that so we have to return the longest length of that array like the number of elemnt behinda nd next to the signs
# sliding windowow is same as kaden alogrorithm

def maxTrublentSize(arr):
  # cz it is subarray
  left=0
  right=1
  # the maximum size of the turblent sum
  result=1
  prevsign=""
  while(right<len(arr)):
    # remember the case have not to be the equal sign
    if arr[right-1]>arr[right] and prevsign!=">":
      result=max(result,right-left+1)
      right+=1
      prevsign=">"
    elif arr[right-1]<arr[right] and prevsign!="<":
      result=max(result,right-left+1)
      right+=1
      prevsign="<"
    # else we have the consective signs or we have the equal signs we have to skip them togther
    else:
      right=right+1 if arr[right]==arr[right+1] else right
      left=right-1
      prevsign=""
  return result  


