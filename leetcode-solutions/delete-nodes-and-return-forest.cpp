class Solution {
public:
    vector<TreeNode*> ans;
    
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> to_delete_set(to_delete.begin(), to_delete.end());
        root = dfs(root, to_delete_set);
        if (root)
            ans.push_back(root);
        return ans;
    }

    TreeNode* dfs(TreeNode* curr, unordered_set<int>& to_delete) {
        if (!curr) return nullptr;
        
        curr->left = dfs(curr->left, to_delete);
        curr->right = dfs(curr->right, to_delete);
        
        if (to_delete.count(curr->val)) {
            if (curr->left) ans.push_back(curr->left);
            if (curr->right) ans.push_back(curr->right);
            return nullptr;
        }
        
        return curr;
    }
};
