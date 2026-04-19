def lengthOfTheLatWord(s):
  words=s.split()
  return len(words[-1])
print(lengthOfTheLatWord("Hello World"))