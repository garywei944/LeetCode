class Solution {
   public:
    void dfs(int target, int start_idx, vector<int>& path, vector<int>& cands,
             vector<vector<int>>& ans) {
        if (target == 0) {
            ans.push_back(path);
            return;
        } else if (target < 0) {
            return;
        }

        for (int i = start_idx; i < cands.size(); i++) {
            path.push_back(cands[i]);
            dfs(target - cands[i], i, path, cands, ans);
            path.pop_back();
        }
    }

   private:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> path;
        vector<vector<int>> ans;

        sort(candidates.begin(), candidates.end());
        dfs(target, 0, path, candidates, ans);

        return ans;
    }
};
