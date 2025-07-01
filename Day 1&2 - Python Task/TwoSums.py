hashmap = {n : i for i, n in enumerate(nums)}
for i in range(len(nums)):
    complement = target - nums[i]
    if complement in hashmap and hashmap[complement] != i:
        return([i, hashmap[complement]])
        break