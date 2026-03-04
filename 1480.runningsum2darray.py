nums=list(map(int,input().split()))
total=0
my_new=[]
for i in range(len(nums)):
  # take total + nums at that index and that index can not be received alone
  # 0:1
  # 1:2
  # 2:3
  # 3:4
  # 4:5
  # 5:6
  total=total+nums[i]
  my_new.append(total)
print(my_new)
