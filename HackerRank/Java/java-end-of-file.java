import java.io.*;
import java.util.*;

public class Solution {

    static int COUNT = 1;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()){
            System.out.printf("%d %s\n", COUNT++, sc.nextLine());
        }
        sc.close();
    }
}
