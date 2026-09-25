from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = Counter(nums)
        print(frequency)

        for k, v in frequency.items():
            if v > 1:
                return True
        return False