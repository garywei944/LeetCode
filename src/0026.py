class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = -1
        curr = None
        for num in nums:
            if num != curr:
                curr = num
                n+=1
                nums[n] = curr
        return n+1
