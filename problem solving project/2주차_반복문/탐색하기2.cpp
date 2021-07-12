#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

void printIndexes(string school[], int n){
	int first = -1; //초기 설정값
	int last = -1;
	int cnt = 0; //AJOU라는 값을 처음만났을때와 아닐때를 구분하기 위한 변수
	for (int i = 0; i < n; i++){
		if(school[i] == "AJOU"){ //string값이 AJOU일때 동작
			if(cnt == 0) //AJOU라는 값을 처음 만났을 경우 first 변수 초기화
				first = i+1; //인덱스가 아니므로 +1
			else // AJOU라는 값을 처음 만나지 않았을 경우
				last = i+1; 
			cnt++; //AJOU라는 값을 만날때마다 플러스됨
		}
		
	}
	printf("%d %d", first, last);
}

int main(){
	int n;
	char buff[11];
	string *school;
	
	scanf("%d", &n);
	school = new string[n];
	
	for (int i =0; i < n; i++) {
		scanf("%s", buff);
		school[i] = buff;
	}
	
	printIndexes(school, n);
	
	delete[] school;
	return 0;
}
