import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_21938 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        double[][] preprocessingMap = new double[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < m; j++) {
                double tempSum = Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken())
                        + Integer.parseInt(st.nextToken());
                preprocessingMap[i][j] = tempSum / 3;
            }
        }

        st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (preprocessingMap[i][j] >= t) {
                    preprocessingMap[i][j] = 1;
                } else {
                    preprocessingMap[i][j] = 0;
                }
            }
        }
        int count = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (preprocessingMap[i][j] == 1) {
                    count++;
                    dfs(i, j, preprocessingMap);
                }
            }
        }

        System.out.println(count);
    }

    public static void dfs(int y, int x, double[][] graph) {
        if (x < graph[0].length - 1 && graph[y][x + 1] == 1) {
            graph[y][x + 1] = 0;
            dfs(y, x + 1, graph);
        }
        if (y < graph.length - 1 && graph[y + 1][x] == 1) {
            graph[y + 1][x] = 0;
            dfs(y + 1, x, graph);
        }
        if (x > 0 && graph[y][x - 1] == 1) {
            graph[y][x - 1] = 0;
            dfs(y, x - 1, graph);
        }
        if (y > 0 && graph[y - 1][x] == 1) {
            graph[y - 1][x] = 0;
            dfs(y - 1, x, graph);
        }
    }
}
