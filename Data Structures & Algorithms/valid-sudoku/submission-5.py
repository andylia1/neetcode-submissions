class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set) #key is tuple

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if (board[r][c] not in rows[r] 
                    and board[r][c] not in cols[c] 
                    and board[r][c] not in boxes[(r//3,c//3)]):
                        rows[r].add(board[r][c])
                        cols[c].add(board[r][c])
                        boxes[(r//3,c//3)].add(board[r][c])
                    else:
                        return False
        return True
