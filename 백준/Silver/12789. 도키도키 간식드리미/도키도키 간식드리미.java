import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int nowNumber = 1;

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            if (arr[i] != nowNumber) {
                stack.push(arr[i]);
            } else {
                nowNumber++;
            }

            while (!stack.empty() && stack.peek().equals(nowNumber)) {
                stack.pop();
                nowNumber++;
            }
        }

        if (stack.empty()) {
            System.out.println("Nice");
        } else {
            System.out.println("Sad");
        }
    }
}
