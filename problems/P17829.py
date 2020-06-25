from typing import List


def solution(matrix: List[List[int]]):
    while len(matrix) != 1:
        matrix = pulling(matrix)
    return matrix[0][0]


def pulling(matrix: List[List[int]]):
    length = len(matrix)
    pulled = [[None]*(length//2) for __ in range(length//2)]

    for i in range(0, length, 2):
        for j in range(0, length, 2):
            pulled[i//2][j//2] = sorted([matrix[i][j],
                                         matrix[i][j+1],
                                         matrix[i+1][j],
                                         matrix[i+1][j+1]])[2]
    return pulled


def test_solution():
    from utils import check_time_limit
    warped_solution = check_time_limit(solution, 0.0078125)
    assert warped_solution([[-6, -8, 7, -4],
                            [-5, -5, 14, 11],
                            [11, 11, -1, -1],
                            [4, 9, -2, -4]]) == 11
    assert warped_solution([[-1, 2, 14, 7, -4, 5, 8, 9],
                            [10, 6, 23, 2, 1, 1, 7, 11],
                            [9, 3, 5, -2, 4, 4, 6, 6],
                            [7, 15, 0, 8, 21, 9, 6, 6],
                            [19, 8, 12, -8, 4, 5, 2, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8],
                            [9, 10, 11, 12, 13, 14, 15, 16],
                            [17, 18, 19, 20, 21, 22, 23, 24]]) == 17


def test_pulling():
    assert pulling([[1, 2], [3, 4]]) == [[3]]
    assert pulling([[-6, -8, 7, -4],
                    [-5, -5, 14, 11],
                    [11, 11, -1, -1],
                    [4, 9, -2, -4]]) == [[-5, 11], [11, -1]]


if __name__ == "__main__":
    matrix = [list(map(int, input().split())) for __ in range(int(input()))]
    print(solution(matrix))
