// https://leetcode.com/submissions/detail/842196963/

class Solution {
    public String convertToTitle(int n) {
        var sb = new StringBuilder();

        while (n > 0) {
            n -= 1;
            int c = 'A' + n % 26;
            sb.append(Character.toString(c));
            n /= 26;
        }

        return sb.reverse().toString();
    }
}
