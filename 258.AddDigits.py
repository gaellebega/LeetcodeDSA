def add_digits(num):
  while num>9:
    tens=num//10
    ones=num%10
    num=tens+ones
  return num  
print(add_digits(38))