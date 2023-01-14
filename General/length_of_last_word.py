class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_list = s.split()
        return len(str_list[-1])