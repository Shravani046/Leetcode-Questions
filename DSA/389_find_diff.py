class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return [i for i in t if s.count(i) != t.count(i)][0]