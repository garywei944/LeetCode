class Solution {
   public:
    int jump(vector<int>& nums) {
        int jumps = 0;
        int best_curr = 0;
        int best_next = 0;

        for (int i = 0; i < nums.size() - 1; i++) {
            best_next = max(best_next, i + nums[i]);
            if (i == best_curr) {
                jumps++;
                best_curr = best_next;
            }
        }
        return jumps;
    }
};
