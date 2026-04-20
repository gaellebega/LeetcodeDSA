from collections import Counter
def findDifference(s,t):
  counter_s=Counter(s)
  counter_t=Counter(t)
  for letter in counter_t:
    if counter_t[letter]!=counter_s.get(letter,0):
      return letter
