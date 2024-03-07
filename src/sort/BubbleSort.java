package sort;

import java.util.Arrays;
import java.util.stream.IntStream;

public class BubbleSort {

    public static void main(String[] args) {
        int[] arr = IntStream.of(5, 4, 3, 2, 1).toArray();

        Arrays.stream(arr).forEach(System.out::println);

        Arrays.stream(bubbleSort(arr)).forEach(System.out::println);


    }

    public static int[] bubbleSort(int[] arr) {
        int n = arr.length;
        int temp;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] > arr[j]) {
                    temp = arr[j];
                    arr[j] = arr[i];
                    arr[i] = temp;
                }
            }
        }

        return arr;
    }

}
