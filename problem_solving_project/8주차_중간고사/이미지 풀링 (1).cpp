#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int p[1025][1025]; //최댓값이 1024이므로
int n, ans; //nxn에서 size를 입력받을 변수와 정답을 저장할 변수

//두 번째로 큰 수를 반환하는 함수
int Pulling(int x, int y) //
{
    vector <int > a; //a는 2x2 벡터이다.
    for (int i = x; i < x + 2; i++)
        for (int j = y; j < y + 2; j++)
            a.push_back(p[i][j]);
    sort(a.begin(), a.end()); //a벡터를 정렬하여 3번째 인덱스를 반환함.
    return a[2];
}

int main() {
    time_t start, end;
    double result;
    cin >> n;
    for (int i = 0; i < n; i++)  {
        for (int j = 0; j < n; j++)
            cin >> p[i][j];        
    }
    start = time(NULL); //입력끝 실행시작
    while (n > 1) //n이 최종적으로 1이 될때까지
    {
        for (int i = 0; i < n; i += 2)
            for (int j = 0; j < n; j += 2)
                p[i / 2][j / 2] = Pulling(i, j); //가로 세로 2칸씩 움직이며 p갱신
        n /= 2; //n의 사이즈를 절반으로 줄임
    }
    end = time(NULL); // 실행종료
    cout << p[0][0] << '\n';//가장 마지막에 남아있는 n의 값을 출력함.
    result = (double)(end - start);
    printf("실행시간 : %f초", result / CLOCKS_PER_SEC);
}