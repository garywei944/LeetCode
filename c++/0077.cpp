// Bit map approach, I like this one, but only works when n is small
// the problem set n<=20, so it's fine
class Solution {
   public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> t;

        for (int i = 0; i < (1 << n); i++) {
            if (__builtin_popcount(i) != k) continue;
            int idx = 0;
            for (int j = 0; j < n; j++) {
                if (idx == k) break;
                if (i & (1 << j)) {
                    t.push_back(j + 1);
                }
            }
            ans.push_back(t);
            t.clear();
        }
        return ans;
    }
};

// Backtracking approach
class Solution {
   public:
    void helper(int n, int k, int start, vector<vector<int>>& ans,
                vector<int> cur) {
        if (cur.size() == k) {
            ans.push_back(cur);
            return;
        }

        for (int i = start; i <= n; i++) {
            cur.push_back(i);
            helper(n, k, i + 1, ans, cur);
            cur.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> cur;

        helper(n, k, 1, ans, cur);

        return ans;
    }
};
