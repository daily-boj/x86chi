def ccw(first: list, second: list, third: list):
    cross_porduct = (second[0] - first[0])*(third[1] - first[1]) - \
        (third[0] - first[0])*(second[1] - first[1])
    if cross_porduct > 0:
        return 1
    if cross_porduct < 0:
        return -1
    return 0


def comparator(left: list, right: list):
    if left[0] == right[0]:
        return left[1] <= right[1]
    return left[0] <= right[1]


def solution(first: list, second: list):
    first_scope = ccw(*first, second[0]) * ccw(*first, second[1])
    second_scope = ccw(*second, first[0]) * ccw(*second, first[1])

    if first_scope == 0 and second_scope == 0:
        return False

    return first_scope <= 0 and second_scope <= 0


def test_solution():
    assert solution([[0, 0], [6, 2]], [[5, -4], [2, 2]]) == True
    assert solution([[-1, -5], [6, 3]], [[1, 10], [-4, -1]]) == False


if __name__ == "__main__":
    lines = list(map(int, input().split()))
    if solution([lines[:2], lines[2:4]], [lines[4:6], lines[6:]]):
        print(1)
    else:
        print(0)
