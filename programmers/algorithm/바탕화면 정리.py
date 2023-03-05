def solution(wallpaper):
    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rdx = 0
    rdy = 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if lux > i:
                    lux = i
                if luy > j:
                    luy = j
                if rdx < i + 1:
                    rdx = i + 1
                if rdy < j + 1:
                    rdy = j + 1
                print(i + 1, j + 1)

    return [lux, luy, rdx, rdy]
