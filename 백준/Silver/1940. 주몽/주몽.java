import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        int m = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        arr = Arrays.stream(arr).sorted().toArray();

        int i = 0;
        int j = n - 1;

        int answer = 0;
        while (i < j) {
            int sum = arr[i] + arr[j];

            if (sum == m) {
                answer++;
                i++;
                j--;
            } else if(sum < m) {
                i++;
            } else {
                j--;
            }
        }

        System.out.println(answer);
    }

}
