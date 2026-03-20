# from collections import defaultdict
# def groupAnagrams(strs):
#   # using the default dictionary on the integers 
#   my_dicitionaty =defaultdict(int)
#   for word in strs:
#     my_dicitionaty[word]+=1

from collections import defaultdict
def groupAnagrams(strs):
  result=[]
  my_dictionary=defaultdict(list)
  # using the sorted element as the key
  for word in strs:
  #  you can not use the list to be the keys
   key=tuple(sorted(word))
  #  for every key we will append the original word tot he array
   my_dictionary[key].append(word)
  print(my_dictionary)

  for value in my_dictionary.values():
    result.append(value)
  return result  