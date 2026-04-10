class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        maximum=nums[0]*nums[1]   
        for i in range(1,len(nums)-1):
            product=nums[i]*nums[i+1]
            maximum=max(product,maximum)
        return maximum   
        