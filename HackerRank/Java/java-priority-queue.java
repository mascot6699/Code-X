import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Student{
   private int token;
   private String fname;
   private double cgpa;
   public Student(int id, String fname, double cgpa) {
      super();
      this.token = id;
      this.fname = fname;
      this.cgpa = cgpa;
   }
   public int getToken() {
      return token;
   }
   public String getFname() {
      return fname;
   }
   public double getCgpa() {
      return cgpa;
   }
   @Override
   public String toString() {
     return this.getFname();
   }
}

public class Solution {

    public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      PriorityQueue<Student> pq = new PriorityQueue<>(
                Comparator.comparing(Student::getCgpa).reversed()
                        .thenComparing(Student::getFname)
                        .thenComparing(Student::getToken));
      int totalEvents = Integer.parseInt(in.nextLine());
      while(totalEvents>0){
         String event = in.next();
         switch(event){
             case "ENTER":
                String name = in.next();
                double cgpa = in.nextDouble();
                int token = in.nextInt();
                pq.offer(new Student(token, name, cgpa));
                break;
             case "SERVED":
                pq.poll();
         }
         totalEvents--;
      }

      if(pq.isEmpty())
          System.out.println("EMPTY");
      while(!pq.isEmpty())
          System.out.println(pq.poll());
    }
}

