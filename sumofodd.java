import java.util.*;
public class sumofodd {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number : ");
        int n = sc.nextInt();
        sc.close();
        System.out.print("Sum is :"+ Sumofodd(n));

    }
    public static int Sumofodd(int n){
        int sum=0;
        for (int i=1 ; i<=n;i++)
        {
            if (i%2!=0){
                sum=sum+i;
            }
            
        }
        return sum;
    }

}
