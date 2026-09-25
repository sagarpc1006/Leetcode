public class functionoverloading {
    static void main(String args[]) {
        fun(2);
        fun("Sagar");
    }

    static void fun(int a) {
        System.out.println(a);
    }

    static void fun(String name) {
        System.out.println(name);
    }
}
