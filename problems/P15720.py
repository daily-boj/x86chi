from math import floor
from typing import List, Tuple


def solution(burgers: List[int], sides: List[int], drinks: List[int]):
    burgers.sort()
    sides.sort()
    drinks.sort()

    original = 0
    discounted = 0
    while burgers or sides or drinks:
        burgers_poped = 0
        sides_poped = 0
        drinks_poped = 0

        if burgers:
            burgers_poped = burgers.pop()
        if sides:
            sides_poped = sides.pop()
        if drinks:
            drinks_poped = drinks.pop()

        accumulated = burgers_poped + sides_poped + drinks_poped

        original += accumulated

        if burgers_poped > 0 and sides_poped > 0 and drinks_poped > 0:
            accumulated = floor((accumulated) * 0.9)

        discounted += accumulated

    return (original, discounted)


def test_solution():
    assert solution([2000, 3000, 2500], [800, 1300, 1000],
                    [500, 1000]) == (12100, 11170)


if __name__ == "__main__":
    input()
    burgers = list(map(int, input().split(' ')))
    sides = list(map(int, input().split(' ')))
    drinks = list(map(int, input().split(' ')))

    answer = solution(burgers, sides, drinks)
    print(answer[0])
    print(answer[1])
