import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] edges = new int[m][3];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            edges[i][0] = Integer.parseInt(st.nextToken());
            edges[i][1] = Integer.parseInt(st.nextToken());
            edges[i][2] = Integer.parseInt(st.nextToken());
        }

        edges = Arrays.stream(edges).sorted((o1, o2) -> o1[2] - o2[2]).toArray(int[][]::new);

        int max = 0;

        int[] parents = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parents[i] = i;
        }

        int answer = 0;
        for (int i = 0; i < m; i++) {
            int parentA = find(parents, edges[i][0]);
            int parentB = find(parents, edges[i][1]);

            if (parentA != parentB) {
                union(parents, parentA, parentB);
                answer += edges[i][2];
                max = Math.max(max, edges[i][2]);
            }

        }

        System.out.println(answer - max);


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
