/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
   public:
    void inorder(TreeNode* node, vector<int>& arr) {
        if (node == nullptr) return;
        inorder(node->left, arr);
        arr.push_back(node->val);
        inorder(node->right, arr);
    }
    int getMinimumDifference(TreeNode* root) {
        auto arr = vector<int>();

        inorder(root, arr);

        int ans = INT_MAX;
        for (int i = 0; i < arr.size() - 1; i++) {
            ans = min(ans, arr[i + 1] - arr[i]);
        }

        return ans;
    }
};
