import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        String str = scan.next();
        int k = scan.nextInt();
        String smallest, largest;
        smallest = largest = str.substring(0, k);
        for(int i = 1; i <= str.length() - k; i++) {
            String sub = str.substring(i, i+k);
            if (smallest.compareTo(sub) > 1) {
                smallest = sub;
            }
            if (largest.compareTo(sub) < 1) {
                largest = sub;
            }
        }
        System.out.println(smallest);
        System.out.println(largest);
    }
}
