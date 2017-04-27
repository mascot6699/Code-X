import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= 10; i++)
        {
            System.out.printf("%d x %d = %d\n", n , i, n*i);
        }
    }
}
