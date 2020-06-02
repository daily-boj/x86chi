from typing import List


def solution(start: int, gap: int, slot: List[bool]) -> List[bool]:
    index = start - 1
    length = len(slot)
    while index < length:
        if slot[index] == False:
            slot[index] = True
        index += gap
    return slot


def test_solution():
    from utils import check_time_limit
    warped_solution = check_time_limit(solution, 0.01)

    slot = [False]*30
    slot = warped_solution(1, 3, slot)
    assert slot == [True, False, False, True, False, False, True, False, False, True, False, False, True,
                    False, False, True, False, False, True, False, False, True, False, False, True, False, False, True, False, False]

    slot = warped_solution(3, 7, slot)
    assert slot == [True, False, True, True, False, False, True, False, False, True, False, False, True, False,
                    False, True, True, False, True, False, False, True, False, True, True, False, False, True, False, False]

    slot = warped_solution(1, 4, slot)
    assert slot == [True, False, True, True, True, False, True, False, True, True, False, False, True, False,
                    False, True, True, False, True, False, True, True, False, True, True, False, False, True, True, False]


if __name__ == "__main__":
    slot_count, ballon_count = map(int, input().split(' '))
    slot = [False]*slot_count

    for __ in range(ballon_count):
        slot = solution(*map(int, input().split(' ')), slot)

    print(slot.count(False))
