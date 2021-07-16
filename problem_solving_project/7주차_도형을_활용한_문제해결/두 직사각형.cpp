#include <iostream>
#include <cstdio>

using namespace std;

int get_area(int la, int ra, int ta, int ba, int lb, int rb, int tb, int bb) {
	int l, r, t, b; //겹쳐지는 사각형

	l = max(la, lb); //겹쳐지는 좌표의 왼쪽은 그림상에서 더 우측에 있는 직사각형의 좌표이므로
	r = min(ra, rb); //겹쳐지는 좌표의 오른쪽은 그림상에서 더 좌측에 있는 직사각형의 좌표이므로
	t = min(ta, tb); //겹쳐지는 좌표의 위쪽은 그림상에서 더 낮은 위치에 있는 직사각형의 좌표이므로
	b = max(ba, bb); //겹쳐지는 좌표의 아랫쪽은 그림상에서 더 높은 위치에 있는 직사각형의 좌표이므로

	if (l <= r && b <= t) //면적이 음수가 될수있을때엔 리턴을 하지 않기하기 위해
		return ((r - l) * (t - b));

	return 0;
}

void test_case() {
	int ax, ay, bx, by; //직사각형 A
	int px, py, qx, qy;
	scanf("%d %d %d %d", &ax, &ay, &bx, &by);
	scanf("%d %d %d %d", &px, &py, &qx, &qy);

	int la, ra, ba, ta;//직사각형 A
	la = min(ax, bx);//왼쪽 좌표
	ra = max(ax, bx);//오른쪽 좌표
	ta = max(ay, by);//위에 좌표
	ba = min(ay, by);//아래 좌표

	int lb, rb, bb, tb;//직사각형 B
	lb = min(px, qx);//왼쪽 좌표
	rb = max(px, qx);//오른쪽 좌표
	tb = max(py, qy);//위 좌표
	bb = min(py, qy);//아래 좌표

	int answer = get_area(la, ra, ta, ba, lb, rb, tb, bb); //겹쳐지는 면적을 구해서 리턴하는 함수

	printf("%d\n", answer);
}
int main() {
	int t;
	scanf("%d", &t); //테스트케이스 갯수를 입력받는 변수

	for (int i = 0; i < t; i++)
		test_case();//테스트케이스 갯수만큼 실행

	return 0;
}