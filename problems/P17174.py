def solution(amount: int, groupTO: int):
    count = amount

    while amount > 0:
        amount //= groupTO
        count += amount
    return count


def test_solution():
    assert solution(13, 10) == 14
    assert solution(100, 8) == 113


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
