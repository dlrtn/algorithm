#include <iostream>
#include <string>
#include <stack>
#include <vector>

using namespace std;


class Parenthesis {
public:
	bool type;  // ���� ��ȣ�� true, ���� ��ȣ�� false
	int index;  // �ش� ��ȣ�� �ε���

	Parenthesis(int index, bool type) { //������ �Լ�
		this->index = index;
		this->type = type;
	}

	Parenthesis(int index, char c) { //bool Ÿ���� �ƴҶ� ������
		this->index = index;
		if (c == '(') {
			this->type = true;
		}
		else {
			this->type = false;
		}
	}
};

bool isValidParentheses(const vector<Parenthesis>& parentheses) {
	
	stack<Parenthesis> stack; // ���� ¦�� ã�� ���� ���� ��ȣ

	for (int i = 0; i < parentheses.size(); i++) {
		
		Parenthesis p = parentheses[i]; // ���ʺ��� �������� ��ȣ�� ���ʷ� ��ȸ

		if (p.type == true) 			
			stack.push(p); // ���� ��ȣ��� ¦�� ã�� �� ���� ���ÿ� ����
		
		else if (p.type == false) { // ���� ��ȣ p�� ���Ͽ�
			

			if (stack.size() > 0 && stack.top().type == true) { // ���� �������� �߰��� ���� ��ȣ�� ¦�� ���� �� �����Ƿ� ����
				stack.pop();
			}
			else {
				return false; // ¦�� ���� �� �ִ� ���� ��ȣ�� ���ٸ� �ùٸ��� ���� ��ȣ ���ڿ�
			}
		}
	}

	if (stack.size() > 0) {
		return false; // ���� ���ÿ� ¦�� ã�� ���� ���� ��ȣ�� ���� ����
	}

	return true;
}

void process(int caseIndex) {
	string str;
	cin >> str; //()()�� �Է¹���

	vector<Parenthesis> parentheses; //���͹迭�� ������
	for (int i = 0; i < str.length(); ++i) {
		parentheses.push_back(Parenthesis(i, str[i])); //vector �迭�� ������
	}

	bool isValid = isValidParentheses(parentheses); //���͸� ������ Ǯ���Լ��� ����

	if (isValid) { //¦�� �� �̷�� YES
		cout << "YES" << endl;
	}
	else { //�� �̷�� NO
		cout << "NO" << endl;
	}
}

int main() { 
	int caseSize; //caseSize��ŭ ����
	cin >> caseSize;

	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) { //���̽� Ƚ����ŭ �����ϰ� ����
		process(caseIndex);
	}
}