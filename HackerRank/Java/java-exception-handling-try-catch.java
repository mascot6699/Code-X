import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        int inputFlag, zeroFlag, x1, x2;
        inputFlag = zeroFlag = x1 = x2 = 0;
        Scanner sc = new Scanner(System.in);

        String x = sc.next();
        String y = sc.next();

        try {
            x1 = Integer.parseInt(x);
            x2 = Integer.parseInt(y);
        } catch (Exception ec) {
            inputFlag = 1;
        }

        if (x2 == 0) zeroFlag = 1;
        if (inputFlag == 1)
            System.out.println("java.util.InputMismatchException");
        else if (zeroFlag == 1)
            System.out.println("java.lang.ArithmeticException: / by zero");
        else
            System.out.printf("%d", x1/x2);
    }
}
