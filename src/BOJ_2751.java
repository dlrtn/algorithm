import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2751 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());

        }

        quickSort(arr, 0, arr.length - 1);

        Arrays.stream(arr).forEach(System.out::println);
    }

    public static void quickSort(int[] arr, int i, int j) {
        if (i >= j) {
            return;
        }

        int pivot = i;
        int left = i + 1;
        int right = j;

        while (left <= right) {
            while (left <= j && arr[left] <= arr[pivot]) {
                left++;
            }

            while (arr[right] >= arr[pivot] && right > i) {
                right--;
            }
            System.out.printf("%d %d", left, right);
            if (left > right) {
                swap(arr, right, pivot);
            } else {
                swap(arr, left, right);
            }

            Arrays.stream(arr).forEach(System.out::print);
        }

        quickSort(arr, i, right - 1);
        quickSort(arr, right + 1, j);
    }


    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

}
