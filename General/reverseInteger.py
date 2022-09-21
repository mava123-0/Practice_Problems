class Solution:
    def reverse(self, x: int) -> int:
        num_list = list(str(x))
        sign_flag = 0
        if(num_list[0] == '-'):
            sign_flag = 1
        num_list.reverse()
        ans = 0
        for num in num_list:
            if(num != '-'):
                ans = ans*10 + int(num)
        print(2**31)
        print(- (2**31))
        if (sign_flag == 0 and not ans > 2**31):
            return ans
        elif (sign_flag == 1 and not int('-' + str(ans)) < -(2**31)):
            return int('-' + str(ans))
        else:
            return 0