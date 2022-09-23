class Solution {
public:
    void reverseString(vector<char>& s) {
        int start = 0, temp;
        int end = size(s)-1;
        while(start<=end){
            temp = s[start];
            s[start] = s[end];
            s[end] = temp;
            start +=1;
            end -= 1;
        }
    }
};