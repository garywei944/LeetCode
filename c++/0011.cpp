class Solution {
   public:
    int maxArea(vector<int>& height) {
        std::ios_base::sync_with_stdio(false);
        std::cin.tie(nullptr);
        std::cout.tie(nullptr);

        int i = 0;
        int j = height.size() - 1;
        int best = 0;

        while (i < j) {
            best = max(best, (j - i) * min(height[i], height[j]));
            if (height[i] < height[j])
                i++;
            else
                j--;
        }

        return best;
    }
};
