class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        hashmap = {}
        if len(nums1) > len(nums2):
            larger = nums1
            smaller = nums2
        else:
            larger = nums2
            smaller = nums1

        for i in larger:
            hashmap[i] = hashmap.get(i, 0) + 1

        for j in smaller:
            if j in hashmap and hashmap[j] > 0:
                answer.append(j)
                hashmap[j] -= 1

        return answer   
        