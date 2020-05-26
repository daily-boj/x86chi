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
    assert solution('micro soft') == 'MS'
    assert solution('biti ali i ne biti') == 'BNB'
    assert solution('ali ja sam i jucer jeo') == 'AJSJJ'


if __name__ == "__main__":
    print(solution(sys.stdin.readline()))
