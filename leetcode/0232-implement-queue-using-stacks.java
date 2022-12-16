// https://leetcode.com/problems/implement-queue-using-stacks/submissions/860723315/

class MyQueue {
    private final Stack<Integer> s1 = new Stack<>();
    private final Stack<Integer> s2 = new Stack<>();
    private int top = 0;
    private boolean push = true;

    public MyQueue() {}

    public void push(int x) {
        if (push != true) {
            int s = s2.size();
            for (int i = 0; i < s; i++) {
                s1.push(s2.pop());
            }
        }

        if (s1.empty()) {
            top = x;
        }

        s1.push(x);
        push = true;
    }

    public int pop() {
        if (push == true) {
            int s = s1.size();
            for (int i = 0; i < s; i++) {
                s2.push(s1.pop());
            }
        }

        int x = s2.pop();
        if (s2.size() > 0) {
            top = s2.peek();
        }
        push = false;
        return x;
    }
    
    public int peek() {
        return top;
    }

    public boolean empty() {
        return s1.empty() && s2.empty();        
    }
}
