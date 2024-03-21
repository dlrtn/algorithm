import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1991 {

    public static class Node {

        private char data;
        private Node left;
        private Node right;

        public Node(char data) {
            this.data = data;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        Node root = new Node('A');

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            char data = st.nextToken().charAt(0);
            char left = st.nextToken().charAt(0);
            char right = st.nextToken().charAt(0);

            Node node = searchNode(root, data);
            if (left != '.') {
                node.left = new Node(left);
            }
            if (right != '.') {
                node.right = new Node(right);
            }
        }

        preOrder(root);
        System.out.println();
        inOrder(root);
        System.out.println();
        postOrder(root);

    }

    public static Node searchNode(Node node, char data) {
        if (node.data == data) {
            return node;
        }

        if (node.left != null) {
            Node left = searchNode(node.left, data);
            if (left != null) {
                return left;
            }
        }

        if (node.right != null) {
            Node right = searchNode(node.right, data);
            if (right != null) {
                return right;
            }
        }

        return null;
    }

    public static void preOrder(Node node) {
        if (node != null) {
            System.out.print(node.data);
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    public static void inOrder(Node node) {
        if (node != null) {
            inOrder(node.left);
            System.out.print(node.data);
            inOrder(node.right);
        }
    }

    public static void postOrder(Node node) {
        if (node != null) {
            postOrder(node.left);
            postOrder(node.right);
            System.out.print(node.data);
        }
    }
}
