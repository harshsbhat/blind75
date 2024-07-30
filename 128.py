class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if num-1 not in numSet:
                streak = 1
                current = num
                while current+1 in numSet:
                    current += 1
                    streak += 1
                longest = max(longest, streak)
        return longest