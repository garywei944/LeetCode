// // DP with O(1) time and O(n) memory
// class Solution {
// public:
//     int numDecodings(string s) {
//         int n = s.length();

//         if (s[0] == '0')
//             return 0;

//         auto dp = vector<int>(n+1);
//         dp[0] = 1;
//         dp[1] = 1;

//         for (int i=2; i<=n; i++){
//             // Add the last charactor
//             if (s[i-1] != '0')
//                 dp[i] += dp[i-1];

//             // Add the last 2 charactors
//             if (s[i-2]=='0')
//                 continue;
//             if (s[i-2]=='1' || (s[i-2]=='2'&&s[i-1]<='6'))
//                 dp[i] += dp[i-2];
//         }

//         return dp[n];
//     }
// };

// O(1) time and O(1) memory
class Solution {
 public:
  int numDecodings(string s) {
    int n = s.length();

    if (s[0] == '0') return 0;

    int rwo2 = 1;
    int rwo1 = 1;
    int r = 1;

    for (int i = 2; i <= n; i++) {
      r = 0;
      // Add the last character
      if (s[i - 1] != '0') r += rwo1;

      // Add the last 2 characters
      if (s[i - 2] == '0')
        ;
      else if (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6')) r += rwo2;
      rwo2 = rwo1;
      rwo1 = r;
    }

    return r;
  }
};
