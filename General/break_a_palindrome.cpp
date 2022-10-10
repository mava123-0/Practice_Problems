class Solution {
public:
    string breakPalindrome(string palindrome) {
        int flag = 0;
        if(palindrome.length()<2){
            return "";
        }
        int i=0;
        while(i<palindrome.length()/2){
            if(palindrome[i]!='a'){
                palindrome[i]='a';
                flag = 1;
                break;
            }
            i++;
        }
        if(flag==0){
            palindrome[(palindrome.length())-1] = 'b';
        }
        return palindrome;
    }
};