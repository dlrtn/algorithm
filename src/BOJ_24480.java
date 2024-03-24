import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ_24480 {

    private static int[] visited;
    private static int count = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        Map<Integer, ArrayList<Integer>> map = new HashMap<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (!map.containsKey(a)) {
                map.put(a, new ArrayList<>());
            }

            if (!map.containsKey(b)) {
                map.put(b, new ArrayList<>());
            }

            map.get(a).add(b);
            map.get(b).add(a);
        }

        visited = new int[n];

        if (m == 0 || map.get(r) == null) {
            visited[r - 1] = 1;
            Arrays.stream(visited).forEach(System.out::println);
            return;
        }
        map.forEach((k, v) -> {
            v.sort((a, b) -> b - a);
        });

        dfs(map, r);

        Arrays.stream(visited).forEach(System.out::println);
    }

    public static void dfs(Map<Integer, ArrayList<Integer>> map, int start) {
        visited[start - 1] = count++;

        for (int i = 0; i < map.get(start).size(); i++) {
            int next = map.get(start).get(i);

            if (visited[next - 1] == 0) {
                dfs(map, next);
            }
        }
    }
}
