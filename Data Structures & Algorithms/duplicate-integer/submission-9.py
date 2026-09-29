class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_set = set()
        for a in range(0, len(nums)):
            nums_set.add(nums[a])
        if len(nums) == len(nums_set):
            return False
        else:
            return True    

                    