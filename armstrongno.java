import java.util.*;

public class armstrongno {
    static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the positive number :");
        int n = sc.nextInt();
        sc.close();
        armstrong(n);
    }

    static void armstrong(int n) {
        int original = n;
        int remainder = 0;
        int sum = 0;
        while (n > 0) {
            remainder = n % 10;
            n = n / 10;
            sum = sum + remainder * remainder * remainder;
        }
        if (sum == original) {
            System.out.print("It is armstrong no :");
        } else {
            System.out.print("It is not armstrong no :");
        }
    }
}
