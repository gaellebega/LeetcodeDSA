# pangram is a sentence where every letter of english character appear at least once
def checkIfPangram(sentence):
  for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in sentence:
      return False
  return True
print(checkIfPangram("myname")) 