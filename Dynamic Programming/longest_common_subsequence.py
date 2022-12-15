class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def longsol(ind1,ind2,text1,text2,mem):
            if(ind1<0 or ind2<0):
                return 0

            if( mem[ind1][ind2] != -1):
                return mem[ind1][ind2]

            if(text1[ind1] == text2[ind2]):
                mem[ind1][ind2] = 1+longsol(ind1-1,ind2-1,text1,text2,mem)
                return mem[ind1][ind2]
            
            left = longsol(ind1-1,ind2,text1,text2,mem)
            right = longsol(ind1,ind2-1,text1,text2,mem)

            mem[ind1][ind2] =  max(left,right)
            return mem[ind1][ind2]

        mem = [[-1 for i in range(len(text2))] for j in range(len(text1))]
        return longsol(len(text1)-1,len(text2)-1,text1,text2,mem)
