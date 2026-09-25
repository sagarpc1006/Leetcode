public class arraycallbyreference {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4 };
        value_change(a);
        System.out.println(a[0]);

    }

    static void value_change(int[] a) {
        a[0] = 99;
    }
}
