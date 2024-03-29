package graph;

import java.util.ArrayDeque;
import java.util.Queue;

public class TopologicalSorting {

    public static void main(String[] args) {
        int n = 7;
        int[][] graph = {
                {0, 1, 0, 1, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 1, 0},
                {0, 0, 0, 0, 0, 0, 1},
                {0, 0, 0, 0, 0, 0, 0}
        };

        System.out.println(topologicalSorting(graph, n));
    }

    public static Queue topologicalSorting(int[][] graph, int n) {
        Queue queue = new ArrayDeque();

        // 진입 차수를 저장할 배열
        int[] indegree = new int[n];

        // 각 노드의 진입 차수 계산
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                indegree[j] += graph[i][j];
            }
        }

        // 진입 차수가 0인 노드를 큐에 삽입
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        while (!queue.isEmpty()) {
            int node = (int) queue.poll();
            System.out.print(node + " ");

            for (int i = 0; i < n; i++) {
                if (graph[node][i] != 0) {
                    indegree[i]--;
                    if (indegree[i] == 0) {
                        queue.offer(i);
                    }
                }
            }
        }

        return queue;
    }


}
