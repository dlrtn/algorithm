import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        OutputStream out = System.out;
        OutputStreamWriter writer = new OutputStreamWriter(out);

        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());

        int k = Integer.parseInt(st.nextToken());

        int size = n / k;

        for (int i = 0; i < n; i += size) {
            Arrays.stream(Arrays.copyOfRange(arr, i, i + size)).sorted().forEach((number) -> {
                try {
                    writer.write(number + " ");
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            });
        }

        writer.flush();
    }
}
