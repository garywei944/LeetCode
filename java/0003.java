class Solution {
    public int lengthOfLongestSubstring(String s) {
        int best = 0;
        int start = 0;
        int[] pos = new int[128];

        int n = s.length();

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            start = Math.max(start, pos[c]);
            best = Math.max(best, i - start + 1);
            pos[c] = i + 1;
        }

        return best;
    }
}
