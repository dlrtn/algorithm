import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1929 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        boolean[] array = eratosthenes(n);

        for (int i = m; i < n + 1; i++) {
            if (array[i]) {
                System.out.println(i);
            }
        }
    }

    public static boolean isPrimeNumber(int n) {
        if (n == 1) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }


    public static boolean[] eratosthenes(int end) {
        boolean[] array = new boolean[end + 1];
        for (int i = 2; i < end + 1; i++) {
            array[i] = true;
        }

        for (int i = 2; i < end + 1; i++) {
            if (array[i] && isPrimeNumber(i)) {
                // 걸러주는 로직
                for (int j = i + i; j <= end; j += i) {
                    array[j] = false;
                }
            }
        }

        return array;
    }
}
