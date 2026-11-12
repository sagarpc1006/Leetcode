import java.util.*;
/* 
public class twodarray {
    static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the no of rows : ");
        int row = sc.nextInt();
        System.out.print("Enter the no of columns : ");
        int col = sc.nextInt();

        int[][] arr = new int[row][col];

        for (int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                arr[i][j]=sc.nextInt();
            }
        }
        sc.close();
        for (int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
}
*/
public class twodarray {
    static void main(String args[]){
        int[] arr = {1,2,3,4,5};
        for (int i=arr.length-1;i>=0;i--){
            System.out.println(arr[i]);
        }
    }
}



class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> list = new ArrayList<>();
        for (int i=1;i<=n;i++){
            if (i%3==0 && i%5==0){
                list.add("FizzBuzz");
            }
            else if (i%3==0){
                list.add("Fizz");
            }
            else if (i%5==0){
                list.add("Buzz");
            }
            else {
                list.add
            }

        }
        return list;

    }
}