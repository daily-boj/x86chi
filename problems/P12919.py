def solution(start: str, to: str):
    goalLength = len(start)

    def backtrack(to: str):
        if (len(to)) == goalLength:
            return start == to

        if to[0] == 'A':
            if to[-1] == 'A':
                return backtrack(to[:-1])
            return False  # A~B의 경우는 없다.

        # B~A 1, 2 가능
        # B~B 2 가능한다
        if to[-1] == 'A':
            return backtrack(to[:-1]) or backtrack(to[::-1][:-1])
        return backtrack(to[::-1][:-1])

    return backtrack(to)


# 1) 맨 뒤에 A를 붙인다
# 2) 맨 뒤에 B를 붙이고 뒤집기= > 뒤집고 앞에 B 붙이기


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
