from typing import List

def solution(wires: List[int]):
    table = [-1]
    for wire in wires:
        if wire > table[len(table)-1]:
            table.append(wire)
        else:
            table[lowerBound(table, wire)] = wire
    return len(wires) - len(table) + 1

def lowerBound(table: List[int], k: int):
    low = 0
    high = len(table) - 1

    while low < high:
        mid = (low + high) // 2
        if table[mid] >= k:
            high = mid
        else:
            low = mid + 1
    return high

def test_solution():
    assert solution([2, 3, 4, 1]) == 1

if __name__ == "__main__":
    input()
    print(solution(list(map(int, input().split()))))
