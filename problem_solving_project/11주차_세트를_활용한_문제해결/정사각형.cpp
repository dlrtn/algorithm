#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <set>
#include <algorithm>

using namespace std;


class Point2D {
public:
	int x;
	int y;
	int index;

	Point2D(int index, int x, int y) {
		this->index = index;
		this->x = x;
		this->y = y;
	}

	Point2D(int x, int y) {
		this->index = 1;
		this->x = x;
		this->y = y;
	}

	long long getSquaredDistanceTo(Point2D target) {
		// �� ��ǥ���� �����Ÿ��� ���
		long long dx = abs(this->x - target.x);
		long long dy = abs(this->y - target.y);
		return dx * dx + dy * dy;
	}

	double getDistanceTo(Point2D target) {
		// �� ��ǥ���� �Ǽ� �Ÿ��� ���
		long long sqd = this->getSquaredDistanceTo(target);
		return sqrt(sqd);
	}

	bool operator < (const Point2D& other) const {
		// �� ��ǥ�� �켱������ ���ϱ� ���� �� ������

		// x��ǥ�� �ٸ��ٸ� x��ǥ�� �������� ��
		if (this->x != other.x) {
			return this->x < other.x;
		}

		// x��ǥ�� ���ٸ� y��ǥ�� �������� ��
		return this->y < other.y;
	}
};

long long getMaximumSquareArea(int n, const vector<Point2D>& points) {
	long long answer = 0;

	// ��� ���� Set�� �����Ѵ�
	set<Point2D> pSet;
	for (int i = 0; i < n; i += 1) {
		pSet.insert(points[i]);
	}

	for (int i = 0; i < n; i += 1) {
		Point2D pa = points[i];
		for (int j = 0; j < n; j += 1) {
			Point2D pb = points[j];
			// �� ������ pa�� pb�� ����
			// ���� pa-pb�� ���簢���� �� ���̶�� �� ��,

			long long area = pa.getSquaredDistanceTo(pb);//�� ���� �Ÿ�(������ ����)�� ������ ���簢���� ������


			
			if (area < answer) // �̹� ���� �簢������ ���̰� ���� �� �ۿ� ���ٸ� �ǳʶ�
				continue;

			// pa->pb������ x, y ��ǥ�� ���� �Ÿ��� ����
			int dx = pb.x - pa.x;
			int dy = pb.y - pa.y;

			// ���� <dx, dy>�� 90���� ȸ����Ű�� <-dy, dx>�� �ȴ�.
			// pa�� pb�� ���� <-dy, dx>�� ���� ���� ���簢���� �����ϴ� �� ��
			// pd, pc�� ����� �� ����
			Point2D pd(pa.x - dy, pa.y + dx);
			Point2D pc(pb.x - dy, pb.y + dx);


			// pd, pc�� �������̹Ƿ� �� ���� pSet�� �����ϴ� ������ �˻��ϸ� ��.
			if (pSet.find(pc) != pSet.end() && pSet.find(pd) != pSet.end()) {
				answer = max(answer, area);
			}
		}
	}


	return answer;
}

void process(int caseIndex) {
	int n;
	cin >> n;

	vector<Point2D> points;

	for (int i = 0; i < n; i += 1) {
		int x, y;
		cin >> x >> y;
		points.push_back(Point2D(i, x, y));//�ε����� x,y��ǥ�� ������ �ʱ�ȭ��Ŵ
	}

	double answer = getMaximumSquareArea(n, points); //N���� ���� ������ �ִ� ���� ���� ��ȯ����

	cout << fixed << setprecision(2) << answer << endl; //�Ҽ��� ���ڸ����� ���
}

int main() {
	int caseSize;
	cin >> caseSize;

	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) { //caseSize��ŭ ����ϱ� ���� ����
		process(caseIndex);
	}
}