def lengthOfLongestSubstring(self, s: str) -> int:
  right=0
  left=0
  new=set()
  max_len=0
  while(right<len(s)):
    if s[left] not in new:
      s.add(s[left])
      right+=1
    else:
      s.remove(s[right])
      left-=1
      max_len(max_len,len(s))
  return max_len    
   

