from typing import List


def solution(staffs: List[int], makeTO: int):
    balloon = 0
    time = 1
    while balloon < makeTO:
        for staff in staffs:
            if time % staff == 0:
                balloon += 1
        time += 1
    return time - 1


def test_solution():
    assert solution([5, 7, 3], 8) == 14


if __name__ == "__main__":
    makeTO = int(input().split()[1])
    staffs = list(map(int, input().split()))
    print(solution(staffs, makeTO))
