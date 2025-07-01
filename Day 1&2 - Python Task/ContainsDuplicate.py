class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1

        found_duplicate = False
        for count in d.values():
            if count >= 2:
                found_duplicate = True
                break

        return found_duplicate
            
        