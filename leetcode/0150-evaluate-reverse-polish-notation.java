// https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/861149140/

class Solution {
    public int evalRPN(String[] tokens) {
        var s = new Stack<Integer>();

        var ops = Map.<String, BinaryOperator<Integer>>of(
            "+", (a, b) -> a + b,
            "-", (a, b) -> a - b,
            "/", (a, b) -> a / b,
            "*", (a, b) -> a * b
        );

        for (String t: tokens) {
            if (ops.keySet().contains(t)) {
                var r = s.pop();
                var l = s.pop();
                var result = ops.get(t).apply(l, r);
                s.push(result);
            }
            else {
                s.push(Integer.valueOf(t));
            }
        }

        return s.pop();
    }
}
