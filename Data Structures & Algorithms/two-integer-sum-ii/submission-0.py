class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for idx,num in enumerate(numbers):
            complement=target-num
            if complement in seen:
                return [seen[complement],idx+1]
            seen[num]=idx+1
        