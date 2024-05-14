static const auto _____ = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();

class Solution {
   public:
    int majorityElement(vector<int>& nums) {
        int ans = INT_MAX, count = 0;

        for (int& x : nums) {
            if (x == ans) {
                count++;
            } else if (count == 0) {
                ans = x;
                count++;
            } else {
                count--;
            }
        }

        return ans;
    }
};
