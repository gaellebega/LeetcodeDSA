class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # find the difference between the values then we find the longest window poassible which is maximum
        # longest string is 3 is what we are gonna return 
        curCost=0
        l=0
        resp=0
        for r in range(len(s)):
            # the ascii value of a string
            cost= abs(ord(s[r])-ord(t[r]))   
            curCost+=cost
            # when we know the window is invalid
            while curCost>maxCost:
                curCost-= abs(ord(s[l])-ord(t[l]))  
                l+=1


            # when the window is valid we make the size of substring and compare it to the max response that we have
            resp=max(resp,r-l+1)
        return resp    
       
        