package programmers;

import java.util.ArrayDeque;
import java.util.Deque;

public class Pro_64062 {

    public static class Node {
        int value;
        int index;

        Node(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }

    public static int solution(int[] stones, int k) {
        Deque<Node> dq = new ArrayDeque<>();
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < stones.length; i++) {
            int stone = stones[i];

            while (!dq.isEmpty() && i - dq.peekFirst().index >= k) {
                dq.pollFirst();
            }

            while (!dq.isEmpty() && stone > dq.peekLast().value) {
                dq.pollLast();
            }

            dq.addLast(new Node(stone, i));

            if (i >= k - 1) {
                min = Math.min(min, dq.peekFirst().value);
            }
        }

        return min;
    }

    public static void main(String[] args) {
        int[] stones = {2, 4, 5, 3, 2, 1, 4, 2, 5, 1};
        int k = 3;

        System.out.println(solution(stones, k));
    }

}
