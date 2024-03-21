package graph;

import java.util.Arrays;

public class Kruskal {

    public static void main(String[] args) {
        int[][] arr = {
                {1, 2, 3},
                {1, 3, 2},
                {3, 2, 1},
                {2, 5, 2},
                {3, 4, 4},
                {4, 5, 6}
        };

        arr = Arrays.stream(arr).sorted((a, b) -> a[2] - b[2]).toArray(int[][]::new);
        System.out.println(Arrays.deepToString(arr));
        int[] parent = new int[6];
        for (int i = 1; i < parent.length; i++) {
            parent[i] = i;
        }

        int answer = 0;
        for (int i = 0; i < arr.length; i++) {
            int a = find(parent, arr[i][0]);
            int b = find(parent, arr[i][1]);

            if (a != b) {
                union(parent, a, b);
                answer += arr[i][2];
            }
        }

        System.out.println(answer);
    }

    public static int find(int[] parent, int i) {
        if (parent[i] == i) {
            return i;
        }
        return parent[i] = find(parent, parent[i]);
    }

    public static void union(int[] parent, int i, int j) {
        int parentI = find(parent, i);
        int parentJ = find(parent, j);

        if (parentI != parentJ) {
            if (parentI < parentJ) {
                parent[parentJ] = parentI;
            } else {
                parent[parentI] = parentJ;
            }
        }
    }

}
