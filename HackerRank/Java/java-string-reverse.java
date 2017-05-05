import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        int strlength = A.length();
        int i, j;
        for (i=0, j=strlength-1; i < j; i++, j--) {
            if ( A.charAt(i) != A.charAt(j) ) {
                System.out.println("No");
                return;
            }
        }
        System.out.println("Yes");
    }
}
