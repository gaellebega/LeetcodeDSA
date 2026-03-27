class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        # represent values in our current window
        window_total=0
        minimum=float("inf")
        for  right in range(len(nums)):
            window_total+=nums[right]
            # becouse we will shrink as long as we find the right result
            # the question is not find the subarray but find the smallest subarray that is why we have use while cz once we find the valid window our job is not finished the next task is can i make it smaller and keep it valid
            while window_total>=target:
                minimum=min(right+left-1,minimum)
                # if window greater or equal to target find small window
                window_total-=nums[left]
                left+=1
        if minimum==float("inf"):
            return 0
        else:
            return minimum       



