def solution(commands: str):
    NEXT_X = (0, -1, 0, 1)
    NEXT_Y = (1, 0, -1, 0)
    x = y = 0
    direction = 0
    max_x = min_x = max_y = min_y = 0

    for command in commands:
        if command == 'F':
            x += NEXT_X[direction]
            y += NEXT_Y[direction]
        elif command == 'B':
            x -= NEXT_X[direction]
            y -= NEXT_Y[direction]
        elif command == 'L':
            direction = (direction + 1) % 4
        else:
            direction = (direction + 3) % 4

        max_x = max(max_x, x)
        min_x = min(min_x, x)

        max_y = max(max_y, y)
        min_y = min(min_y, y)

    return (max_x - min_x) * (max_y - min_y)


def test_solution():
    assert solution('FFLF') == 2
    assert solution('FFRRFF') == 0
    assert solution('FFFBBBRFFFBBB') == 9


if __name__ == "__main__":
    for __ in range(int(input())):
        print(solution(input()))
