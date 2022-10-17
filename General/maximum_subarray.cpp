class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size()==1){
            return nums[0];
        }
        int ans = nums[0];
        vector<int> ans_arr;
        ans_arr.push_back(ans);
        nums.erase(nums.begin());
        for (auto x : nums){
            ans = ans+x;
            ans = max(ans,x);
            ans_arr.push_back(ans);
        }
        int x = *max_element(ans_arr.begin(),ans_arr.end() );
        return x;
    }
};