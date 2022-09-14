/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        queue<TreeNode*> arr;
        vector<double> ans;
        if(root!=NULL){
            arr.push(root);
            double sum = 0;
            while(arr.size()!=0){
                sum = 0;
                int qlen = arr.size();
                for (int i=0; i < qlen; i++){
                    TreeNode* curnode = arr.front(); 
                    arr.pop();
                    sum += curnode->val;
                    if(curnode->left!=NULL) arr.push(curnode->left);
                    if(curnode->right!=NULL) arr.push(curnode->right);
                }
                ans.push_back(sum/qlen);
            }
        }
        return ans;
    }
};