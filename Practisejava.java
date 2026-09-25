import java.util.*;

public class Practisejava {
    public static void main(String[] args) {

        fun(1, 2, 3, 4, 5, 5);
    }

    static void fun(int... h) {
        System.out.println(Arrays.toString(h));
    }

    public static int Sum(int n1, int n2) {
        return n1 + n2;
    }

}
