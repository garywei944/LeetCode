class Solution {
   public:
    int maxSubarraySumCircular(vector<int>& nums) {
        ios_base::sync_with_stdio(0);
        cin.tie(nullptr);

        int best, worst, top, bot;

        best = top = INT_MIN;
        worst = bot = INT_MAX;

        for (int& x : nums) {
            top = x + max(0, top);
            bot = x + min(0, bot);
            best = max(best, top);
            worst = min(worst, bot);
        }

        return best > 0 ? max(best, reduce(nums.begin(), nums.end()) - worst)
                        : best;
    }
};
