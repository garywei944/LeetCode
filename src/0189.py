class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums) - k
        nums[:l] = nums[:l][::-1]
        nums[l:] = nums[l:][::-1]
        nums.reverse()
