class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mem = [-1 for _ in range(len(costs))]

        def dp_sol(costs,coins_left,index,curr_num):
            if(index <= 0):
                if(costs[index] <= coins_left):
                    return curr_num + 1
                else:
                    return curr_num
            
            elif(mem[index] != -1):
                return mem[index]
            
            else:
                picked = 0

                if(costs[index] <= coins_left):
                    picked = dp_sol(costs,coins_left - costs[index],index-1,curr_num+1)

                notpicked = dp_sol(costs,coins_left,index-1,curr_num)

            return max(picked,notpicked)

        res = dp_sol(costs,coins,len(costs)-1,0)
        # print(res)
        return res	