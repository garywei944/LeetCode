class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    int n = s.length();
    int best = 0;
    int start = 0;
    auto pos = vector<int>(128);

    for (int i = 0; i < n; i++) {
      char c = s[i];
      start = max(start, pos[c]);
      best = max(best, i - start + 1);
      pos[c] = i + 1;
    }

    return best;
  }
};
