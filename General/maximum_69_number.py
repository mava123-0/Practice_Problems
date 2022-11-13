class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list = list(str(num))
        for x in range (len(num_list)):
            if int(num_list[x]) == 6:
                num_list[x] = '9'
                break
        return ''.join(num_list)