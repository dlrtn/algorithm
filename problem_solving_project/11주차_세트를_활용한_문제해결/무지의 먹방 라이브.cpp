#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b) {
	return a.second < b.second;
}

int solution(vector<int> food_times, long long k) {
	long long lastTime = 0; //바로 직전 검사한 음식의 걸리는 시간
	long long time = 0;     //섭취 시 가장 적게 시간이 걸리는 음식 * 남은 음식의 size를 곱한 변수
	int size = food_times.size();
	vector<pair<int, int>> food_info;

	for (int i = 0; i < food_times.size(); i++) //두 개의 변수를 가지고 있는 food_times 벡터를 초기화
		food_info.push_back(make_pair(food_times[i], i + 1));
	sort(food_info.begin(), food_info.end());   //오름차순으로 정리해줌. 0번째 인덱스에 가장 적은 시간이 걸리는 음식이 오도록함.

	for (vector<pair<int, int>>::iterator i = food_info.begin(); i != food_info.end(); i++) {
		time = (i->first - lastTime) * size; //현재 i는 정렬되어있으므로 i에는 섭취에 가장 적은 시간이 
											//걸리는 음식의 인덱스가 저장되어있음.
											//t에는 섭취에 가장 적은 시간이 걸리는 음식의 시간 * size하여 k에서 빼주어
											//남은 시간을 계산해야함.
		if (time <= k) {
			k -= time; //남은 시간 감소
			lastTime = i->first; //방금 찾아갔던 음식이 몇초 걸리는지
		}
		else {
			sort(i, food_info.end(), compare); //음식 번호순으로 다시 정렬
			return (i + (k % size))->second; //그 다음으로 섭취해야할 음식의 인덱스를 return함.
		}
		size--;
	}
	return -1;
}

int main() {
	int n, t, answer;
	time_t start, end;
	double result;
	vector<int> food;

	scanf("%d", &n); //음식의 개수 변수

	for (int i = 0; i < n; i++) { //음식의 인덱스마다 걸리는 시간을 입력받아 벡터를 초기화
		int x;
		scanf("%d", &x);
		food.push_back(x);
	}

	scanf("%d", &t);//중단되는 시간으 입력받는 변수

	start = time(NULL); //입력끝 실행시작
	answer = solution(food, t);
	end = time(NULL); // 실행종료
	printf("%d\n", answer);
	result = (double)(end - start);
	printf("실행시간 : %f초", result / CLOCKS_PER_SEC);
	return 0;
}