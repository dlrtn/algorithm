package search;

import java.util.Stack;

public class DepthFirstSearch {

    public static void main(String[] args) {
        int[][] graph = {
                {0, 1, 1, 0, 0, 0, 0, 0},
                {1, 0, 0, 1, 1, 0, 0, 0},
                {1, 0, 0, 0, 0, 1, 1, 0},
                {0, 1, 0, 0, 0, 0, 0, 1},
                {0, 1, 0, 0, 0, 0, 0, 1},
                {0, 0, 1, 0, 0, 0, 0, 1},
                {0, 0, 1, 0, 0, 0, 0, 1},
                {0, 0, 0, 1, 1, 1, 1, 0}
        };

        boolean[] visited = new boolean[graph.length];

        dfs(graph, visited, 0);
    }

    public static void dfs(int[][] graph, boolean[] visited, int start) {
        Stack stack = new Stack();

        while (true) {
            visited[start] = true;
            System.out.print(start + " ");

            for (int i = 0; i < graph.length; i++) {
                if (graph[start][i] == 1 && !visited[i]) {
                    stack.push(i);
                }
            }

            if (stack.isEmpty()) {
                break;
            }

            start = (int) stack.pop();
        }
    }

}
