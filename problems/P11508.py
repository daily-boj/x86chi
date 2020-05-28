from sys import stdin


def solution(C: list):
    answer = 0
    C.sort(reverse=True)
    while C:
        lenght = len(C)
        if lenght < 3:
            answer += sum(C)
            break
        answer += sum(C[:2])
        C = C[3:]
    return answer


def test_solution():
    from utils import check_time_limit
    warped_solution = check_time_limit(solution, 1)
    assert warped_solution([3, 2, 3, 2]) == 8
    assert warped_solution([6, 4, 5, 5, 5, 5]) == 21


if __name__ == "__main__":
    print(solution([int(stdin.readline())
                    for i in range(int(stdin.readline()))]))
