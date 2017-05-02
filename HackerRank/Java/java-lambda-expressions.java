import java.io.*;
import java.util.*;

interface PerformOperation {
   boolean check(int a);
}

class MyMath {
    
    public static boolean checker(PerformOperation p, int num) {
        return p.check(num);
    }

    public static PerformOperation is_odd(){
        return (a) -> a % 2 != 0;
    }

    public static PerformOperation is_prime(){
        return (a) -> java.math.BigInteger.valueOf(a).isProbablePrime(1);
    }

    public static PerformOperation is_palindrome(){
        return (a) ->  { 
            String str1 = Integer.toString(a);
            return str1.equals(new StringBuilder(str1).reverse().toString());
        };
    }
}

public class Solution {

   public static void main(String[] args) throws IOException {

      MyMath ob = new MyMath();
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int T = Integer.parseInt(br.readLine());
      PerformOperation op;
      boolean ret = false;
      String ans = null;

      while (T--> 0) {
         String s = br.readLine().trim();
         StringTokenizer st = new StringTokenizer(s);
         int ch = Integer.parseInt(st.nextToken());
         int num = Integer.parseInt(st.nextToken());
         if (ch == 1) {
            op = ob.is_odd();
            ret = ob.checker(op, num);
            ans = (ret) ? "ODD" : "EVEN";
        } else if (ch == 2) {
            op = ob.is_prime();
            ret = ob.checker(op, num);
            ans = (ret) ? "PRIME" : "COMPOSITE";
        } else if (ch == 3) {
            op = ob.is_palindrome();
            ret = ob.checker(op, num);
            ans = (ret) ? "PALINDROME" : "NOT PALINDROME";
        }
        System.out.println(ans);
    }
}
}
