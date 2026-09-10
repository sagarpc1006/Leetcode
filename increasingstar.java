public class increasingstar {
    public static void main(String[] args) {

        // Outer for loop
        for (int i = 1; i <= 5; i++) {
            // Inner space for loop
            for (int space = 5; space > i; space--) {
                System.out.print(" ");
            }
            // Inner star for loop
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}