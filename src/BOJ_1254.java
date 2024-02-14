import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1254 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();

        int i = 0;
        int j = s.length();

        while (i < j) {
            String nowString = s.substring(i, j);
            StringBuffer sb = new StringBuffer(nowString);
            if (nowString.equals(sb.reverse().toString())) {
                break;
            }
            i++;
        }
        System.out.println(i + s.length());
    }

}
