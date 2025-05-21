import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_21394 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            int[] arr = new int[9];
            int length = 0;
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < 9; j++) {
                arr[j] = Integer.parseInt(st.nextToken());
                length += arr[j];
            }

            PriorityQueue<Integer> queue = new PriorityQueue<>(
                    (o1, o2) -> o2 - o1
            );

            for (int j = 8; j >= 0; j--) {
                while (arr[j] > 0) {
                    if (j == 5) {
                        queue.add(9);
                        arr[j]--;
                        continue;
                    }
                    queue.add(j + 1);
                    arr[j]--;
                }
            }

            int[] answer = new int[length];
            for (int j = 0; j < length; j++) {
                // 왼쪽
                // 오른쪽
                // 차례대로 채워나가면 됨

                if (j % 2 == 0) {
                    answer[j / 2] = queue.poll();
                } else {
                    answer[length - 1 - j / 2] = queue.poll();
                }
            }

            for (int j = 0; j < length; j++) {
                System.out.print(answer[j] + " ");
            }
            System.out.println();
        }
    }
}
