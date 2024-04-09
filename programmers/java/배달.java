public class 배달 {

    public static void main(String[] args) {
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

        System.out.println(solution(N, road, K)); // 4

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

        System.out.println(solution(N, road, K)); // 4
    }

    public static int solution(int N, int[][] road, int K) {
        int answer = 0;
        int[][] map = new int[N][N];
        int[] distance = new int[N];
        boolean[] visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            distance[i] = Integer.MAX_VALUE;
            for (int j = 0; j < N; j++) {
                if (i == j) {
                    map[i][j] = 0;
                } else {
                    map[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        for (int[] r : road) {
            int a = r[0] - 1;
            int b = r[1] - 1;
            int c = r[2];

            if (map[a][b] > c) {
                map[a][b] = c;
                map[b][a] = c;
            }
        }

        distance[0] = 0;

        for (int i = 0; i < N; i++) {
            int min = Integer.MAX_VALUE;
            int minIndex = -1;

            for (int j = 0; j < N; j++) {
                if (!visited[j] && distance[j] < min) {
                    min = distance[j];
                    minIndex = j;
                }
            }

            visited[minIndex] = true;

            for (int j = 0; j < N; j++) {
                if (!visited[j] && map[minIndex][j] != Integer.MAX_VALUE) {
                    if (distance[j] > distance[minIndex] + map[minIndex][j]) {
                        distance[j] = distance[minIndex] + map[minIndex][j];
                    }
                }
            }
        }

        for (int i : distance) {
            if (i <= K) {
                answer++;
            }
        }

        return answer;
    }

}
