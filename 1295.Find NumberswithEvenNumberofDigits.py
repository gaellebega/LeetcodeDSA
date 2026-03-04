nums=list(map(int,input().split()))
count=0
for num in nums:
  size=len(str(num))
  if size%2==0:
    count+=1
print(count)