class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i + 1 < n and nums[i + 1] == nums[i] + 1:
            i += 1
        s = sum(nums[:i + 1])
        num_set = set(nums)
        while s in num_set:
            s += 1
        return s