class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for c in s:
            c=c.lower()
            if c.isalnum():
                l.append(c)
        k="".join(l)
        return k==k[::-1]