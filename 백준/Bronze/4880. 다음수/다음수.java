import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int s1 = Integer.parseInt(st.nextToken());
        int s2 = Integer.parseInt(st.nextToken());
        int s3 = Integer.parseInt(st.nextToken());
        while (true) {
            if (s1 == 0 && s2 == 0 && s3 == 0) {
                break;
            }

            if ((s1 == 0 || s2 == 0 || s3 == 0) || isAP(s1, s2, s3)) {
                System.out.println("AP " + (s3 + (s3 - s2)));
            } else {
                System.out.println("GP " + (s3 * (s3 / s2)));
            }

            st = new StringTokenizer(br.readLine());
            s1 = Integer.parseInt(st.nextToken());
            s2 = Integer.parseInt(st.nextToken());
            s3 = Integer.parseInt(st.nextToken());
        }


    }

    public static boolean isAP(int s1, int s2, int s3) {
        if ((s3 - s2) == (s2 - s1) && s3 - s2 != 0) {
            return true;
        }
        return false;
    }
}
