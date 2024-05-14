class Solution {
   public:
    int maxSubArray(vector<int>& nums) {
        int best = INT_MIN;
        int t = 0;

        for (int i = 0; i < nums.size(); i++) {
            t = nums[i] + max(t, 0);
            best = max(best, t);
        }

        return best;
    }
};
