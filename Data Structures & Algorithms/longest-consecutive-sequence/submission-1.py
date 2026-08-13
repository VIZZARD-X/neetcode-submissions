class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        c=0
        for n in s:
            if (n-1) not in s:
                length=0
                while(n+length in s):
                    length+=1
                c=max(length,c)
        return c 


