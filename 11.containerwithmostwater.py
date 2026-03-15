def maxArea(self, height: List[int]) -> int:
  # BRUTE FORCE
  response=0
  for l in range(len(height)):
    for r in range(1,len(height)):
      # width(r-l)
      # height will always be the min of the right pointer
      w=r-l
      h=min(height[r],height[l])
      area=w*h
      res=max(res,area)
  return res   
      
