

import math
def judgeSum(c):
  squareroot=set()
  for i in range(0,int(sqrt(c))):
    squareroot.add(i*i)

    # instead of making the squareroot of a and make the 
    a=0
    while a*a<c:
      target=c-a*a
      if target in squareroot:
        a+=1
        return True 
    return False
