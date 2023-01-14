class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(x) for x in digits]
        digVal = ''.join(digits)
        ans = []
        digVal = int(digVal)+1
        for i in str(digVal):
            ans.append(int(i))
        return ans