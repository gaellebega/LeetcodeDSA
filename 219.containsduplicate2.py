def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen and abs(i-seen[nums[i]])<=k:
                return True 
                # It updates the last position where this number was seen.
                seen[nums[i]]=i
        return False        