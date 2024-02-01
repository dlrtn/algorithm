import java.util.ArrayList;
import java.util.Scanner;

public class BOJ_10814 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        ArrayList<Human> humans = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int age = sc.nextInt();
            String name = sc.next();

            humans.add(new Human(name, age));
        }

        humans.stream().sorted((o1, o2) -> {
            if (o1.age > o2.age) {
                return 1;
            } else if (o1.age < o2.age) {
                return -1;
            } else {
                return 0;
            }

        }).forEach(human -> System.out.println(human.age + " " + human.name));

    }

    public static class Human {

        private String name;
        private int age;

        public Human(String name, int age) {
            this.name = name;
            this.age = age;
        }
    }

}
