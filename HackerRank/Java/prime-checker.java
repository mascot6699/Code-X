import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;

import static java.lang.System.in;

class Prime {
    void checkPrime(int ... elements) {
        for (int i = 0; i < elements.length; i++ ){
            if (Prime.isPrime(elements[i])) {
                System.out.printf("%d ", elements[i]);
            }
        }
        System.out.println();
    }
    static boolean isPrime(int num) {
        if (num < 2) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;
        for (int i = 3; i * i <= num; i += 2)
            if (num % i == 0) return false;
        return true;
    }
}

public class Solution {

    public static void main(String[] args) {
        try{
        BufferedReader br=new BufferedReader(new InputStreamReader(in));
        int n1=Integer.parseInt(br.readLine());
        int n2=Integer.parseInt(br.readLine());
        int n3=Integer.parseInt(br.readLine());
        int n4=Integer.parseInt(br.readLine());
        int n5=Integer.parseInt(br.readLine());
        Prime ob=new Prime();
        ob.checkPrime(n1);
        ob.checkPrime(n1,n2);
        ob.checkPrime(n1,n2,n3);
        ob.checkPrime(n1,n2,n3,n4,n5);
        Method[] methods=Prime.class.getDeclaredMethods();
        Set<String> set=new HashSet<>();
        boolean overload=false;
        for(int i=0;i<methods.length;i++)
        {
            if(set.contains(methods[i].getName()))
            {
                overload=true;
                break;
            }
            set.add(methods[i].getName());
        }
        if(overload)
        {
            throw new Exception("Overloading not allowed");
        }
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
}
