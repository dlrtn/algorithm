def edit_dist(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        dp[i][0] = i
    for j in range(1, len(str2) + 1):
        dp[0][j] = j

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[-1][-1]


def solution(begin, target, words):
    distance_dict = dict()
    if target not in words:
        return 0

    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and edit_dist(words[i], words[j]) == 1:
                if words[i] not in distance_dict.keys():
                    distance_dict[words[i]] = set()

                distance_dict[words[i]].add(words[j])

    for i in range(len(words)):
        if edit_dist(begin, words[i]) == 1:
            if begin not in distance_dict.keys():
                distance_dict[begin] = set()

            distance_dict[begin].add(words[i])


    stack = [begin]
    count = 0
    visited = [0] * len(words)

    while stack:
        print(stack)
        word = stack.pop()
        if word == target:
            return count

        for i in range(len(words)):
            if visited[i] == 0 and word in distance_dict.keys() and words[i] in distance_dict[word]:
                visited[i] = 1
                stack.append(words[i])
        count += 1

    return count


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
