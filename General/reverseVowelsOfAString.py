class Solution:
    def reverseVowels(self, s: str) -> str:
        word_arr = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        ptr1,ptr2 = 0,len(word_arr)-1
        
        while(ptr1 < ptr2):
            if(word_arr[ptr1] in vowels and word_arr[ptr2] in vowels):
                word_arr[ptr1], word_arr[ptr2] = word_arr[ptr2], word_arr[ptr1]
                ptr1 +=1
                ptr2 -=1
            if (word_arr[ptr1] not in vowels):
                ptr1+=1
            if (word_arr[ptr2] not in vowels):
                ptr2 -=1
        return ''.join(word_arr)