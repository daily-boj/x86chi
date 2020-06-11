def solution(coins: str):
    binarys = coins.replace('H', '1').replace('T', '0')
    answer = [0]*8
    for index in range(38):
        answer[int(binarys[index:index+3], 2)] += 1
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
