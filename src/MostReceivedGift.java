import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class MostReceivedGift {

    public int solution(String[] friends, String[] gifts) {
        int answer = 0;

        Map<String, Integer> friendIndex = new HashMap<>();
        int[] giverMap = new int[friends.length];
        int[] takerMap = new int[friends.length];
        int[] giftIndicators = new int[friends.length];
        int[] nextMonthGiftCount = new int[friends.length];

        for (int i = 0; i < friends.length; i++) {
            friendIndex.put(friends[i], i);
        }

        int[][] giftMap = new int[friends.length][friends.length];

        for (int i = 0; i < gifts.length; i++) {
            String[] gift = gifts[i].split(" ");
            giftMap[friendIndex.get(gift[0])][friendIndex.get(gift[1])]++;
            giverMap[friendIndex.get(gift[0])]++;
            takerMap[friendIndex.get(gift[1])]++;
        }

        for (int i = 0; i < friends.length; i++) {
            giftIndicators[i] = giverMap[i] - takerMap[i];
        }

        for (int i = 0; i < friends.length; i++) {
            for (int j = i + 1; j < friends.length; j++) {
                if (i == j) {
                    continue;
                }

                if (giftMap[i][j] > 0 || giftMap[j][i] > 0) {
                    if (giftMap[i][j] > giftMap[j][i]) {
                        nextMonthGiftCount[friendIndex.get(friends[i])]++;
                    } else if (giftMap[i][j] < giftMap[j][i]) {
                        nextMonthGiftCount[friendIndex.get(friends[j])]++;
                    } else {
                        if (giftIndicators[friendIndex.get(friends[i])] > giftIndicators[friendIndex.get(friends[j])]) {
                            nextMonthGiftCount[friendIndex.get(friends[i])]++;
                        } else if (giftIndicators[friendIndex.get(friends[i])] < giftIndicators[friendIndex.get(friends[j])]) {
                            nextMonthGiftCount[friendIndex.get(friends[j])]++;
                        }
                    }
                } else {
                    if (giftIndicators[friendIndex.get(friends[i])] > giftIndicators[friendIndex.get(friends[j])]) {
                        nextMonthGiftCount[friendIndex.get(friends[i])]++;
                    } else if (giftIndicators[friendIndex.get(friends[i])] < giftIndicators[friendIndex.get(friends[j])]) {
                        nextMonthGiftCount[friendIndex.get(friends[j])]++;
                    }
                }
            }
        }

        return Arrays.stream(nextMonthGiftCount).max().getAsInt();
    }

    public static void main(String[] args) {
        MostReceivedGift test = new MostReceivedGift();
        String[] friends = {"muzi", "ryan", "frodo", "neo"};
        String[] gifts = {"muzi frodo", "muzi frodo", "ryan muzi","ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"};

        System.out.println(test.solution(friends, gifts));
    }

}
