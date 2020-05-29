def solution(N: int, coins: list, goal: int):
    first_dimension = [None for __ in range(N)]
    counts = [first_dimension.copy() for __ in range(goal+1)]

    def pay(goal: int, N: int):
        count = 0
        if N == 1:
            if goal % coins[0] == 0:
                return 1
            return 0
        for i in range(goal // coins[N - 1] + 1):
            _goal = goal - coins[N - 1] * i
            maxIndex = N-1

            if counts[_goal][maxIndex] == None:
                counts[_goal][maxIndex] = pay(_goal, maxIndex)

            count += counts[_goal][maxIndex]
        return count
    return pay(goal, N)


def test_solution():
    from utils import check_time_limit
    warped_solution = check_time_limit(solution, 0.01)
    assert warped_solution(2, [1, 2], 1000) == 501
    assert warped_solution(3, [1, 5, 10], 100) == 121
    assert warped_solution(2, [5, 7], 22) == 1


if __name__ == "__main__":
    count = int(input())
    for __ in range(count):
        N = int(input())
        coins = list(map(int, input().split(' ')))
        goal = int(input())
        print(solution(N, coins, goal))
