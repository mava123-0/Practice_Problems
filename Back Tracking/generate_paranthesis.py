class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def sol(comb):
            if(len(comb) == 2*n):
                if(comb[0] == ')'):
                    return

                # check if correct and append to result array
                count = 0
                for i in comb:
                    if i == '(':
                        count+=1
                    else:
                        count-=1
                    if(count<0):
                        return
               
                if(count == 0):
                    res.append(comb)
                return 

            front = sol(comb + '(')
            back = sol(comb + ')')

        sol("")
        return res