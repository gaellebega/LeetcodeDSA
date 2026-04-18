class Solution:
    def singleNumber(nums) -> int:
        for num in nums:
            if nums.count(num)==1:
                return num