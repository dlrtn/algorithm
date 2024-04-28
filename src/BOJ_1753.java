import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1753 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());

        int[][] graph = new int[V][V];

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (graph[i][j] == 0) {
                    graph[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            if (w < graph[u - 1][v - 1]) {
                graph[u - 1][v - 1] = w;
            }
        }

        // 시작점에서 해당 정점까지 현재 연결된 간선을 기준으로 초기화
        int[] distance = new int[V];
        for (int i = 0; i < V; i++) {
            if (i != K - 1) {
                distance[i] = graph[K - 1][i];
            }
        }
        boolean[] visited = new boolean[V];
        visited[K - 1] = true;

        for (int i = 0; i < V - 1; i++) {
            int min = Integer.MAX_VALUE;
            int nowIndex = -1;
            for (int j = 0; j < V; j++) {
                if (!visited[j] && min > distance[j]) {
                    min = distance[j];
                    nowIndex = j;
                }
            }
            if (nowIndex == -1) {
                break;
            }
            visited[nowIndex] = true;

            for (int k = 0; k < V; k++) {
                if (!visited[k] && graph[nowIndex][k] != Integer.MAX_VALUE) {
                    if (distance[k] > graph[nowIndex][k] + distance[nowIndex]) {
                        distance[k] = graph[nowIndex][k] + distance[nowIndex];
                    }
                }
            }
        }

        for (int i = 0; i < V; i++) {
            if (distance[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(distance[i]);
            }
        }
    }

}

