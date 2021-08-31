/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool flipEquiv(struct TreeNode* root1, struct TreeNode* root2){
    if (root2 == NULL && root1 == NULL)
        return true;
    if (!root1 || !root2)
        return false;
    if(flipEquiv(root1->left, root2->left) && flipEquiv(root1->right, root2->right)){
        return root1->val == root2->val;
    }else if(flipEquiv(root1->left, root2->right) && flipEquiv(root1->right, root2->left)){
        return root1->val == root2->val;
    }
    return false;
}