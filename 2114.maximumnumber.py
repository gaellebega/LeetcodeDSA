def makemaximum_num(sentences):
  max_sentence=0
  for sentence in sentences:
    new=len(sentence.split())

    if new>max_sentence:
      max_sentence=new
  return new    
print(makemaximum_num(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))

