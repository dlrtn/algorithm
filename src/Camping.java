import java.util.Scanner;

public class Camping {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int caseNumber = 1;
        while (true) {
            int L = sc.nextInt();
            int P = sc.nextInt();
            int V = sc.nextInt();

            if (L == 0 && P == 0 && V == 0) {
                break;
            }

            int usedDayCount = (V / P) * L;
            usedDayCount += (V % P) > L ? L : (V % P);

            System.out.println("Case " + caseNumber + ": " + usedDayCount);
            caseNumber++;
        }
    }
}
