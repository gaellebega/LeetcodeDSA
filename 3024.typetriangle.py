class Solution:
    def triangleType(self, nums: List[int]) -> str:
            first=nums[0]
            second=nums[1]
            third=nums[2]
            if first+second<=third or second+third<=first or third+first<=second:
                return "none"
            if first==second and second==third :
                return "equilateral"
                 # Scalene: all sides different
            elif first != second and second != third and third != first:
                return "scalene"    
            else:
                return "isosceles"
                  


                 
     
