def maxArea(self, height: List[int]) -> int:
  n=len(height)
  left=0
  right=n-1
  max_area=0
  # if the left height and the right height all they are tall then we found our result
