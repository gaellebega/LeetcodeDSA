def numberOfEmployeesWhoMetTarget(hours,target):
  count=0
  for i in range(len(hours)):
    if hours[i]>=target:
      count+=1
  return count    
print(numberOfEmployeesWhoMetTarget([5,1,4,2,2],6))