import sys


def main():
    HEIGHT, MULTIPLY_TO = map(int, input().split(' '))
    DIV_TO = 1000000007

    multiplied = 1
    answer = 0

    for __ in range(HEIGHT):
        multiplied *= MULTIPLY_TO
        multiplied %= DIV_TO
        answer += int(sys.stdin.readline()) * multiplied
        answer %= DIV_TO

    return answer


def test_main():
    sys.stdin = open('problems/17950.txt', 'r')
    assert main() == 2830


if __name__ == "__main__":
    print(main())
