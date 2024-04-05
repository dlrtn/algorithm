import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        long k = Long.parseLong(st.nextToken());

        long[] arr = new long[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(arr);

        Map<Long, Long> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            long num = arr[i] % k;

            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1L);
            }
        }

        long count = 0;
        for (Entry<Long, Long> entry : map.entrySet()) {
            long value = entry.getValue();

            if (value >= 2) {
                count += calculateCombinations(value, 2);
            }
        }

        System.out.println(count);
    }

    // 조합의 개수를 계산하는 메서드
    public static long calculateCombinations(long n, int r) {
        return factorial(n) / (factorial(r) * factorial(n - r));
    }

    // 팩토리얼을 계산하는 메서드
    public static long factorial(long n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }
}
