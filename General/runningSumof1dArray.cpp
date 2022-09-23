class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int sum = 0;
        for (int i=0; i<size(nums); i++){
            sum += nums[i];
            nums[i] = sum;
        }
        return nums;
    }
};