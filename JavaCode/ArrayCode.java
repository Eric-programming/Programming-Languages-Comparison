import java.util.*;

public class ArrayCode {
    public static void main(String[] args) {
        demo();
    }

    public static void demo() {
        // Initize 1D array
        int[] arr = { 1, 2, 3 };
        arr = new int[] { 3, 2, 1 };

        // Initize 1D array to x
        int n = 5, x = 3;
        int[] arr1 = new int[n];
        Arrays.fill(arr1, x); // Expect [3,3,3,3,3]

        // Initize 2D array to x
        int m = n;
        int[][] arr2 = new int[m][n];
        for (int[] row : arr2) {
            Arrays.fill(row, x);
        }
        // Expect [3,3,3,3,3] * 5

        // Initize 3D array to x
        int k = n;
        int[][][] arr3 = new int[k][m][n];
        for (int[][] matrix : arr3) {
            for (int[] row : matrix) {
                Arrays.fill(row, x);
            }
        }
        // Expect [3,3,3,3,3] * 5 * 5
    }
}