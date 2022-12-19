class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        n = len(s)
        
        for i in range(len(s)):
            l,r = i,i
            temp = ""
            # print("\nFIRST")
            while(s[l]==s[r]):
                temp = s[l:r+1]
                # print(temp,s[l],s[r])
                l -= 1
                r += 1
                if(l<0 or r>n-1):
                    break
            # print(temp)
            if(len(temp)>len(res)):
                res = temp
                # print("res updated",res)
                resLen = len(temp)

            l,r = i,i+1
            temp = ""
            # print("\nSECOND")
            while(l>=0 and r<n and s[l]==s[r]):
                temp = s[l:r+1]
                # print(temp,s[l],s[r])
                l -= 1
                r += 1
                if(l<0 or r>n-1):
                    break
            # print(temp)
            if(len(temp)>len(res)):
                res = temp
                # print("res updated",res)
                resLen = len(temp)
        return res