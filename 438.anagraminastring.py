from collections import Counter
class Solution:
    def findAnagrams(s, p):
        result=[]
        k=len(p)
        p_counter=Counter(p)
        window_count=Counter()
        if k> len(s):
            return result
        for i in range(k):
            window_count[s[i]]+=1
        if  window_count==p_counter:
            result.append(0)
        left=0
        right=k
        while(right<len(s)):
            window_count[s[right]]+=1
            right+=1
            window_count[s[left]]-=1
            if window_count[s[left]]==0:
                del window_count[s[left]]
            left+=1
            if window_count==p_counter:
                result.append(left)
        return result            



               