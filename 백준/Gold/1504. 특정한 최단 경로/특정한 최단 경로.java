import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        int[][] graph = new int[n][n];

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken());

            graph[a][b] = c;
            graph[b][a] = c;
        }

        st = new StringTokenizer(br.readLine());
        int v1 = Integer.parseInt(st.nextToken()) - 1;
        int v2 = Integer.parseInt(st.nextToken()) - 1;

        int[] distance = Dijkstra.dijkstra(graph, 0);
        int[] distance1 = Dijkstra.dijkstra(graph, v1);
        int[] distance2 = Dijkstra.dijkstra(graph, v2);

        // 2개의 루트가 존재한다. 경우의 수상 무조건! 왜냐 처음과 끝은 1과 N으로 고정되어있는데
        // 거쳐가야하는 노드 2개는 고정되어 있지 않기 때문에!
        // 1 -> v1 -> v2 -> N
        // 1 -> v2 -> v1 -> N
        // 근데 만약? 총 6개의 경로 중, 하나라도 INF 값인 경우엔..! -1 출력

        int result = Math.min(distance[v1] + distance1[v2] + distance2[n - 1],
                distance[v2] + distance2[v1] + distance1[n - 1]);

        if (distance[v1] == Integer.MAX_VALUE || distance1[v2] == Integer.MAX_VALUE
                || distance2[n - 1] == Integer.MAX_VALUE || distance[v2] == Integer.MAX_VALUE
                || distance2[v1] == Integer.MAX_VALUE || distance1[n - 1] == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(result);
        }
    }


    public static class Dijkstra {

        public static int[] dijkstra(int[][] graph, int start) {
            int n = graph.length;
            int[] distance = new int[n];
            boolean[] visited = new boolean[n];

            for (int i = 0; i < n; i++) {
                distance[i] = Integer.MAX_VALUE;
            }
            distance[start] = 0;

            for (int i = 0; i < n - 1; i++) {
                int minIndex = getMinIndex(distance, visited);
                visited[minIndex] = true;

                for (int j = 0; j < n; j++) {
                    if (!visited[j] && graph[minIndex][j] != 0
                            && distance[minIndex] != Integer.MAX_VALUE) {
                        distance[j] = Math.min(distance[j],
                                distance[minIndex] + graph[minIndex][j]);
                    }
                }
            }

            return distance;
        }

        // using priority queue
        public static int getMinIndex(int[] distance, boolean[] visited) {
            PriorityQueue<Node> pq = new PriorityQueue<>();

            for (int i = 0; i < distance.length; i++) {
                if (!visited[i]) {
                    pq.add(new Node(i, distance[i]));
                }
            }

            return pq.poll().index;
        }


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
