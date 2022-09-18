class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector <int> arr1;
        vector<int> arr2;
        vector<int> ans;
        if(size(nums)!=0){
            for (int i=0; i<size(nums); i++){
                if(i>size(nums)/2 or i==size(nums)/2){
                    arr2.push_back(nums[i]);
                }
                else{
                    arr1.push_back(nums[i]);
                }
            }
            for (int i=0; i<size(nums)/2; i++){
                ans.push_back(arr1[i]);
                ans.push_back(arr2[i]);
            }
        }
        return ans;
    }
};