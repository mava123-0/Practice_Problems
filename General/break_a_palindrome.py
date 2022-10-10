class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        arr = palindrome
        if(len(arr)==1):
            return ""
        i = len(arr)-2
        for i in range(len(arr)//2):
            if(arr[i]!='a'):
                return str(arr[:i]+'a'+arr[i+1:])
        return arr[:-1]+'b'