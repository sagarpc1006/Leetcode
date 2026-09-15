import java.util.*;

public class Practisejava {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no 1 : ");
        int n1 = sc.nextInt();
        System.out.print("Enter no 2 : ");
        int n2 = sc.nextInt();
        System.out.println(Sum(n1, n2));
    }

    public static int Sum(int n1, int n2) {
        return n1 + n2;
    }

}
