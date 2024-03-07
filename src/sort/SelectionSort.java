package sort;

import java.util.Arrays;
import java.util.stream.IntStream;

public class SelectionSort {

    public static void main(String[] args) {
        int[] arr = IntStream.of(5, 4, 3, 2, 1).toArray();

        Arrays.stream(selectionSort(arr)).forEach(System.out::println);
    }

    public static int[] selectionSort(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            int min = Integer.MAX_VALUE;
            int nowIndex = 0;
            for (int j = i; j < n; j++) {
                if (min > arr[j]) {
                    nowIndex = j;
                    min = arr[j];

                }
            }
            int temp = arr[i];
            arr[i] = arr[nowIndex];
            arr[nowIndex] = temp;
        }

        return arr;
    }

}
