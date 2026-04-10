# if it is possible to make the moves and then you return to the origin then we are gonna return true else we return false
# we are not gonna consider the moves but the frequencies
from collections import Counter
# big O of n where the n is the length of the string that we are given
def robotreturntoorigin(moves):
  fmap=Counter(moves)
  for m in moves:
    fmap[m]+=1
    if fmap['U']==fmap['D'] and fmap["R"]==fmap["L"]:
      return True
    else:  
      return False



