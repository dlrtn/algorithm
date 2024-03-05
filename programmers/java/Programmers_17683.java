import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;

public class Programmers_17683 {

    public static void main(String[] args) {
        System.out.println(Solution.solution("ABCDEFG",
                new String[]{"12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"}));
        System.out.println(Solution.solution("CC#BCC#BCC#BCC#B",
                new String[]{"03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"}));
        System.out.println(Solution.solution("ABC",
                new String[]{"12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"}));
        System.out.println(Solution.solution("ABC",
                new String[]{"12:00,12:14,HELLO,ABCABC", "13:00,13:15,WORLDD,ABC"}));
        System.out.println(Solution.solution("ABC",
                new String[]{"12:00,12:14,HELLO,ABCABC", "13:00,13:13,WORLDD,ABC"}));
        System.out.println(Solution.solution("A",
                new String[]{"12:00,12:01,Song,BA"}));
        // "BA", ["12:00,12:02,Song,AB"] -> "(None)"
        //"BA", ["12:00,12:03,Song,AB"] -> "Song"
        System.out.println(Solution.solution("BA",
                new String[]{"12:00,12:02,Song,AB"}));
        System.out.println(Solution.solution("BA",
                new String[]{"12:00,12:03,Song,AB"}));

        //"BA", ["12:00,12:04,Song,A#B"] -> "(None)"
        //
        //"A", ["12:00,12:01,Song,A#"] -> "(None)"
        //"A#", ["12:00,12:01,Song,A#"] -> "Song"

        System.out.println(Solution.solution("BA",
                new String[]{"12:00,12:04,Song,A#B"}));
        System.out.println(Solution.solution("A",
                new String[]{"12:00,12:01,Song,A#"}));
        System.out.println(Solution.solution("A#",
                new String[]{"12:00,12:01,Song,A#"}));

        // "ABA", ["12:00,13:00,Song,AB"] -> "Song"
        System.out.println(Solution.solution("ABA",
                new String[]{"12:00,13:00,Song,AB"}));

        // "A", ["12:00,12:01,Sing,A", "12:00,12:01,Song,A"] -> "Sing"
        //
        //"A", ["12:00,12:01,Sing,A", "12:00,12:02,Song,A"] -> "Song"
        //"A", ["12:00,12:01,Sing,A", "12:00,13:00,Song,A"] -> "Song"

        System.out.println(Solution.solution("A",
                new String[]{"12:00,12:01,Sing,A", "12:00,12:01,Song,A"}));
        System.out.println(Solution.solution("A",
                new String[]{"12:00,12:01,Sing,A", "12:00,12:02,Song,A"}));
        System.out.println(Solution.solution("A",
                new String[]{"12:00,12:01,Sing,A", "12:00,13:00,Song,A"}));
    }

}

class Solution {

    public static String solution(String m, String[] musicinfos) {
        Queue<String> inputOrder = new ArrayDeque<>();
        Map<String, String> musicMap = new HashMap<>();
        Map<String, Integer> musicPlayTime = new HashMap<>();
        Arrays.stream(musicinfos).forEach((musicinfo) -> {
            String[] data = musicinfo.split(",");
            int startedAt = Integer.parseInt(data[0].split(":")[0]) * 60 + Integer.parseInt(
                    data[0].split(":")[1]);
            int endedAt = Integer.parseInt(data[1].split(":")[0]) * 60 + Integer.parseInt(
                    data[1].split(":")[1]);
            int playTime = endedAt - startedAt;

            String musicTitle = data[2];
            String musicSheetInfo = data[3].replaceAll("C#", "X").replaceAll("D#", "Y").replaceAll(
                    "F#", "Z").replaceAll("G#", "I").replaceAll("A#", "K").replaceAll("B#", "L");

            int musicSheetLength = musicSheetInfo.length();
            String music =
                    musicSheetInfo.repeat(playTime / musicSheetLength) + musicSheetInfo.substring(0,
                            playTime % musicSheetLength);
            musicMap.put(musicTitle, music);
            musicPlayTime.put(musicTitle, playTime);
            inputOrder.add(musicTitle);
        });
        String comparison = m.replaceAll("C#", "X").replaceAll("D#", "Y").replaceAll("F#", "Z")
                .replaceAll("G#", "I").replaceAll("A#", "K").replaceAll("B#", "L");

        String[] answer = musicMap.keySet().stream()
                .filter((musicTitle) -> musicMap.get(musicTitle).contains(comparison))
                .sorted((o1, o2) -> {
                    int o1PlayTime = musicPlayTime.get(o1);
                    int o2PlayTime = musicPlayTime.get(o2);
                    if (o1PlayTime == o2PlayTime) {
                        return inputOrder.stream().collect(
                                java.util.stream.Collectors.toList()).indexOf(o1) - inputOrder.stream()
                                .collect(java.util.stream.Collectors.toList()).indexOf(o2);
                    }
                    return o2PlayTime - o1PlayTime;
                }).collect(
                        java.util.stream.Collectors.toList()).toArray(new String[0]);

        if (answer.length == 0) {
            return "(None)";
        }
        return answer[0];
    }
}
