import java.util.*;

class Solution {
    public NestedInteger deserialize(String s) {

        // If the input is just an integer
        if (s.charAt(0) != '[') {
            return new NestedInteger(Integer.parseInt(s));
        }

        Stack<NestedInteger> stack = new Stack<>();
        NestedInteger current = null;

        int num = 0;
        boolean negative = false;
        boolean hasNumber = false;

        for (int i = 0; i < s.length(); i++) {

            char c = s.charAt(i);

            if (c == '[') {
                // Start a new nested list
                stack.push(new NestedInteger());

            } else if (c == '-' || Character.isDigit(c)) {

                // Build the number
                if (c == '-') {
                    negative = true;
                } else {
                    num = num * 10 + (c - '0');
                    hasNumber = true;
                }

            } else if (c == ',' || c == ']') {

                // If we have a number, add it to current list
                if (hasNumber) {
                    if (negative) {
                        num = -num;
                    }

                    stack.peek().add(new NestedInteger(num));

                    num = 0;
                    negative = false;
                    hasNumber = false;
                }

                // Closing bracket
                if (c == ']') {
                    current = stack.pop();

                    // Add the completed list to its parent
                    if (!stack.isEmpty()) {
                        stack.peek().add(current);
                    }
                }
            }
        }

        return current;
    }
}