import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_23827 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] arr = new long[n];
        long[] cur = new long[n];
        long answer = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
            cur[i] = arr[i];
        }

        for (int i = 1; i < n; i++) {
            cur[i] = (cur[i] + cur[i - 1]) % 1000000007;
        }

        for (int i = 0; i < n - 1; i++) {
            answer += ((cur[n - 1] - cur[i]) * arr[i]) % 1000000007;
            answer %= 1000000007;
        }

        System.out.println(answer);
    }

}
