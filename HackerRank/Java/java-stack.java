import java.util.*;

class Solution {
    private static final Deque<Character> stack = new ArrayDeque<>();

    private static boolean isBalanced(String str) {
        stack.clear();
        int len = str.length();
        boolean failed = false;
        for (int ix = 0; !failed && ix < len; ++ix) {
            char currChar = str.charAt(ix);
            switch (currChar) {
                case '(':
                case '[':
                case '{':
                    stack.addFirst(currChar);
                    break;
                case ']':
                    failed = stack.size() == 0 || (stack.removeFirst() != '[');
                    break;
                case ')':
                    failed = stack.size() == 0 || (stack.removeFirst() != '(');
                    break;
                case '}':
                    failed = stack.size() == 0 || (stack.removeFirst() != '{');
                    break;
                default:
                    failed = true;
                    break;
            }
        }
        failed |= (stack.size() != 0);
        return !failed;
    }

   public static void main(String []argh)
   {
      Scanner sc = new Scanner(System.in);

      while (sc.hasNext()) {
         String input=sc.next();
         System.out.println(Solution.isBalanced(input));
      }

   }
}

