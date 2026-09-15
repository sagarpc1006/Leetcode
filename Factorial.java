import java.util.*;

public class Factorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the positive no : ");
        int n = sc.nextInt();
        System.out.println(factorial(n));
    }

    public static int factorial(int n) {
        int product = 1;
        for (int i = n; i >= 1; i--) {
            product = product * i;
        }
        return product;
    }
}
