class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        res=[]
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in d:
                res.append(d[complement])
                res.append(i)
                return res
            else:
                d[nums[i]]=i
        