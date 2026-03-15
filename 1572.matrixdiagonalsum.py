def diagonalSum(self, mat: List[List[int]]) -> int:
  n=len(mat)
  result=0
  for i in range(len(n)):
    # primary diagonal
    result+=mat[i][i]
    # secondary diagonal
    result+=mat[i][n-1-i]
  if n%2!=0:
    return result-mat[n//2][n//2]
  return result-0
