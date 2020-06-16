from typing import List
from itertools import combinations


def solution(spaces: List[List[int]]):
    combines = combinations(range(len(spaces)), 2)
    count = 0
    for combine in combines:
        if isBalance(spaces[combine[0]], spaces[combine[1]]):
            count += 1
    return count


def isBalance(A: List[int], B: List[int]):
    def check(i: int, j: int):
        if A[i] < A[j] and B[i] < B[j]:
            return True
        if A[i] == A[j] and B[i] == B[j]:
            return True
        if A[i] > A[j] and B[i] > B[j]:
            return True
        return False
    combines = combinations(range(len(A)), 2)
    for combine in combines:
        if check(*combine) == False:
            return False
    return True


def test_isBalance():
    assert isBalance([1, 3, 2], [12, 50, 31]) == True
    assert isBalance([1, 3, 2], [12, 50, 10]) == False


def test_solution():
    from utils import check_time_limit
    warped_solution = check_time_limit(solution, 0.5)
    assert warped_solution([[20, 10, 30], [10, 20, 60], [80, 25, 79], [
                           30, 50, 80], [80, 25, 81]]) == 2


if __name__ == "__main__":
    M, N = map(int, input().split())
    spaces = [list(map(int, input().split())) for __ in range(M)]
    print(solution(spaces))
