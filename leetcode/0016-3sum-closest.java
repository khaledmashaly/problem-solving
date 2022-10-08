// https://leetcode.com/submissions/detail/818021900/


class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length;
        Arrays.sort(nums);
        int ans = Integer.MAX_VALUE;

        for (int i = 0; i < n - 2; i++) {
            int l = i + 1;
            int r = n - 1;
            int t = target - nums[i];

            while (l < r) {
                if (nums[l] + nums[r] == t) {
                    return target;
                }

                int s = nums[i] + nums[l] + nums[r];

                if (Math.abs(target - s) < Math.abs(target - ans)) {
                    ans = s;
                }

                if (nums[l] + nums[r] > t) {
                    r--;
                }
                else {
                    l++;
                }
            }
        }

        return ans;
    }
}
