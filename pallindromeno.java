import java.util.*;

public class pallindromeno {
    static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the positive number :");
        int n = sc.nextInt();
        sc.close();
        pallindrome(n);
    }

    static void pallindrome(int n) {
        int original = n;
        int reversedno = 0;
        while (n != 0) {
            int remainder = n % 10;
            reversedno = reversedno * 10 + remainder;
            n = n / 10;
        }
        if (reversedno == original) {
            System.out.print("It is Pallindrome no");
        } else {
            System.out.print("It is not pallindrome");
        }
    }
}
