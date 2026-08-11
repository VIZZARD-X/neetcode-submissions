class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        f=[[]for _ in range(len(nums)+1)]
        for num,c in count.items():
            f[c].append(num)
        res=[]
        for i in range(len(f)-1,0,-1):
            for num in f[i]:
                res.append(num)
                if len(res)==k:
                    return res
        return res