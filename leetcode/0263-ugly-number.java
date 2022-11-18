// https://leetcode.com/submissions/detail/845896153/

class Solution {
    public boolean isUgly(int n) {
        int[] ugly = new int[] {2, 3, 5};

        for (int factor: ugly) {
            while (n > 1 && n % factor == 0) {
                n /= factor;
            }
        }

        return n == 1;
    }
}
