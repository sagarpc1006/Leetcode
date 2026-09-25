import java.util.*;

public class primeno {
    static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the positive no : ");
        int n = sc.nextInt();
        sc.close();
        prime(n);
    }

    static void prime(int n) {
        boolean isprime = true;
        if (n == 0) {
            System.out.println("Not prime");
        } else if (n == 1) {
            System.out.println("Prime");
        } else {
            for (int i = 2; i < n; i++) {
                if (n % i == 0) {
                    System.out.println("No is not prime");
                    isprime = false;
                    break;
                }

            }

        }
        if (isprime) {
            System.out.println("No is prime");
        }
    }

}
