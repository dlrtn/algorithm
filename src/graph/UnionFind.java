package graph;

public class UnionFind {

    private int[] parent;
    private int[] rank;

    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    public int find(int x) {
        if (parent[x] == x) {
            return x;
        }

        return parent[x] = find(parent[x]);
    }

    public void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x == y) {
            return;
        }

        if (rank[x] < rank[y]) {
            parent[x] = y;
        } else {
            parent[y] = x;

            if (rank[x] == rank[y]) {
                rank[x]++;
            }
        }
    }

    public boolean isSameParent(int x, int y) {
        return find(x) == find(y);
    }

    public static void main(String[] args) {
        UnionFind uf = new UnionFind(5);

        uf.union(0, 1);
        uf.union(2, 3);
        uf.union(0, 4);

        System.out.println(uf.isSameParent(1, 4));
    }

}
