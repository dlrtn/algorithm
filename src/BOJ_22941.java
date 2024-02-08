import static java.lang.System.exit;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_22941 {

    static class Hero {

        private long hp;
        private long atk;

        public Hero(long hp, long atk) {
            this.hp = hp;
            this.atk = atk;
        }

        public void attack(Devil devil) {
            devil.beAttacked(atk);
        }

        public void beAttacked(long damage) {
            hp -= damage;

            isDefeated();
        }

        private void isDefeated() {
            if (hp <= 0) {
                System.out.println("gg");
                exit(0);
            }
        }
    }

    static class Devil {

        private long hp;
        private long atk;
        private HealSkill healSkill;

        public Devil(long
                hp, long atk, long point, long amount) {
            this.hp = hp;
            this.atk = atk;
            healSkill = new HealSkill(point, amount);
        }

        public void attack(Hero hero) {
            hero.beAttacked(atk);
        }

        public void beAttacked(long damage) {
            hp -= damage;

            isDefeated();
        }

        public void useHealSkill() {
            if (healSkill.isUsed && (hp >= 1 && hp <= healSkill.getPoint())) {
                hp += healSkill.getAmount();
                healSkill.updateUseState();
            }
        }

        private void isDefeated() {
            if (hp <= 0) {
                System.out.println("Victory!");
                exit(0);
            }
        }
    }

    static class HealSkill {

        private long point;
        private long amount;
        private boolean isUsed;

        public HealSkill(long point, long amount) {
            this.point = point;
            this.amount = amount;
            this.isUsed = true;
        }

        public long getAmount() {
            return amount;
        }

        public long getPoint() {
            return point;
        }

        public void updateUseState() {
            this.isUsed = !isUsed;
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Hero hero = new Hero(Long.parseLong(st.nextToken()), Long.parseLong(st.nextToken()));
        long devilsHp = Long.parseLong(st.nextToken());
        long devilsAttack = Long.parseLong(st.nextToken());

        st = new StringTokenizer(br.readLine());

        long healPoint = Long.parseLong(st.nextToken());
        long healAmount = Long.parseLong(st.nextToken());
        Devil devil = new Devil(devilsHp, devilsAttack, healPoint, healAmount);

        while (true) {
            hero.attack(devil);
            devil.attack(hero);
            devil.useHealSkill();
        }
    }
}
