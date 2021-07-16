#include <iostream>
#include <string>
#include <stack>
#include <vector>

using namespace std;


class Parenthesis {
public:
	bool type;  // 열린 괄호면 true, 닫힌 괄호면 false
	int index;  // 해당 괄호의 인덱스

	Parenthesis(int index, bool type) { //생성자 함수
		this->index = index;
		this->type = type;
	}

	Parenthesis(int index, char c) { //bool 타입이 아닐때 생성자
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
	
	stack<Parenthesis> stack; // 현재 짝을 찾지 못한 열린 괄호

	for (int i = 0; i < parentheses.size(); i++) {
		
		Parenthesis p = parentheses[i]; // 왼쪽부터 오른쪽의 괄호를 차례로 조회

		if (p.type == true) 			
			stack.push(p); // 열린 괄호라면 짝을 찾을 때 까지 스택에 보관
		
		else if (p.type == false) { // 닫힌 괄호 p에 대하여
			

			if (stack.size() > 0 && stack.top().type == true) { // 가장 마지막에 추가된 열린 괄호와 짝을 맞출 수 있으므로 제거
				stack.pop();
			}
			else {
				return false; // 짝을 맞출 수 있는 열린 괄호가 없다면 올바르지 않은 괄호 문자열
			}
		}
	}

	if (stack.size() > 0) {
		return false; // 아직 스택에 짝을 찾지 못한 열린 괄호가 남아 있음
	}

	return true;
}

void process(int caseIndex) {
	string str;
	cin >> str; //()()을 입력받음

	vector<Parenthesis> parentheses; //벡터배열로 선언함
	for (int i = 0; i < str.length(); ++i) {
		parentheses.push_back(Parenthesis(i, str[i])); //vector 배열에 저장함
	}

	bool isValid = isValidParentheses(parentheses); //벡터를 변수로 풀이함수를 실행

	if (isValid) { //짝을 다 이루면 YES
		cout << "YES" << endl;
	}
	else { //안 이루면 NO
		cout << "NO" << endl;
	}
}

int main() { 
	int caseSize; //caseSize만큼 실행
	cin >> caseSize;

	for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) { //케이스 횟수만큼 실행하고 종료
		process(caseIndex);
	}
}