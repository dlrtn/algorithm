import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1922 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());

        int[][] lines = new int[m][3];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            lines[i][0] = Integer.parseInt(st.nextToken());
            lines[i][1] = Integer.parseInt(st.nextToken());
            lines[i][2] = Integer.parseInt(st.nextToken());
        }

        lines = Arrays.stream(lines).sorted((o1, o2) -> o1[2] - o2[2]).toArray(int[][]::new);

        int[] parents = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parents[i] = i;
        }

        int answer = 0;
        for (int i = 0; i < m; i++) {
            int parentA = find(parents, lines[i][0]);
            int parentB = find(parents, lines[i][1]);

            if (parentA != parentB) {
                union(parents, parentA, parentB);
                answer += lines[i][2];
            }

        }
        System.out.println(answer);
    }

    private static int find(int[] parents, int x) {
        if (parents[x] == x) {
            return x;
        }
        return parents[x] = find(parents, parents[x]);
    }

    private static void union(int[] parents, int x, int y) {
        int parentX = find(parents, x);
        int parentY = find(parents, y);

        if (parentX != parentY) {
            if (parentX < parentY) {
                parents[parentY] = parentX;
            } else {
                parents[parentX] = parentY;
            }
        }
    }

}
