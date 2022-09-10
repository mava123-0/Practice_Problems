#include <math.h>

class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n>0){
            float value = log10 (n) / log10 (4);
            cout<<value;
            if (value - int(value) == 0 ){
                return true;
            }
        }
        return false;
    }
};