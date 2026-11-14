import java.util.Scanner;

public class Practise {
    static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of array : ");
        int size = sc.nextInt();

        int[] arr = new int[size];

        // Enter elements in an array
        for (int i = 0; i < size; i++) {
            System.out.print("Enter the element at index " + i + " : ");
            arr[i] = sc.nextInt();
        }
        sc.close();
        System.out.print("The array is : ");
        // Print the elements
        for (int i = 0; i < size; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
