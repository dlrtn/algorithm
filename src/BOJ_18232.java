import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_18232 {

    public static boolean[] visited = new boolean[300001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        Map<Integer, ArrayList<Integer>> linkedMap = new HashMap<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            if (!linkedMap.containsKey(x)) {
                linkedMap.put(x, new ArrayList<>());
            }
            if (!linkedMap.containsKey(y)) {
                linkedMap.put(y, new ArrayList<>());
            }
            linkedMap.get(x).add(y);
            linkedMap.get(y).add(x);
        }

        System.out.println(bfs(linkedMap, s, e, n));
        Runtime.getRuntime().gc();
        long usedMemory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        System.out.print(usedMemory / 1024 / 1024 + " mbytes");
    }

    public static int bfs(Map<Integer, ArrayList<Integer>> linkedMap, int s, int e, int n) {
        Queue<Node> queue = new PriorityQueue<>();
        int count = 0;
        queue.add(new Node(s, 0));
        while (!queue.isEmpty()) {
            Node nowNode = queue.remove();

            if (nowNode.index == e) {
                return nowNode.count;
            }
            if (nowNode.index + 1 < n + 1 && !visited[nowNode.index + 1]) {
                queue.add(new Node(nowNode.index + 1, nowNode.count + 1));
            }
            if (nowNode.index - 1 > 0 && !visited[nowNode.index - 1]) {
                queue.add(new Node(nowNode.index - 1, nowNode.count + 1));
            }
            if (linkedMap.containsKey(nowNode.index)) {
                linkedMap.get(nowNode.index).forEach((node) -> {
                    if (node == e) {
                        return;
                    }
                    if (visited[node]) {
                        return;
                    }
                    queue.add(new Node(node, nowNode.count + 1));
                });
            }
        }
        return count;
    }

    public static class Node implements Comparable<Node> {

        public int index;
        public int count;

        public Node(int index, int count) {
            this.index = index;
            this.count = count;
        }

        @Override
        public int compareTo(Node o) {
            return this.count - o.count;
        }
    }

}
