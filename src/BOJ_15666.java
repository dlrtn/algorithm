import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_15666 {

    static Stack<Integer> queue = new Stack<>();
    static int m;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        arr = Arrays.stream(arr).sorted().toArray();

        backtracking(0, arr, 0);

    }

    public static void backtracking(int selectedNumber, int[] arr, int depth) {
        if (depth == m) {
            for (Integer integer : queue) {
                System.out.print(integer + " ");
            }
            System.out.println();
            return;
        }

        int prev = -1;
        for (int i = selectedNumber; i < arr.length; i++) {
            if (prev == arr[i]) continue;
            queue.add(arr[i]);
            backtracking(i, arr, depth + 1);
            prev = queue.pop();
        }
    }
}
