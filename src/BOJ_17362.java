import java.util.Scanner;

public class BOJ_17362 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        switch (n % 8) {
            case 1:
                System.out.println(1);
                break;
            case 2:
                System.out.println(2);
                break;
            case 3:
                System.out.println(3);
                break;
            case 4:
                System.out.println(4);
                break;
            case 5:
                System.out.println(5);
                break;
            case 6:
                System.out.println(4);
                break;
            case 7:
                System.out.println(3);
                break;
            case 0:
                System.out.println(2);
                break;
        }
    }

}
