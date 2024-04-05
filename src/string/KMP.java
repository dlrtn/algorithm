package string;

public class KMP {

    public static void main(String[] args) {
        String s = "abacabacabacaabacabaac";
        String p = "abacabaac";

        int[] pi = getPi(p);
        int result = kmp(s, p, pi);

        System.out.println(result);
    }

    public static int[] getPi(String p) {
        // pi[i] : p[0] ~ p[i]까지의 부분 문자열 중에서 접두사 == 접미사의 최대 길이
        int[] pi = new int[p.length() + 1];
        pi[0] = -1;
        // j : 접두사 == 접미사의 최대 길이
        int j = 0;

        // i : 접미사 포인터
        for (int i = 1; i < p.length(); i++) {
            // j가 0보다 크고 접두사와 접미사가 다르면 j를 pi[j]로 변경
            while (j > 0 && p.charAt(i) != p.charAt(j)) {
                j = pi[j];
            }

            // 접두사와 접미사가 같으면 j를 증가시키고 pi[i]에 j를 저장
            if (p.charAt(i) == p.charAt(j)) {
                pi[i + 1] = ++j;
            }
        }

        return pi;
    }

    public static int kmp(String s, String p, int[] pi) {
        int sLen = s.length();
        int pLen = p.length();
        int dist = 0;
        int idx = 0;
        int cnt = 0;

        while (true) {
            idx = 0;
            if ((idx + dist) + pLen > sLen) {
                break;
            }

            while (s.charAt(idx + dist) == p.charAt(cnt)) {
                idx++;
                cnt++;

                if (cnt == pLen) {
                    return dist;
                }
            }

            dist = dist + (cnt - pi[cnt]);
            cnt = 0;
        }

        return 0;
    }

}
