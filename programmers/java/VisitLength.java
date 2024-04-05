import java.util.ArrayList;
import java.util.List;

public class VisitLength {

    public static class Node {

        int x;
        int y;

        List<MovementHistory> history;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
            this.history = new ArrayList<>();
        }

        public boolean isPossible(char direct) {
            switch (direct) {
                case 'U':
                    return y + 1 <= 5;
                case 'D':
                    return y - 1 >= -5;
                case 'R':
                    return x + 1 <= 5;
                case 'L':
                    return x - 1 >= -5;
                default:
                    return false;
            }
        }

        public boolean isContain(int x, int y, int x2, int y2) {
            for (MovementHistory movementHistory : history) {
                if (movementHistory.x == x && movementHistory.y == y && movementHistory.x2 == x2 && movementHistory.y2 == y2) {
                    return true;
                }
            }
            return false;
        }

        public void move(char direct) {
            switch (direct) {
                case 'U':
                    if (!isContain(x, y, x, y + 1) && !isContain(x, y + 1, x, y)) {
                        history.add(new MovementHistory(x, y, x, y + 1));
                        history.add(new MovementHistory(x, y + 1, x, y));
                    }
                    y += 1;
                    break;
                case 'D':
                    if (!isContain(x, y, x, y - 1) && !isContain(x, y - 1, x, y)) {
                        history.add(new MovementHistory(x, y, x, y - 1));
                        history.add(new MovementHistory(x, y - 1, x, y));
                    }
                    y -= 1;
                    break;
                case 'R':
                    if (!isContain(x, y, x + 1, y) && !isContain(x + 1, y, x, y)) {
                        history.add(new MovementHistory(x, y, x + 1, y));
                        history.add(new MovementHistory(x + 1, y, x, y));
                    }
                    x += 1;
                    break;
                case 'L':
                    if (!isContain(x, y, x - 1, y) && !isContain(x - 1, y, x, y)) {
                        history.add(new MovementHistory(x, y, x - 1, y));
                        history.add(new MovementHistory(x - 1, y, x, y));
                    }
                    x -= 1;
                    break;
                default:
                    break;
            }
        }
    }

    public static class MovementHistory {

        int x;
        int y;
        int x2;
        int y2;

        MovementHistory(int x, int y, int x2, int y2) {
            this.x = x;
            this.y = y;
            this.x2 = x2;
            this.y2 = y2;
        }

        @Override
        public boolean equals(Object obj) {
            MovementHistory movementHistory = (MovementHistory) obj;
            return this.x == movementHistory.x && this.y == movementHistory.y && this.x2 == movementHistory.x2 && this.y2 == movementHistory.y2;
        }
    }


    public static void main(String[] args) {
        System.out.println(solution("ULURRDLLU"));
        System.out.println(solution("LULLLLLLU"));
    }

    public static int solution(String dirs) {
        Node node = new Node(0, 0);

        for (int i = 0; i < dirs.length(); i++) {
            char direct = dirs.charAt(i);
            if (node.isPossible(direct)) {
                node.move(direct);
            }

        }

        return (int) node.history.stream().distinct().count() / 2;
    }

}
