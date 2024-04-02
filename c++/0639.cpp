unsigned int MOD = 1e9 + 7;
unsigned int AA = 15;

class Solution {
   public:
    int numDecodings(string s) {
        int n = s.length();

        // Base cases
        if (s[0] == '0')
            return 0;
        else if (n == 1)
            return s[0] == '*' ? 9 : 1;

        auto dp = vector<long long>(n + 1);
        dp[0] = 1;
        dp[1] = s[0] == '*' ? 9 : 1;

        char c2, c1;
        long long e;

        for (int i = 2; i <= n; i++) {
            c2 = s[i - 2];
            c1 = s[i - 1];

            e = dp[i - 1];
            // Add the last character
            if (c1 != '0') {
                if (c1 == '*')
                    dp[i] += (9 * e)%MOD;
                else
                    dp[i] += e;
            }
            dp[i] %= MOD;
            e = dp[i-2];

            // Add the last 2 characters
            if (c2 == '0') continue;
            // 6 cases: ** *x x* xx x0 *0
            if (c1 == '*' && c2 == '*') {
                // **
                dp[i] += (AA * e)%MOD;
            } else if (c2 == '*') {
                if (c1 <= '6') {
                    // *0 *x
                    dp[i] += e*2;
                }
                else {
                    // *x
                    dp[i] += e;
                }
            }
            else{
                // x* xx x0
                if (c1=='*'){
                    // x*
                    if (c2 == '1') dp[i] += 9*e;
                    else if (c2 == '2') dp[i] += 6*e;
                }
                else if (c1 == '0'){
                    // x0
                    if (c2 <= '2') dp[i] += e;
                }
                else {
                    // xx
                    if (c2 == '1' || (c2 == '2' && c1 <='6')) dp[i] +=e;
                }
            }

            dp[i] %= MOD;
        }

        return dp[n];
    }
};
