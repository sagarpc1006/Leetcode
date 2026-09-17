import java.util.*;

public class fibonacciusingloop {
    public static void main (String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number : ");
    int n = sc.nextInt();
    sc.close();
    int first_no=0;
    int second_no=1;
    int next_no=0;
    System.out.print("0 1 ");
    for (int i=3;i <= n;i++){
        next_no=first_no+second_no;
        System.out.print(next_no+" ");
        first_no=second_no;
        second_no=next_no;
    }
}

}
