from typing import List, Tuple


def solve_n_queens(n: int = 8) -> List[List[Tuple[int, int]]]:
    """回溯法求解n皇后问题，返回所有解的坐标列表"""
    solutions = []
    board = [-1] * n  # board[row] = col 记录每行列位置

    def is_safe(row: int, col: int) -> bool:
        """判断(row, col)位置放皇后是否安全"""
        for i in range(row):
            # 列冲突 或 对角线冲突
            if board[i] == col:
                return False
        return True

    def backtrack(row: int) -> None:
        """递归回溯填充皇后"""
        if row == n:
            # 记录当前解的坐标
            solution = [(i, board[i]) for i in range(n)]
            solutions.append(solution)
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)
    return solutions


def print_board(solution: List[Tuple[int, int]], n: int = 8) -> str:
    """将解转换为可视化棋盘字符串"""
    board = [['.' for _ in range(n)] for _ in range(n)]
    for r, c in solution:
        board[r][c] = 'Q'
    return '\n'.join(' '.join(row) for row in board)


if __name__ == "__main__":
    # 主程序入口：执行求解并打印结果
    print("=== 8皇后问题求解中 ===")
    all_solutions = solve_n_queens(8)
    print(f"共找到 {len(all_solutions)} 个有效解")

    # 打印第一个解的可视化棋盘
    print("第一个解的棋盘布局：")
    print(print_board(all_solutions[0]))
