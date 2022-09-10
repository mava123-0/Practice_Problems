#include <math.h>

class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n>0){
            double value = log10 (n) / log10 (3);
            cout<<value;
            if (value - int(value) == 0){
                return true;
            }
        }
        return false;
    }
};