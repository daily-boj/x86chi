def solution(coins: str):
    answer = [0]*8
    뒤 = 'T'
    for index in range(38):
        first = coins[index]
        second = coins[index+1]
        third = coins[index+2]
        if first == 뒤:
            if second == 뒤:
                if third == 뒤:
                    answer[0] += 1
                else:
                    answer[1] += 1
            else:
                if third == 뒤:
                    answer[2] += 1
                else:
                    answer[3] += 1
        else:
            if second == 뒤:
                if third == 뒤:
                    answer[4] += 1
                else:
                    answer[5] += 1
            else:
                if third == 뒤:
                    answer[6] += 1
                else:
                    answer[7] += 1
    return answer


def test_solution():
    assert solution('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH') == [
        0, 0, 0, 0, 0, 0, 0, 38]
    assert solution('TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT') == [
        38, 0, 0, 0, 0, 0, 0, 0]
    assert solution('HHTTTHHTTTHTHHTHHTTHTTTHHHTHTTHTTHTTTHTH') == [
        4, 7, 6, 4, 7, 4, 5, 1]
    assert solution('HTHTHHHTHHHTHTHHHHTTTHTTTTTHHTTTTHTHHHHT') == [
        6, 3, 4, 5, 3, 6, 5, 6]


if __name__ == "__main__":
    for __ in range(int(input())):
        print(*solution(input()))
