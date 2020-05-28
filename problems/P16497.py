def solution(N: int, data: list, stock: int):
    count = 0
    mapped = [0]*100
    for request in data:
        mapped[request[0]-1] += 1
        mapped[request[1]-1] -= 1

    for i in range(100):
        count += mapped[i]
        if count > stock:
            return 0
    return 1


def test_solution():
    assert solution(3, [[1, 2], [3, 6], [5, 8]], 1) == 0
    assert solution(3, [[1, 2], [3, 4], [5, 8]], 1) == 1
    assert solution(3, [[1, 2], [3, 6], [5, 8]], 2) == 1


if __name__ == "__main__":
    from sys import stdin
    N = int(stdin.readline())
    data = [list(map(int, stdin.readline().split(' '))) for __ in range(N)]
    stock = int(stdin.readline())
    print(solution(N, data, stock))
