import pytest
from src.eight_queens import solve_n_queens

def test_8_queens_solution_count():
    """验证8皇后问题的解总数为92"""
    solutions = solve_n_queens(8)
    assert len(solutions) == 92

def test_4_queens_solution_count():
    """验证4皇后问题的解总数为2（用于边界测试）"""
    solutions = solve_n_queens(4)
    assert len(solutions) == 2

def test_all_solutions_valid():
    """验证所有解的合法性（无行列/对角线冲突）"""
    solutions = solve_n_queens(8)
    for sol in solutions:
        rows = set()
        cols = set()
        diags1 = set()
        diags2 = set()
        for (r, c) in sol:
            rows.add(r)
            cols.add(c)
            diags1.add(r - c)
            diags2.add(r + c)
        assert len(rows) == 8
        assert len(cols) == 8
        assert len(diags1) == 8
        assert len(diags2) == 8
