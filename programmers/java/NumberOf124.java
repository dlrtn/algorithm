public class NumberOf124 {

    public static void main(String[] args) {
        System.out.println(solution(1)); // 1
        System.out.println(solution(2)); // 2
        System.out.println(solution(3)); // 4
        System.out.println(solution(4)); // 11
    }

    public static String solution(int n) {
        StringBuilder sb = new StringBuilder();
        int[] arr = {4, 1, 2};

        while (n > 0) {
            sb.insert(0, arr[n % 3]);
            n = (n - 1) / 3;
        }

        return sb.toString();
    }

}
