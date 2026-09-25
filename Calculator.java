// Calculator code  
package Leetcode;

import java.util.*;

public class Calculator {
    public static void main(String[] args) {
        // Input choice for switch case
        System.out.println("Enter 1 for addition :");
        System.out.println("Enter 2 for substraction :");
        System.out.println("Enter 3 for multiplication :");
        System.out.println("Enter 4 for division :");

        Scanner sc = new Scanner(System.in);
        int choice = sc.nextInt();
        // Input first number
        System.out.print("Enter first no :");
        int n1 = sc.nextInt();
        // Input second number
        System.out.print("Enter second no :");
        int n2 = sc.nextInt();

        switch (choice) {
            case 1:
                System.out.print("Addition is : ");
                System.out.print(n1 + n2);
                break;
            case 2:
                System.out.print("Substraction is :");
                System.out.print(n1 - n2);
                break;
            case 3:
                System.out.print("Multiplication is :");
                System.out.print(n1 * n2);
                break;
            case 4:
                System.out.print("Division is :");
                System.out.print(n1 / n2);
                break;
            default:
                System.out.print("Invalid Choice");
        }
        sc.close();

    }

}
