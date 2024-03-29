import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_1238 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        int[][] graph = new int[n][n];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken());

            graph[a][b] = c;
        }

        int[][] distances = new int[n][n];

        for (int i = 0; i < n; i++) {
            distances[i] = dijkstra(graph, i);
        }

        int max = 0;

        for (int i = 0; i < n; i++) {
            max = Math.max(max, distances[i][x] + distances[x][i]);
        }

        System.out.println(max);
    }

    public static int[] dijkstra(int[][] graph, int startNode) {
        int n = graph.length;
        int[] distance = new int[n];
        boolean[] visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            distance[i] = Integer.MAX_VALUE;
        }

        distance[startNode] = 0;

        for (int i = 0; i < n - 1; i++) {
            int current = getMinIndex(distance, visited);
            visited[current] = true;

            for (int j = 0; j < n; j++) {
                if (!visited[j] && graph[current][j] != 0 && distance[current] != Integer.MAX_VALUE
                        && distance[current] + graph[current][j] < distance[j]) {
                    distance[j] = distance[current] + graph[current][j];
                }
            }
        }

        return distance;

    }

    public static int getMinIndex(int[] distance, boolean[] visited) {
        PriorityQueue<Node> pq = new PriorityQueue<>();

        for (int i = 0; i < distance.length; i++) {
            if (!visited[i]) {
                pq.add(new Node(i, distance[i]));
            }
        }

        return pq.poll().index;
    }

    public static class Node implements Comparable<Node> {

        int index;
        int distance;

        public Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node o) {
            return this.distance - o.distance;
        }

    }


}
