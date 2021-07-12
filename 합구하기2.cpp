#include <iostream>
#include <stdio.h>

using namespace std;

void solve(int data[], int n, int p, int q) {
	int sum = 0, cnt = 0; // sum이라는 값에 탑승가능한 사람의 몸무게의 총합을
					 	  // cnt라는 변수에는 탑승가능한 인원을 저장할 예정

	for (int i = 0; i < n; i++) { //n명 모두에 대한 검사를 위한 반복문
		if (p > data[i] || p == data[i]) { //탑승제한 중량과 같거나 적은 사람을 걸러냄
			sum += data[i];
			cnt++;
		}
	}

	printf("%d %d\n", cnt, sum);
	if (q > sum || q == sum) //최대중량보다 적으면 YES 많으면 NO
		printf("YES");
	else
		printf("NO");
}
int main() {
	int n, p, q;
	int* data;

	scanf("%d %d %d", &n, &p, &q);
	data = new int[n];
	for (int i = 0; i < n; i++) {
		scanf("%d", &data[i]);
	}

	solve(data, n, p, q);

	delete[] data;
	return 0;
}