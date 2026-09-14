public class butterflystar {
    public static void main(String[] args) {
        // Upper for loop
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= 8; j++) {

                if (j == 1 || j == 8) {
                    System.out.print("* ");
                } else if ((i == 2 && j == 2) || (i == 2 && j == 7)) {
                    System.out.print("* ");
                } else if ((i == 3 && (j == 3 || j == 2)) || (i == 3 && (j == 6 || j == 7))) {
                    System.out.print("* ");

                } else if (i == 4 || i == 5) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }

            }
            System.out.println();
        }
        // Lower for loop
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 8; j++) {
                if (j == 1 || j == 8) {
                    System.out.print("* ");
                } else if ((i == 1 && (j == 2 || j == 3)) || (i == 1 && (j == 6 || j == 7))) {
                    System.out.print("* ");
                } else if (i == 2 && (j == 2 || j == 7)) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }

}
