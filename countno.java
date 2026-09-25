import java.util.*;

public class countno {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int count_positive=0;
        int count_negative=0;
        int count_zero=0;
        while(true){
            System.out.print("Enter 1 to continue and else to stop : ");
            int n = sc.nextInt();
            if (n==1){
                System.out.print("Enter the number :");
                int n1 = sc.nextInt();
                if (n1>0){
                    count_positive++;
                }
                else if (n1<0){
                    count_negative++;
                }
                else {
                    count_zero++;
                }
            }
            else {
                break;
            }
        }
        sc.close();
        System.out.println("Positive count is :"+ count_positive);
        System.out.println("Negative count is :"+ count_negative);
        System.out.println("Zero count is :"    + count_zero);
    }
}
