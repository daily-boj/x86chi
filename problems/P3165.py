import re


def solution(N: str, K: int):
    return re.sub(r'^0+', '', find(N.zfill(16), K))


def find(N: str, K: int):
    length = len(N)
    if length < K:
        return False
    if length == K:
        expect = '5'*K
        if N < expect:
            return expect
        return False
    if length == 1:
        if N == '9':
            return False
        return str(1 + int(N))

    rest = N[1:]
    attempt = None
    if N[0] == '5':
        attempt = find(rest, K-1)
    else:
        attempt = find(rest, K)

    if attempt:
        return N[0] + attempt

    if N[0] == '9':
        return False
    if N[0] == '4':
        return '5' + '0' * (length-K) + '5' * (K-1)
    return str(int(N[0])+1) + '0' * (length-K-1) + '5' * K


def test_find():
    assert solution('595'.zfill(16), 2) == '655'
    assert solution('4'.zfill(16), 2) == '55'


if __name__ == "__main__":
    N, K = input().split()
    print(solution(N, int(K)))
