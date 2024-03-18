import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2470 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int i = 0;
        int j = n - 1;

        int[] answer = new int[2];
        int min = Integer.MAX_VALUE;

        arr = Arrays.stream(arr).sorted().toArray();

        while (i < j) {
            int sum = arr[i] + arr[j];
            if (Math.abs(sum) < min) {
                answer[0] = arr[i];
                answer[1] = arr[j];
                min = Math.abs(sum);
            }

            if (sum > 0) {
                j -= 1;
            } else {
                i += 1;
            }
        }

        System.out.printf("%d %d", answer[0], answer[1]);
    }

}
