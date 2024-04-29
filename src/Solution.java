class Solution {

    public static long count;
    public static boolean[] visited;

    public static void backtracking(int depth, int n, long k) {
        if (depth == n) {
            count++;

            if (count == k) {
                for (int i = 0; i < n; i++) {
                    System.out.print(i + 1 + " ");
                }
                return;
            }
        }

        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }

            visited[i] = true;
            backtracking(depth + 1, n, k);
            visited[i] = false;
        }
    }

    public int[] solution(int n, long k) {
        int[] answer = {};

        count = 0;
        visited = new boolean[n];

        backtracking(0, n, k);
        return answer;
    }
}