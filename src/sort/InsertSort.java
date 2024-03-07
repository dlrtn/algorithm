package sort;

import java.util.Arrays;
import java.util.stream.IntStream;

public class InsertSort {

    public static void main(String[] args) {
        int[] arr = IntStream.of(5, 4, 3, 2, 1).toArray();

        Arrays.stream(insertSort(arr)).forEach(System.out::println);
    }

    public static int[] insertSort(int[] arr) {
        int n = arr.length;
        int j;
        int temp;

        for (int i = 0; i < n - 1; i++) {
            j = i;
            while (j >= 0 && arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                j--;
            }
        }

        return arr;
    }

}
