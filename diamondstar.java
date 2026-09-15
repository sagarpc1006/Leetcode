public class diamondstar {
    public static void main(String[] args) {
        // Upper half
        for (int i = 1; i <= 4; i++) {
            for (int space = 3; space >= i; space--) {
                System.out.print("  ");
            }
            for (int j = 1; j <= i * 2 - 1; j = j + 1) {
                System.out.print("* ");
            }
            System.out.println();
        }
        // Lower half
        for (int i = 4; i >= 1; i--) {
            for (int space = 3; space >= i; space--) {
                System.out.print("  ");
            }
            for (int j = 1; j <= i * 2 - 1; j = j + 1) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
