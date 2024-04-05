import java.util.Arrays;

public class 등굣길 {

    public static void main(String[] args) {
        int m = 4;
        int n = 3;
        int[][] puddles = {{2, 2}};
        System.out.println(solution(m, n, puddles));
    }

    public static int solution(int m, int n, int[][] puddles) {
        int[][] arr = new int[m][n];

        for (int i = 0; i < puddles.length; i++) {
            arr[puddles[i][0] - 1][puddles[i][1] - 1] = -1;
        }
        arr[0][0] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] == -1) {
                    arr[i][j] = -1;
                    continue;
                }

                if (i > 0 && arr[i - 1][j] != -1) {
                    arr[i][j] += arr[i - 1][j] % 1000000007;
                }
                if (j > 0 && arr[i][j - 1] != -1) {
                    arr[i][j] += arr[i][j - 1] % 1000000007;
                }
            }
        }

        return arr[m - 1][n - 1] % 1000000007;
    }

}
