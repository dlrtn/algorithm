import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ_1991_Array {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        char[] arr = new char[(int) Math.pow(2, 27)];
        Map<Character, Integer> map = new HashMap<>();

        arr[1] = 'A';
        map.put('A', 1);

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            char data = st.nextToken().charAt(0);
            char left = st.nextToken().charAt(0);
            char right = st.nextToken().charAt(0);

            Integer parentNodeIndex = map.get(data);

            if (left != '.') {
                int leftIndex = parentNodeIndex * 2;
                arr[leftIndex] = left;
                map.put(left, leftIndex);
            }

            if (right != '.') {
                int rightIndex = parentNodeIndex * 2 + 1;
                arr[rightIndex] = right;
                map.put(right, rightIndex);
            }
        }

        preOrder(arr, 1);
        System.out.println();
        inOrder(arr, 1);
        System.out.println();
        postOrder(arr, 1);
    }

    public static void preOrder(char[] arr, int index) {
        if (arr[index] == 0) {
            return;
        }
        System.out.print(arr[index]);
        preOrder(arr, index * 2);
        preOrder(arr, index * 2 + 1);
    }

    public static void inOrder(char[] arr, int index) {
        if (arr[index] == 0) {
            return;
        }
        inOrder(arr, index * 2);
        System.out.print(arr[index]);
        inOrder(arr, index * 2 + 1);
    }

    public static void postOrder(char[] arr, int index) {
        if (arr[index] == 0) {
            return;
        }
        postOrder(arr, index * 2);
        postOrder(arr, index * 2 + 1);
        System.out.print(arr[index]);
    }

}
