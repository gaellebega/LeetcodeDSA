def subtractProductAndSum( n: int) -> int:
  product=1
  total=0
  for num in str(n):
    product*=int(num)
    total+=int(num)
    remaining=product-total
  return remaining
print(subtractProductAndSum(178))
print(subtractProductAndSum(234))