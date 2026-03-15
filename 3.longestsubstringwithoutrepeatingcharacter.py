def lengthOfLongestSubstring(self, s: str) -> int:
  right=0
  left=1
  new=()
  while(left<right):
    if s[left]!=s[right]:
       new.add(s[left])
       new.add(s[right])
       left+=1
     return len(new)  
    elif s[left]==s[right]:
        return 1



