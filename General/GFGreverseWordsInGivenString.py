class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        arr = S.split('.')
        arr.reverse()
        # return arr2
        return '.'.join(arr)