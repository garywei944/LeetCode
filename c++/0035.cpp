class Solution {
   public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size();

        if (target > nums[right - 1]) return right;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
};
