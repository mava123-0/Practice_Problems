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
    int count = 0;
    
    void nodeCount(TreeNode* root, int curmax){
        if(curmax <= root->val){
            count += 1;
            curmax = root->val;
        }
        if(root->left){
            nodeCount (root->left, curmax);
        }
        if(root->right){
            nodeCount (root->right, curmax);
        }
        return;
    }
    
    int goodNodes(TreeNode* root) {
        if(root != NULL){
            nodeCount(root,root->val);
        }
        return count;
    }
};