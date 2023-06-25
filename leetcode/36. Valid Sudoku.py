class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    for k in range(9):
                        if k != j and board[i][k] == board[i][j]:
                            return False
                        if k != i and board[k][j] == board[i][j]:
                            return False

                    if i <= 2:
                        y = 0
                    elif i <= 5:
                        y = 3
                    else:
                        y = 6

                    if j <= 2:
                        x = 0
                    elif j <= 5:
                        x = 3
                    else :
                        x = 6

                    for a in range(y, y + 3):
                        for b in range(x, x + 3):
                            if a != i and b != j and board[a][b] == board[i][j]:
                                return False


        return True