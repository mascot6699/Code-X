import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine().trim();
        String[] tokens = input.split("[^\\p{Alpha}]+");

        int size = (input.isEmpty()) ? 0 : tokens.length;
        System.out.println(size);

        for(String token : tokens) {
            System.out.println(token);
        }
        scan.close();
    }
}

