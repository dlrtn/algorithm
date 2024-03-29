package graph;

import java.util.PriorityQueue;

public class Dijkstra {

    public static void main(String[] args) {
        int[][] graph = {
                {0, 2, 5, 1, 0, 0},
                {2, 0, 3, 2, 0, 0},
                {5, 3, 0, 3, 1, 5},
                {1, 2, 3, 0, 1, 0},
                {0, 0, 1, 1, 0, 2},
                {0, 0, 5, 0, 2, 0}
        };
        int start = 0;
        int[] distance = dijkstra(graph, start);
        for (int i = 0; i < distance.length; i++) {
            System.out.println(start + " -> " + i + ": " + distance[i]);
        }
    }

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
                    distance[j] = Math.min(distance[j], distance[minIndex] + graph[minIndex][j]);
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
