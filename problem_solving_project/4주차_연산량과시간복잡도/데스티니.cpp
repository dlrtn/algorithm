#include <cstdio>
#include <cmath>
#include <climits>
#include <iostream>

using namespace std;

class Point2D { //2차원의 점을 표현하기 위한 class
private: //변수들의 접근성을 제한함
	int x;
	int y;
public: 
	Point2D(int x = 0, int y = 0) {//x,y값이 주어지지 않을경우 0,0으로 초기화되지만 입력되는 경우에는 각각 x,y값을 넣어줌
		this->x = x;
		this->y = y;
	}

	int getSquareDistanceTo(const Point2D & target) const { //this에서 target까지의 거리의 제곱을 구하는 함수
		int dx = abs(this->x - target.x); //지금 점의 x좌표와 대상 x좌표의 차이를 델타x로 명명함 abs는 그 차이가 마이너스일수도 있기때문에 절댓값을 반환하기 위함
		int dy = abs(this->y - target.y); //지금 점의 y좌표와 대상 y좌표의 차이를 델타y로 명명함 abs는 그 차이가 마이너스일수도 있기때문에 절댓값을 반환하기 위함
		return dx * dx + dy * dy; //어차피 제곱근은 getDistanceTo에서 해주므로 제곱해서 더한 값만을 return함
	}

	double getDistanceTo(const Point2D& target) const { //getSquareDistanceTo에서 구한 제곱에 제곱근을 씌워 거리를 구하는 함수
		double sqd = (double)this->getSquareDistanceTo(target); // sqd에 getSquareDistanceTo에서 구한 값을 저장
		return sqrt(sqd); //제곱을 씌워 retrun
	}
};

int main() {
	int n; //몇개의 별이 존재하는지를 저장받을 변수
	Point2D* points; //별이 n개 존재하므로 포인터변수로 선언하여 동적할당을 사용하기 위함

	scanf("%d", &n); //별의 개수를 입력받음
	points = new Point2D[n]; //별의 개수만큼 동적할당을 시켜줌

	for (int i = 0; i < n; i++) { //n번만큼 별의 좌표를 입력받은 후 그 값으로 point[i]번째 인덱스를 초기화 시킴
		int x, y;
		scanf("%d %d", &x, &y); //x,y입력받음

		points[i] = Point2D(x, y);//자세한 용어는 기억이 나지 않지만 입력값을 토대로 class 내의 변수를 초기화시켜주는 함수였던것 같습니다.
	}

	int min_sqd = INT_MAX; //최소 거리는 INT 자료형의 최대값으로 설정 그래야 나중에 다른값으로 초기화 되기 편함
	int min_cnt = 0; //초기값은 0으로 지정

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			int sqd = points[i].getSquareDistanceTo(points[j]); //sqd에 i번째 인덱스의 천체와 j번째 인덱스의 거리값을 삽입함
			if (sqd < min_sqd) { //만약 그 값이 min_sqd보다 작을 경우 실행
				min_sqd = sqd; //i,j간의 거리로 값을 초기화 시켜주고
				min_cnt = 1; //쌍이 새로 하나 생긴것이므로 1로 초기화
			}
			else if (sqd == min_sqd) { //min_sqd와 i,j간의 sqd가 같은경우 쌍이 하나 더 있는것이므로 ++해줌
				min_cnt++;
			}
		}
	}

	double distance = sqrt(min_sqd); //거리는 제곱으로 구했으므로 이에 제곱근을 씌어주어야함
	printf("%.1f\n", distance); //그렇게 구한 거리 출력
	printf("%d\n", min_cnt); //쌍의 갯수 출력

	delete[] points; //동적할당하였으므로 메모리 해제
	return 0; //메인 함수 종료
}
