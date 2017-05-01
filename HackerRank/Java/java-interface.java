import java.util.*;
interface AdvancedArithmetic{
  int divisor_sum(int n);
}

class MyCalculator implements AdvancedArithmetic {
    public int divisor_sum(int n){
        int sum = 0;
        if (n == 1)
            return 1;
        else
            sum = 1 + n;
        int loop = (int)Math.sqrt(n);
        for(int i = 2; i <= loop; i++)
        {
            if(n % i == 0)
            {
               sum += i;
               int d = n/i;
               if(d!=i)
                  sum+=d;
            }
        }
        return sum;
    }
}

class Solution{
    public static void main(String []args){
        MyCalculator my_calculator = new MyCalculator();
        System.out.print("I implemented: ");
        ImplementedInterfaceNames(my_calculator);
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.print(my_calculator.divisor_sum(n) + "\n");
        sc.close();
    }
    /*
     *  ImplementedInterfaceNames method takes an object and prints the name of the interfaces it implemented
     */
    static void ImplementedInterfaceNames(Object o){
        Class[] theInterfaces = o.getClass().getInterfaces();
        for (int i = 0; i < theInterfaces.length; i++){
            String interfaceName = theInterfaces[i].getName();
            System.out.println(interfaceName);
        }
    }
}
