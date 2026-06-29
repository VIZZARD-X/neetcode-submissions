class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        r=[]
        for i in range(len(nums)):
            c=target-nums[i]
            if c in seen:
                r.append(i)
                r.append(seen[c])
                r.sort()
                return r
            else:
                seen[nums[i]]=i