class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return {};
        return build(1, n);
    }

    vector<TreeNode*> build(int start, int end) {
        if (start > end) return {nullptr};

        vector<TreeNode*> res;
        for (int i = start; i <= end; i++) {
            vector<TreeNode*> left = build(start, i - 1);
            vector<TreeNode*> right = build(i + 1, end);

            for (auto l : left) {
                for (auto r : right) {
                    TreeNode* root = new TreeNode(i);
                    root->left = l;
                    root->right = r;
                    res.push_back(root);
                }
            }
        }
        return res;
    }
};
