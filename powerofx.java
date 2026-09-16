import java.util.*;
public class powerofx {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the value of base : ");
        int x = sc.nextInt();
        System.out.print("Enter the value of power : ");
        int n = sc.nextInt();
        sc.close();
        System.out.println("Value is : "+Powerofx(x,n));
    }
    public static int Powerofx(int x,int n){
        int result = 1;
        for (int i=1;i<=n;i++){
            result=result*x;
        }
        return result;
    }
}
