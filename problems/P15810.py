from typing import List


def solution(staffs: List[int], makeTO: int):
    low = 0
    heigh = 1000000000000

    while low < heigh:
        mid = (low + heigh) // 2
        result = sum(map(lambda staff: mid // staff, staffs))
        if result < makeTO:
            low = mid + 1
        else:
            heigh = mid
    return low


def test_solution():
    assert solution([5, 7, 3], 8) == 14


if __name__ == "__main__":
    makeTO = int(input().split()[1])
    staffs = list(map(int, input().split()))
    print(solution(staffs, makeTO))
