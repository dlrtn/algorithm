package graph;

import java.io.IOException;

public class DijkstraExample {

    public static void dijkstra(int N, int[][] road, int K) throws IOException {
        // 1. 현재 정점에서 최단 거리의 인덱스를 구한다.
        // 2. 현재 정점에서 최단 거리의 인덱스를 방문 처리한다.
        // 3. 현재 정점에서 최단 거리의 인덱스를 기준으로 갱신할 수 있는 정점들을 갱신한다.
        int[] distance = new int[N];
        int[][] graph = new int[N][N];
        boolean[] visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            distance[i] = Integer.MAX_VALUE;
            for (int j = 0; j < N; j++) {
                if (i == j) {
                    graph[i][j] = 0;
                } else {
                    graph[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        for (int[] r : road) {
            int a = r[0] - 1;
            int b = r[1] - 1;
            int c = r[2];

            if (graph[a][b] < c) {
                continue;
            }
            graph[a][b] = c;
            graph[b][a] = c;
        }

        for (int i = 0; i < N; i++) {
            distance[i] = graph[0][i];
        }

        for (int i = 0; i < N; i++) {
            int minIndex = -1;
            int minDistance = Integer.MAX_VALUE;
            for (int j = 0; j < N; j++) {
                if (!visited[j] && distance[j] < minDistance) {
                    minDistance = distance[j];
                    minIndex = j;
                }
            }
            visited[minIndex] = true;

            for (int j = 0; j < N; j++) {
                if (visited[j] || graph[minIndex][j] == Integer.MAX_VALUE) {
                    continue;
                }

                if (graph[minIndex][j] + distance[minIndex] < distance[j]) {
                    distance[j] = graph[minIndex][j] + distance[minIndex];
                }
            }
        }

        int count = 0;
        for (int i : distance) {
            if (i <= K) {
                count++;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        int N = 5;
        int[][] road = {
                {1, 2, 1},
                {2, 3, 3},
                {5, 2, 2},
                {1, 4, 2},
                {5, 3, 1},
                {5, 4, 2}
        };
        int K = 3;

        dijkstra(N, road, K);

        N = 6;
        road = new int[][]{
                {1, 2, 1},
                {1, 3, 2},
                {2, 3, 2},
                {3, 4, 3},
                {3, 5, 2},
                {3, 5, 3},
                {5, 6, 1}
        };
        K = 4;

        dijkstra(N, road, K);
    }
}
