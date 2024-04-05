package string;

public class RabinKarp {

    public static void main(String[] args) {
        String text = "ABABDABACDABABCABAB";
        String pattern = "ABABCABAB";
        System.out.println(rabinKarp(text, pattern));
    }

    public static int rabinKarp(String parent, String pattern) {
        int parentSize = parent.length();
        int patternSize = pattern.length();
        int parentHash = 0, patternHash = 0, power = 1;

        for (int i = 0; i <= parentSize - patternSize; i++) {
            if (i == 0) {
                for (int j = 0; j < patternSize; j++) {
                    parentHash += parent.charAt(patternSize - 1 - j) * power;
                    patternHash += pattern.charAt(patternSize - 1 - j) * power;
                    if (j < patternSize - 1) {
                        power *= 2;
                    }
                }
            } else {
                parentHash = 2 * (parentHash - parent.charAt(i - 1) * power) + parent.charAt(
                        patternSize - 1 + i);
            }

            if (parentHash == patternHash) {
                boolean finded = true;
                for (int j = 0; j < patternSize; j++) {
                    if (parent.charAt(i + j) != pattern.charAt(j)) {
                        finded = false;
                        break;
                    }
                }
                if (finded) {
                    return i + 1;
                }
            }
        }

        return -1;
    }

}
