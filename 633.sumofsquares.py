import math
def judgeSquareSum(self, c: int) -> bool:
  # a and be dont have to be different
  # they could be the same
  # what if a,b all equal to 0

  for a in range(0,sqrt(c)+1):
    for b in range(0,sqrt(c) +1):
      # Brute false solution
      if a<=c and b<=c:
        asq=a*a
        bsq=b*b
        if asq+bsq==c:
        return True
  return False
