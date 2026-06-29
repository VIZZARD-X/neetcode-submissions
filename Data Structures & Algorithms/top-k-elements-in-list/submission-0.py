from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        mk=d.most_common(k)
        return[item[0]for item in mk]
        