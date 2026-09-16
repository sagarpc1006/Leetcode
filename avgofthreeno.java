import java.util.*;
public class avgofthreeno {

    public static void main(String[] args) {
        System.out.println("Enter three numbers: ");
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();   
        int n3 = sc.nextInt();
        sc.close();
        System.out.println("Average of three numbers is: " + Average(n1, n2, n3));   
    }
    public static double Average(int n1, int n2, int n3) {
        return ((n1 + n2 + n3) / 3.0);
    }
   
}