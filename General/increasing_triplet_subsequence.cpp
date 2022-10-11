class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if(size(nums)<3){
            return false;
        }
        int x = INT_MAX, y = INT_MAX;
        for (int i=0; i<size(nums); i++){
            if(nums[i]<=x){
                x=nums[i];
            }
            else if(nums[i]<=y){
                y=nums[i];
            }
            else{
                return true;
            }
        }
        return false;
    }
};