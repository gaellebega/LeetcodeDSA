class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
    #  took our array then we reversed
    # then we took the k elements  then we take the first portion and we reverse that and then we take the remaiining portion and also we reverse it aside
            k=k%len(nums)
            l=0
            r=len(nums)-1
            while(l<r):
                nums[l],nums[r]=nums[r],nums[l]
                l,r=l+1,r-1
            l=0
            r=k-1   
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l,r=l+1,r-1
            l=k
            r=len(nums)-1   
            while(l<r):
                nums[l],nums[r]=nums[r],nums[l]
                l,r=l+1,r-1 