#include <cstdio>
#include <vector>

using namespace std;

class TicketTable {
public:
	vector<bool> used; //������ �ƴ��� �ȵƴ����� �����ϴ� ���� �����ϱ� ���ؼ� bool�� ����� ���մϴ�
	int length; //ȸ����ȣ�� �����ϴ� ����

	TicketTable(int length) { //�ʱ� class�� �ʱ�ȭ�����ִ� ������
		this->length = length;
		this->used.assign(length, false); //ó���� ���� �ʱ�ȭ�����ִ� �Լ���� �մϴ�.
	}

	int findEmptyIndexByUserId(int userId) { //������� ȸ�� ��ȣ�� ���޹ް� �� ���� ��ȣ�� ����ϴ� �޼ҵ�
		int index = userId % length;    // ���� �ʱ⿡ �õ� �� Ƽ�� ��ȣ
		while (this->isEmpty(index) == true) {   // ���� Ƽ�� ��ȣ��� �ǳ� ��
			index = (index + 1) % length;   // ���� ��ȣ�� ����
		}
		return index; // ������ ���� �ε����� ã�Ƽ� ��ȯ
	}

	bool isEmpty(int ticketIndex) { //�ش� ���� ��ȣ�� �̹� ��� ������ ���θ� ��ȯ�ϴ� �޼ҵ�
		return this->used[ticketIndex]; // ��뿩�� <==> used[ticketIndex]
	}
	
	void setUsed(int index, bool status) { //Ƽ�� ��� ���θ� �����ϱ� ���� �޼ҵ�
		this->used[index] = status; //��뿩�θ� �Է¹޾� �ش� �ε����� ������
	}
};

vector<int> getTicketNumbers(int n, int m, const vector<int>& ids) { 
	vector<int> tickets; //������ tickets ������ ���� ����
	TicketTable table = TicketTable(n); //n����ŭ ������ n�� ��ü Ƽ�ϼ���

	for (int i = 0; i < m; i++) { //ȸ�� ��ȣ ������ŭ ����ϱ� ����
		int ticketIndex = table.findEmptyIndexByUserId(ids[i]); //�� �ε����� ȸ����ȣ�� ��� ����Ϸ� ���� �ش� �ε����� ����ִ��� Ȯ���ϰ� �Ⱥ���ִٸ� �Ѿ�� ������ �ᱹ ����ִ� �ε����� ��ȯ
		tickets.push_back(ticketIndex); //tickets�� �ش� �ε����� �����ϰ�
		table.setUsed(ticketIndex, true); //�� �ε����� ���Ǿ����� ��ȯ��
	}

	return tickets; //���������� ���� �ε����� ȸ����ȣ ����ŭ ������
}

int main() {	
	int n, m; // n: ��ü Ƽ���� �� m: ��û ���� ��
	scanf("%d%d", &n, &m); //�Է¹���

	vector<int> ids(m); //int�迭�� ids�� m����ŭ ������, ȸ����ȣ�� �����ϴ� ������
	for (int i = 0; i < m; ++i) { //m����ŭ ����
		scanf("%d", &ids[i]); //�ε������� ȸ����ȣ�� �����Ͽ� ������
	}

	vector<int> tickets = getTicketNumbers(n, m, ids); //tickets��� ������ ���Ϳ� getTicketNumbers�� n,m,ids�� ������ ����� ���� ������. ��ȯ���� vector��
	for (int i = 0; i < tickets.size(); ++i) //���� ȸ����ȣ�� ������ִ� �Լ�
		printf("%d\n", tickets[i]);
	
}