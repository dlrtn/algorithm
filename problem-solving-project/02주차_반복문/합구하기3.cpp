#include <cstdio>
#include <iostream>

using namespace std;

long long getAnswer(int n){
	int *data; //각 인덱스+1까지의 값을 저장해놓을 배열
	long long sum = 0; //return 해줄 값을 저장해놓는 변수
	data = new int[n]; //메모리 할당
	data[0] = 1; //초기값을 지정해줌
	for (int i = 1; i < n; i++){ //인덱스 0을 제외하고 n-1까지 동작 수행
		data[i] += (data[i-1] + i+1);
	}
	for (int i =0; i < n; i++){//배열의 0~99 인덱스 값을 더해줌
		sum += data[i];
		
	}
	return sum; //최종값 리턴
}

int main(){
	int n;	
	
	scanf("%d", &n);
			
	long long answer = getAnswer(n);
	
	printf("%lld\n", answer);
	return 0;
}