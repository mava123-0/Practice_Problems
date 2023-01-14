class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valCount = nums.count(val)
        for i in range(valCount):
            nums.pop(nums.index(val))
        return 