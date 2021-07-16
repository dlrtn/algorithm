#include <iostream>
#include <math.h>

//2초이내로 대답해야한다는 조건이 있었으므로 수행시간을 줄이는 방법이 필요

bool isPrime(int N) { //일반적인 2~N까지 약수가 있는지 구하는 방법은 입력되는 N이 커질수록 실행시간에 손해를 보기때문에 math헤더파일의 sqrt함수 활용
	int sq; // N의 제곱근이 저장될 변수

	if (N == 1) //만약 N이 1일 경우 바로 소수가 아니다고 return
		return false;
	
	sq = (int)sqrt(N); //N의 제곱근 값을 sqrt에 저장

	for (int i = 2; i <= sq; i++) { //이 for문은 2부터 제곱근 n의 값까지 실행시키므로 기존 방법보다 훨씬 적은 수행시간 필요
		if (N % i == 0) //만약 약수가 있을 경우 바로 false return
			return false;
	}

	return true; //그외에는 약수가 없는 경우이므로 true return
}

void testcase(int caseIndex) {
	int n; //소수인지 판별할 정수
	scanf("%d", &n);// 정수를 입력받음

	bool result = isPrime(n); //isPrime이라는 함수에 n을 보내 소수인지 판별하는 return값을 저장

	printf("Case #%d\n", caseIndex); //몇번째 실행되는 함수인지를 표현하는 프린트문
	if (result) //isPrime 실행결과값이 true일 경우 = 소수인경우
	{
		printf("YES\n"); // YES 출력
	}
	else { //isPrime 실행결과값이 false인 경우 = 소수가 아닌경우
		printf("NO\n"); // NO 출력
	}
}

int main() {
	int caseSize; //수행할 케이스가 몇개인지를 저장하는 변수
	scanf("%d", &caseSize); //입력될 케이스 갯수를 입력받는 함수
	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) //testcase라는 함수를 caseSize번만큼 실행시켜주는 함수 
	{
		testcase(caseIndex); //caseIndex를 매개변수로 실행시키는 함수
	}
	return 0;
}
