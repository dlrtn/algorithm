#include <cstdio>
#include <vector>

using namespace std;

class TicketTable {
public:
	vector<bool> used; //지급이 됐는지 안됐는지를 저장하는 변수 쉽게하기 위해서 bool을 사용한 듯합니다
	int length; //회원번호를 저장하는 변수

	TicketTable(int length) { //초기 class를 초기화시켜주는 생성자
		this->length = length;
		this->used.assign(length, false); //처음과 끝을 초기화시켜주는 함수라고 합니다.
	}

	int findEmptyIndexByUserId(int userId) { //사용자의 회원 번호로 지급받게 될 행운권 번호를 계산하는 메소드
		int index = userId % length;    // 가장 초기에 시도 할 티켓 번호
		while (this->isEmpty(index) == true) {   // 사용된 티켓 번호라면 건너 뜀
			index = (index + 1) % length;   // 다음 번호를 조사
		}
		return index; // 사용되지 않은 인덱스를 찾아서 반환
	}

	bool isEmpty(int ticketIndex) { //해당 행운권 번호가 이미 사용 중인지 여부를 반환하는 메소드
		return this->used[ticketIndex]; // 사용여부 <==> used[ticketIndex]
	}
	
	void setUsed(int index, bool status) { //티켓 사용 여부를 갱신하기 위한 메소드
		this->used[index] = status; //사용여부를 입력받아 해당 인덱스에 저장함
	}
};

vector<int> getTicketNumbers(int n, int m, const vector<int>& ids) { 
	vector<int> tickets; //저장할 tickets 정수형 벡터 선언
	TicketTable table = TicketTable(n); //n개만큼 생성함 n은 전체 티켓수임

	for (int i = 0; i < m; i++) { //회원 번호 갯수만큼 계산하기 위함
		int ticketIndex = table.findEmptyIndexByUserId(ids[i]); //각 인덱스별 회원번호를 들고 계산하러 가서 해당 인덱스가 비어있는지 확인하고 안비어있다면 넘어가는 식으로 결국 비어있는 인덱스를 반환
		tickets.push_back(ticketIndex); //tickets에 해당 인덱스를 삽입하고
		table.setUsed(ticketIndex, true); //그 인덱스가 사용되었음을 반환함
	}

	return tickets; //최종적으로 사용된 인덱스를 회원번호 수만큼 리턴함
}

int main() {	
	int n, m; // n: 전체 티켓의 수 m: 요청 고객의 수
	scanf("%d%d", &n, &m); //입력받음

	vector<int> ids(m); //int배열인 ids를 m개만큼 선언함, 회원번호를 저장하는 변수임
	for (int i = 0; i < m; ++i) { //m개만큼 받음
		scanf("%d", &ids[i]); //인덱스별로 회원번호를 저장하여 연산함
	}

	vector<int> tickets = getTicketNumbers(n, m, ids); //tickets라는 정수형 벡터에 getTicketNumbers에 n,m,ids를 가지고 계산한 값을 저장함. 반환형이 vector임
	for (int i = 0; i < tickets.size(); ++i) //사용된 회원번호를 출력해주는 함수
		printf("%d\n", tickets[i]);
	
}