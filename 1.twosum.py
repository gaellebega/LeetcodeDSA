class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       left=0
       right=1
       while(right<len(nums)):
          if nums[left]+nums[right]==target:
               return [left,right]
          right+=1
          if right==len(nums):
              right+=1
              left=right+1
           

                