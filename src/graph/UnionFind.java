package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class UnionFind {

    private static int[] unionFind;

    public static void union(int i, int j) {
        int parentI = find(i);
        int parentJ = find(j);

        if (parentI != parentJ) {
            if (parentI < parentJ) {
                unionFind[parentJ] = parentI;
            } else {
                unionFind[parentI] = parentJ;
            }
        }
    }

    public static int find(int i) {
        if (unionFind[i] == i) {
            return i;
        }
        return unionFind[i] = find(unionFind[i]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        unionFind = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            unionFind[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (command == 0) {
                union(a, b);
            } else {
                if (unionFind[a] != unionFind[b]) {
                    System.out.println("NO");
                } else {
                    System.out.println("YES");
                }
            }
        }
    }

}
