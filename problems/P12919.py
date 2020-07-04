def solution(start: str, to: str):
    goalLength = len(to)
    result = [False]

    def dfs(start):
        if (len(start)) == goalLength:
            if start == to:
                result[0] = True
            return
        dfs(start + 'A')
        dfs((start + 'B')[::-1])
    dfs(start)
    return result[0]


def test_solution():
    from utils import check_time_limit
    warped_solution = check_time_limit(solution, 2 / (2**50))
    assert solution('A', 'BABA') == True
    assert solution('BAAAAABAA', 'BAAAAABAA') == True
    assert solution('A', 'ABBA') == False


if __name__ == "__main__":
    start = input()
    to = input()
    if solution(start, to):
        print(1)
    else:
        print(0)
