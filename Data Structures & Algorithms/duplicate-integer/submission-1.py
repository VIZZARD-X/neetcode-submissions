class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rep={}
        flag=False
        for i in range(len(nums)):
            if nums[i] in rep:
                rep[nums[i]]+=1
            else:
                rep[nums[i]]=1
        for i in rep:
            if rep[i]>1:
                flag=True

        return flag