class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        # we are gonna make the sum of numbers of ns until we get the duplicates
        # we are using the while loop cz we dont know the number of times we are gonna make this happen
        while n not in visit:
            visit.add(n)
            n=self.sumOfSquares(n)
            if n == 1:
               return True
        return False   
    def sumOfSquares(self, n: int) -> int:
        output=0
        while n:
            digit = n%10
            digit=digit**2
            output+=digit
            n=n//10
            n=n**2
        return output   

