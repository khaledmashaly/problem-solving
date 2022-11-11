// https://leetcode.com/submissions/detail/841486857/

class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        int j = 1;

        while (j < nums.length) {
            if (nums[i] != nums[j]) {
                i += 1;
                nums[i] = nums[j];
            }

            j += 1;
        }

        return i + 1;
    }
}
