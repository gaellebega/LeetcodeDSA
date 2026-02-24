n=int(input())
for i in range(n):
  players=int(input())
  y,r=list(map(int,input().split()))
  yellow=y//2
  red=r
  # cz it doesnt have to be above the number of the players that we have
  total_susp=min(players,yellow+r)
  print(total_susp)