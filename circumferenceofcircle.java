import java.util.*;

public class circumferenceofcircle {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the radius : ");
        int r = sc.nextInt();
        sc.close();
        System.out.print("Circumference is :"+ Circumference(r));
    }
    public static double Circumference(int r){
        return 2*3.14*r;
    }
}
