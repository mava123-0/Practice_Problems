class Solution:
    def isPalindrome(self, s: str) -> bool:
        strVal = ""
        for i in s:
            if(i.isalnum()):
                strVal += i.lower() 
        print(strVal)
        i = 0
        j = len(strVal)-1
        while(i<len(strVal) and j>-1):   
            if(strVal[i] != strVal[j]):
                return False
            i+=1
            j-=1
        return True