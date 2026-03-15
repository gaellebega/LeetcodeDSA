# input: haystack="hello", niddle="ll"
# input:haystack="aaa",needle="bba"
# empty string we will return 0
def strStr(self, haystack: str, needle: str) -> int:
  #  if our needle is empty
 for i in range(len(haystack)):
  if haystack[i:i+len(needle)]==needle:
   return i
 return -1
  