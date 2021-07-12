#include<cstdio>
#include<iostream>

using namespace std;

bool isInside(long long x, long long y, long long R) {
	long long sqd = x * x + y * y; //거리의 제곱
	if (sqd < R * R)  //반지름의 제곱
	{   
		return true;//원점과의 거리가 반지름보다 작다면, 원 안에 있으므로 true
	}
	return false;//아니면 false
}

void testcase(int caseIndex) {
	long long R; //반지름임 왜 long long이라는 자료형을 사용했는지는 모르겠습니다.
	scanf("%lld", &R);

	long long sum = 0; //1사분면에 존재하는 총 픽셀의 수
	long long y = R; //위에서부터 내려오므로 R부터 시작
	for (long x = 0; x <= R; x++) { // x는 0부터 반지름까지 구해야함.
		long long height = 0; //초기 높이는 0
		for (; y >= 0; y--) {//위에 y는 이미 초기값을 설정해주었으므로 생략, 내려오므로
			if (isInside(x, y, R)) {// 위에서부터 내려오다가 최초로 원 안에 포함된 좌표 x, y
				height = (y + 1); //얘들의 높이는 y+1이 왜냐 한 변이 1이므로 됨
				break;
			}
		}

		sum += height; //너비는 1이므로
	}


	printf("#%d\n", caseIndex);
	printf("%lld\n", sum * 4); //모든 사분면의 픽셀 수
}

int main() {
	int caseSize; //case 갯수를 저장받는 변수
	scanf("%d", &caseSize); //입력
	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) //caseSize만큼 실행
	{
		testcase(caseIndex);//testcase를 index에 맞춰 실행
	}
	return 0;
}