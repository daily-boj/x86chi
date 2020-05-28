import sys

ignore = {'i': True, 'pa': True, 'te': True, 'ni': True, 'niti': True,
          'a': True, 'ali': True, 'nego': True, 'no': True, 'ili': True}


def solution(words: str):
    words = words.split(' ')
    answer = words[0][0].upper()
    for index in range(1, len(words)):
        if ignore.get(words[index]):
            continue
        answer += words[index][0].upper()
    return answer


def test_solution():
    from utils import check_time_limit
    warped_solution = check_time_limit(solution, 1)
    assert warped_solution('micro soft') == 'MS'
    assert warped_solution('biti ali i ne biti') == 'BNB'
    assert warped_solution('ali ja sam i jucer jeo') == 'AJSJJ'


if __name__ == "__main__":
    print(solution(sys.stdin.readline()))
