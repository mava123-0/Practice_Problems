class Solution:
    def longestPalindrome(self, s: str) -> str:
        mem = [-1 for i in range(len(s))]

        def sol(s,index,substr,ans,mem,tabs=""):
            if(substr == ''.join(list(substr[::-1])) and len(substr)>=len(ans)):
                ans = substr

            if(index<0):
                return ans
            
            # if(substr == ''.join(list(substr[::-1])) and len(substr)>=len(ans)):
            #     ans = substr
            
            picked = sol(s,index-1,substr+s[index],ans,mem,tabs+'\t')
            notpicked = sol(s,index-1,substr,ans,mem,tabs+'\t')
            # print(f"{tabs}",picked,notpicked)

            if(len(picked)>len(notpicked)):
                return picked
            return notpicked

        result = sol(s,len(s)-1,"","",[])
        # print("Final",result)
        return result