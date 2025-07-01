class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = {}
        for i in nums:
            c[i] = c.get(i, 0) + 1

        check = len(nums)/2

        if check < max(c.values()):
            return max(c)
