class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;

        for (int i = 0; i < nums.size(); i++) {
            int e = target - nums[i];
            if (mp.contains(e)) {
                return {i, mp[e]};
            }
            mp[nums[i]] = i;
        }
        return {0, 0};
    }
};
