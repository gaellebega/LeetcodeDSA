def roman_to_int(s):
  roman_dict={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
  }
  n=len(s)
  remaining=0
  i=0
  while(i<n):
    # to access the value we use the key
      current=roman_dict[s[i]]
      if (i+1<n):
        next_item=roman_dict[s[i+1]]
        if next_item>current:
            remaining+=next_item-current
            i+=2
            continue
    #after the while loop then we hace 
        elif next_item<=current:
          remaining+=current
          i+=1
      else:
          remaining+=current
          i+=1  
  return remaining 
# Test the function
print(roman_to_int("III"))       # Should print 3
print(roman_to_int("IV"))        # Should print 4
print(roman_to_int("IX"))        # Should print 9
print(roman_to_int("LVIII"))     # Should print 58
print(roman_to_int("MCMXCIV"))   # Should print 1994


     
