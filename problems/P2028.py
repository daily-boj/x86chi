from math import log10, floor


def solution(number):
    squared = number * number
    length = floor(log10(number)) + 1
    return number == squared % (10**length)


def test_solution():
    assert solution(1) == True
    assert solution(6) == True
    assert solution(76) == True
    assert solution(89) == False


if __name__ == "__main__":
    for __ in range(int(input())):
        if solution(int(input())):
            print('YES')
        else:
            print('NO')
