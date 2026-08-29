class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        idx = sorted(range(n), key=lambda i: nums[i])
        result = [0] * n
        group = []
        for k in range(n):
            i = idx[k]
            if group and nums[i] - nums[idx[k-1]] > limit:
                indices = sorted(group)
                values = sorted(nums[j] for j in group)
                for pos, val in zip(indices, values):
                    result[pos] = val
                group = []
            group.append(i)
        if group:
            indices = sorted(group)
            values = sorted(nums[j] for j in group)
            for pos, val in zip(indices, values):
                result[pos] = val
        return result