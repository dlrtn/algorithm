import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Queue;
import java.util.Scanner;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.stream.Collectors;

public class BOJ_11866 {

    public static void main(String[] args) {
        List<Integer> removes = new ArrayList<>();
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        Queue queue = new LinkedBlockingQueue(n);

        for (int i = 1; i <= n; i++) {
            queue.add(i);
        }

        while (!queue.isEmpty()) {
            for (int i = 0; i < k - 1; i++) {
                queue.add(queue.remove());
            }
            removes.add((Integer) queue.remove());
        }

        String answer = removes.stream().map(Objects::toString).collect(Collectors.joining(", "));

        System.out.println("<" + answer + ">");
    }

}
