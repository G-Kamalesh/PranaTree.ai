class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        if len(s) != len(t):
            return False
        else:
            for char in s:
                d1[char] = d1.get(char, 0) + 1
            for char in t:
                d2[char] = d2.get(char, 0) + 1

            if d1 == d2:
                return True
            else:
                return False

        