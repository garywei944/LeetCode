class Solution {
   public:
    int lengthOfLongestSubstring(string s) {
        int best = 0;
        int start = 0;
        auto pos = vector<int>(128);

        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            start = max(start, pos[c]);
            best = max(best, i - start + 1);
            pos[c] = i + 1;
        }

        return best;
    }
};
