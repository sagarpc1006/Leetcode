public class solidrhombus {
    public static void main(String[] args) {
        // Outer for loop
        for (int i = 1; i <= 5; i++) {

            // Inner for loop for space
            for (int space = 5; space > i; space--) {
                System.out.print("  ");
            }

            // Inner for loop for star
            for (int j = 1; j <= 5; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
