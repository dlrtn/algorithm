import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_5904 {

    static String[] s = new String[28];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        getMoo(27);
        System.out.println(s[27].charAt(n));
    }


    public static String getMoo(int n) {
        if (n == 0) {
            return "moo";
        } else if (s[n] == null) {
            return s[n] = getMoo(n - 1) + "m" + "o".repeat(n + 2) + getMoo(n - 1);
        } else {
            return s[n];
        }
    }
}
