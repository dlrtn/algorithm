package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class FloydWarshall {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[][] graph = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        floydWarshall(graph, n);
    }

    // annotation please
    public static int[][] floydWarshall(int[][] graph, int n) {
        // dist[i][j] = i에서 j로 가는 최단 거리
        int[][] dist = new int[n][n];

        // dist 배열 초기화
        for (int i = 0; i < n; i++) {
            System.arraycopy(graph[i], 0, dist[i], 0, n);
        }

        // k = 거쳐가는 노드
        for (int k = 0; k < n; k++) {
            // i = 출발 노드
            for (int i = 0; i < n; i++) {
                // j = 도착 노드
                for (int j = 0; j < n; j++) {
                    // i에서 j로 가는 최단 거리보다 i에서 k를 거쳐 j로 가는 거리가 더 짧을 경우
                    if (dist[i][k] != 0 && dist[k][j] != 0) {
                        // i에서 j로 가는 최단 거리를 i에서 k를 거쳐 j로 가는 거리로 갱신
                        if (dist[i][j] == 0) {
                            // i에서 j로 가는 경로가 없는 경우
                            dist[i][j] = dist[i][k] + dist[k][j];
                        } else {
                            // i에서 j로 가는 경로가 있는 경우
                            dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                        }
                    }
                }
            }
        }

        return dist;
    }

}
