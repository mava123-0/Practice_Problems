class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        comb_list = []

        if (digits == ""):
            return ""

        def sol(num_index,comb):
            if(len(comb) == len(digits)):
                comb_list.append(comb)
                return 

            for i in (char_map[int(digits[num_index])-2]):
                sol(num_index+1, comb+i)


        sol(0,"")
        return comb_list