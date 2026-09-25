import java.util.*;
public class greateroftwo {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the two no :");
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        sc.close();
        System.out.print("Greater no is :"+ Greater(n1,n2));

    }
    public static int Greater(int n1,int n2){
        if (n1>n2){
            return n1;
        }
        else {
            return n2;
        }
    }
}
