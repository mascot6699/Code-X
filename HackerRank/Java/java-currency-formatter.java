import java.util.*;
import java.text.*;

public class Solution {

    public static String formattedCurrency(String language, String country, Double amount) {
        return NumberFormat.getCurrencyInstance(new Locale(language, country)).format(amount);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        System.out.println("US: " + Solution.formattedCurrency("en","US", payment));
        System.out.println("India: " + Solution.formattedCurrency("en","IN", payment));
        System.out.println("China: " + Solution.formattedCurrency("zh","CN", payment));
        System.out.println("France: " + Solution.formattedCurrency("fr","FR", payment));
    }
}

