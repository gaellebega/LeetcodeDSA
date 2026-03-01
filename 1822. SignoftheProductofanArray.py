
nums=list(map(int,input().split()))  
count=0      
found_zero=False      
for num in nums:
  if num==0:
    print("0")
    found_zero=True
    break
  if num<0:
    count+=1
if not found_zero:    
  if count %2==0:
    print(1)
  else:
    print(-1)  

  
  