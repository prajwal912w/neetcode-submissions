class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_arr = set(nums)

        if len(nums) != len(set_arr):
            return True

        return False