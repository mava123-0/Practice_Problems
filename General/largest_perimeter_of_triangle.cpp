class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        int n = sizeof(nums)/sizeof(nums);
        sort(nums.begin(),nums.end());
        for (int i=nums.size()-3; i>-1; i--){
            if(nums[i+1]+nums[i] > nums[i+2] ){
                return nums[i+1]+nums[i+2]+nums[i];
            }
        }
        return 0;
    }
};