import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Locale locale = new Locale("en");
        Calendar cal= Calendar.getInstance();
        Scanner in = new Scanner(System.in);

        int month = in.nextInt();
        int day = in.nextInt();
        int year = in.nextInt();

        cal.set(year, month-1, day);
        System.out.println(cal.getDisplayName(
            Calendar.DAY_OF_WEEK, // get the day of the week
            Calendar.LONG,        // get the full long name format
            locale                // in *English locale
        ).toUpperCase());      // uppercase the answer
    }
}

