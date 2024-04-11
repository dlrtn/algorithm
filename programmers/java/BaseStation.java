public class BaseStation {

    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int start = 1;
        int end = 1;

        for (int station : stations) {
            end = station - w - 1;

            if (start <= end) {
                int range = end - start + 1;
                answer += range / (2 * w + 1);
                if (range % (2 * w + 1) != 0) {
                    answer++;
                }
            }

            start = station + w + 1;
        }

        if (start <= n) {
            int range = n - start + 1;
            answer += range / (2 * w + 1);
            if (range % (2 * w + 1) != 0) {
                answer++;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        BaseStation baseStation = new BaseStation();
        int n = 11;
        int[] stations = {4, 11};
        int w = 1;

        /*
        13 [3, 7, 11] 1 4
        6 [3] 2 1
        11 [1, 5] 1 3
         */

        n = 13;
        stations = new int[]{3, 7, 11};
        w = 1;
        System.out.println(baseStation.solution(n, stations, w));

        n = 6;
        stations = new int[]{3};
        w = 2;
        System.out.println(baseStation.solution(n, stations, w));

        n = 11;
        stations = new int[]{1, 5};
        w = 1;
        System.out.println(baseStation.solution(n, stations, w));
    }

}
