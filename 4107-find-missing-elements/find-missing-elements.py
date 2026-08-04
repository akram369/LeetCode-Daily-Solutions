class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        full_range = set(range(min(nums), max(nums) + 1))
        return sorted(full_range - set(nums))