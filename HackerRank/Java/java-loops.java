import java.util.*;
import java.io.*;

class Solution {

    public static void printSeries(int a, int b, int n) {
        int element = a;
        for (int j = 0; j < n; j++) {
            element += (int) (Math.pow(2.0, j) * b);
            System.out.printf("%d ", element);
        }
        System.out.println();
    }

    public static void main(String []argh) {
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            Solution.printSeries(a, b, n);
        }
        in.close();
    }
}

