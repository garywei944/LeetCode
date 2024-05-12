class Solution {
   public:
    string longestCommonPrefix(vector<string> &strs) {
        if (strs.size() == 1) {
            return strs[0];
        }

        sort(strs.begin(), strs.end());

        auto &start = strs.front();
        auto &end = strs.back();
        int n = min(start.size(), end.size());
        for (int i = 0; i < n; i++) {
            if (start[i] != end[i]) {
                return start.substr(0, i);
            }
        }
        return start.substr(0, n);
    }
};
