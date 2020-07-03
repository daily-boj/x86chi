offsets = [1, 2, 3, 4, 5, 4, 3, 2]

def solution(n: int):
    offset = (n-1) % 8
    return offsets[offset]

def test_solution():
    assert solution(3) == 3
    assert solution(1000) == 2

if __name__ == "__main__":
    print(solution(int(input())))
