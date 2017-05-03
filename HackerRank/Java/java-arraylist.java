import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int d, q, x, y;
        ArrayList[] arr = new ArrayList[n];
        for(int i=0; i<n; i++){
            d = in.nextInt();
            arr[i] = new ArrayList();
            for(int j=0; j<d; j++){
                arr[i].add(in.nextInt());
            }
        }
        q = in.nextInt();
        for(int i=0; i<q; i++){
            x = in.nextInt();
            y = in.nextInt();
            try {
                System.out.println(arr[x-1].get(y-1));
            } catch(Exception e){
                System.out.println("ERROR!");
            }
        }
    }
}
