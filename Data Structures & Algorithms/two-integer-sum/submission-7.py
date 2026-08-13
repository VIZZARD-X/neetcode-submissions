class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=collections.defaultdict()
        for idx,num in enumerate(nums):
            comp=target-num
            if comp in seen:
                return [seen[comp],idx]
            seen[num]=idx
        return []
