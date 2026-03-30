def find_words(words,k):
  result=[]
  for i in range(len(words)):
    for ch in words[i]:
      if ch==k:
        result.append(i)
        break
  return result
print(find_words(["leet","coode","game"],"e"))