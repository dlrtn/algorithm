import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_23882 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        if (!selectionSort(arr, k)) {
            System.out.println("-1");
        }
    }

    public static boolean selectionSort(int[] args, int k) {
        int n = args.length;
        int count = 0;

        for (int i = n - 1; i > 0; i--) {
            int maxIndex = i;
            for (int j = 0; j < i; j++) {
                if (args[maxIndex] < args[j]) {
                    maxIndex = j;
                }
            }
            if (maxIndex != i) {
                count += 1;
                swap(args, i, maxIndex);
            }
            if (count == k) {
                for (int j = 0; j < n; j++) {
                    System.out.print(args[j] + " ");
                }
                return true;
            }
        }
        return false;
    }

    public static void swap(int[] args, int i, int j) {
        int temp = args[i];
        args[i] = args[j];
        args[j] = temp;
    }

}
