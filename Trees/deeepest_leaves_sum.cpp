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
    int deepestLeavesSum(TreeNode* root) {
        
        queue<TreeNode*> node_queue;
        node_queue.push(root);
        
        int level_sum=0;
        
        while(node_queue.size()!=0){
            
            level_sum = 0;
            int queue_size = node_queue.size();
            
            for (int i=0; i<queue_size; i++){
                
                TreeNode *current_node = new TreeNode();
                current_node = node_queue.front();
                node_queue.pop();
                level_sum += current_node->val;
                if (current_node->left!=NULL) node_queue.push(current_node->left);
                if (current_node->right!=NULL) node_queue.push(current_node->right);
                
            }
        }
        
        return level_sum;
        
        }
};