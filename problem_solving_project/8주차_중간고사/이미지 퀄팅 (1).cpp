#include <algorithm>
#include <iostream>
#include <cmath>
#include <time.h>

using namespace std;

#define MIN(x,y) (x)<(y)?(x):(y)
#define GET_MIN(x,y,z) (MIN(x, y))<(z)?(MIN(x, y)):(z)

int main() {
	int y, x;
	cin >> y >> x;
	int min = 2147483647;
	time_t start, end;
	double result;
	int** a = new int* [y]; //이미지 B1 (왼쪽)
	int** b = new int* [y]; //이미지 B2 (오른쪽)
	int** c = new int* [y]; //DP를 사용해 풀기 위한 배열 사이즈는 x, y로 B1, B2와 동일

	for (int i = 0; i < y; i++) //이미지 B1의 밝기를 a라는 2차원 배열에 저장하기위해 동적할당
		a[i] = new int[x];
	for (int i = 0; i < y; i++) //이미지 B2의 밝기를 b라는 2차원 배열에 저장하기위해 동적할당
		b[i] = new int[x];
	for (int i = 0; i < y; i++) //이미지 (B1-B2)^2의 값을 c라는 2차원 배열에 저장하기위해 동적할당
		c[i] = new int[x];

	for (int i = 0; i < y; i++) { //B1 이미지의 밝기를 받아 초기화
		for (int j = 0; j < x; j++)
			cin >> a[i][j];
	}
	for (int i = 0; i < y; i++) { //B2 이미지의 밝기를 받아 초기화
		for (int j = 0; j < x; j++)
			cin >> b[i][j];
	}
	start = time(NULL);
	//DP를 사용하여 풀기로 하였음.
	for (int i = 0; i < y; i++) {
		for (int j = 0; j < x; j++)
			c[i][j] = (a[i][j] - b[i][j]) * (a[i][j] - b[i][j]); // a와 b의 각 요소에서 차를 제곱하여 c배열에 저장		
	}

	for (int i = 1; i < y; i++) { //문제 풀이는 두번째 줄부터 시작하므로 시작 인덱스를 1로 지정
		for (int j = 0; j < x; j++) { //0부터 끝까지 동작을 수행
			if (j == 0) //만약 픽셀의 위치가 가장 왼쪽일 경우, -1칸 차이나는 픽셀은 사용하지 못함
				c[i][j] += MIN(c[i - 1][j + 1], c[i - 1][j]);
			else if ((j + 1) == x) //만약 픽셀의 위치가 가장 오른쪽일 경우 +1칸 차이나는 픽셀은 사용하지 못함
				c[i][j] += MIN(c[i - 1][j - 1], c[i - 1][j]);
			else  //나머지 경우에는 -1,0,+1 모두 사용가능함
				c[i][j] += GET_MIN(c[i - 1][j + 1], c[i - 1][j - 1], c[i - 1][j]);
		}
	}

	for (int i = 0; i < x; i++) { //가장 마지막줄에서 최솟값을 출력하고 동작을 종료함
		if (min > c[y - 1][i])
			min = c[y - 1][i];
	}
	end = time(NULL);
	printf("%d\n", min);
	result = (double)(end - start);
	printf("실행시간 : %f초", result / CLOCKS_PER_SEC);
}