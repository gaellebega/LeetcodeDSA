def rotate_matirx(mat):
  left=0
  right=len(mat)-1
  while(left<right):
    for i in range(left-right):
      top=left
      bottom=right
      # temporary variable to hold our topleft
      topLeft= mat[top][left]
      mat[top][left]=mat[bottom][left]
      mat[bottom][left]=mat[bottom][right]
      mat[bottom][right]=mat[top][right]
      mat[top][right]=topLeft
    r-=1
    l+=1
  


    