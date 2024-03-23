import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class BOJ_1431 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int n = Integer.parseInt(br.readLine());

        String[] arr = new String[n];

        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine();
        }

        Arrays.stream(arr).sorted((a, b) -> {
            if (a.length() == b.length()) {
                if (sum(a) == sum(b)) {
                    return a.compareTo(b);
                }
                return Integer.compare(sum(a), sum(b));
            }
            return a.length() - b.length();
        }).forEach(System.out::println);
    }

    public static int sum(String string) {
        return Arrays.stream(string.split(""))
                .filter(s -> Character.isDigit(s.charAt(0)))
                .mapToInt(Integer::parseInt)
                .sum();

    }
}
