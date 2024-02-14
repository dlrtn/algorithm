import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_17123 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int[][] arr = new int[N][N];
            int[] rows = new int[N];
            int[] cols = new int[N];

            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < N; k++) {
                    int val = Integer.parseInt(st.nextToken());
                    arr[j][k] = val;
                    rows[j] += val;
                    cols[k] += val;
                }
            }

            for (int x = 0; x < M; x++) {
                st = new StringTokenizer(br.readLine());
                int r1 = Integer.parseInt(st.nextToken()) - 1;
                int c1 = Integer.parseInt(st.nextToken()) - 1;
                int r2 = Integer.parseInt(st.nextToken()) - 1;
                int c2 = Integer.parseInt(st.nextToken()) - 1;
                int v = Integer.parseInt(st.nextToken());

                for (int r = r1; r <= r2; r++) {
                    rows[r] += (c2 - c1 + 1) * v;
                }

                for (int c = c1; c <= c2; c++) {
                    cols[c] += (r2 - r1 + 1) * v;
                }
            }

            for (int temp = 0; temp < N; temp++) {
                sb.append(rows[temp] + " ");
            }
            sb.append('\n');
            for (int temp = 0; temp < N; temp++) {
                sb.append(cols[temp] + " ");
            }
            sb.append('\n');
        }

        System.out.println(sb);

    }

}
