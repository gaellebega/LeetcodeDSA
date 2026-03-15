def maxArea( height):
  # BRUTE FORCE
  response=0
  for l in range(len(height)):
    for r in range(1,len(height)):
      # width(r-l)
      # height will always be the min of the right pointer
      w=r-l
      h=min(height[r],height[l])
      area=w*h
      response=max(response,area)
  return response
print(maxArea([1,8,6,2,5,4,8,3,7]))      
print(maxArea([1,1]))
