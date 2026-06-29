from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anamap=defaultdict(list)
        for word in strs:
            sw="".join(sorted(word))
            anamap[sw].append(word)
        return list(anamap.values())