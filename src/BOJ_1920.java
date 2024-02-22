import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1920 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[] a = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int[] b = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        int[] sortedArray = Arrays.stream(a).sorted().toArray();

        Arrays.stream(b).forEach((number) -> {
            if (binarySearch(sortedArray, number, 0, sortedArray.length)) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        });
    }

    public static boolean binarySearch(int[] arr, int number, int i, int j) {
        int m = (i + j) / 2;

        if (arr[m] == number) {
            return true;
        } else if (i == m) {
            return false;
        } else if (arr[m] > number) {
            return binarySearch(arr, number, i, m);
        } else {
            return binarySearch(arr, number, m, j);
        }
    }
}
