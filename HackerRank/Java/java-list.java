import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList arr = new ArrayList();
        int n = sc.nextInt();
        for(int i=0; i<n; i++) {
            arr.add(i,sc.nextInt());
        }
        int q = sc.nextInt();
        for(int i=0; i<q; i++) {
            String s = sc.next();
            if(s.equals("Insert")) {
                 int x = sc.nextInt();
                 int y = sc.nextInt();
                 arr.add(x, y);
            } else if(s.equals("Delete")) {
                int x = sc.nextInt();
                arr.remove(x);
            }
        }
        Iterator it = arr.iterator();
        while(it.hasNext()) {
            System.out.print(it.next() + " ");
        }
    }
}
