def solution(N: int):
    T = [0]*(N+1)
    T[0] = 1

    for i in range(1, N+1):
        for j in range(i):
            T[i] += T[j] * T[i-1-j]
    return T[N]


def test_solution():
    assert solution(3) == 5
    assert solution(25) == 4861946401452


if __name__ == "__main__":
    print(solution(int(input())))
