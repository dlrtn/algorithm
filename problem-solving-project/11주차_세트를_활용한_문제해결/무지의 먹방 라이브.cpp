#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b) {
	return a.second < b.second;
}

int solution(vector<int> food_times, long long k) {
	long long lastTime = 0; //�ٷ� ���� �˻��� ������ �ɸ��� �ð�
	long long time = 0;     //���� �� ���� ���� �ð��� �ɸ��� ���� * ���� ������ size�� ���� ����
	int size = food_times.size();
	vector<pair<int, int>> food_info;

	for (int i = 0; i < food_times.size(); i++) //�� ���� ������ ������ �ִ� food_times ���͸� �ʱ�ȭ
		food_info.push_back(make_pair(food_times[i], i + 1));
	sort(food_info.begin(), food_info.end());   //������������ ��������. 0��° �ε����� ���� ���� �ð��� �ɸ��� ������ ��������.

	for (vector<pair<int, int>>::iterator i = food_info.begin(); i != food_info.end(); i++) {
		time = (i->first - lastTime) * size; //���� i�� ���ĵǾ������Ƿ� i���� ���뿡 ���� ���� �ð��� 
											//�ɸ��� ������ �ε����� ����Ǿ�����.
											//t���� ���뿡 ���� ���� �ð��� �ɸ��� ������ �ð� * size�Ͽ� k���� ���־�
											//���� �ð��� ����ؾ���.
		if (time <= k) {
			k -= time; //���� �ð� ����
			lastTime = i->first; //��� ã�ư��� ������ ���� �ɸ�����
		}
		else {
			sort(i, food_info.end(), compare); //���� ��ȣ������ �ٽ� ����
			return (i + (k % size))->second; //�� �������� �����ؾ��� ������ �ε����� return��.
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

	scanf("%d", &n); //������ ���� ����

	for (int i = 0; i < n; i++) { //������ �ε������� �ɸ��� �ð��� �Է¹޾� ���͸� �ʱ�ȭ
		int x;
		scanf("%d", &x);
		food.push_back(x);
	}

	scanf("%d", &t);//�ߴܵǴ� �ð��� �Է¹޴� ����

	start = time(NULL); //�Է³� �������
	answer = solution(food, t);
	end = time(NULL); // ��������
	printf("%d\n", answer);
	result = (double)(end - start);
	printf("����ð� : %f��", result / CLOCKS_PER_SEC);
	return 0;
}