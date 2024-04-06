# 등수 구하기

# 문제
# 랭킹 리스트에 올라 갈 수 있는 점수의 개수 P가 주어진다. 그리고 리스트에 있는 점수 N개가 비오름차순으로 주어지고, 태수의 새로운 점수가 주어진다.
# 이때, 태수의 새로운 점수가 랭킹 리스트에서 몇 등 하는지 구하는 프로그램을 작성하시오.
# 만약 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1을 출력한다.
# 만약, 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다.

# 입력
# 첫째 줄에 N, 태수의 새로운 점수, 그리고 P가 주어진다.
# P는 10보다 크거나 같고, 50보다 작거나 같은 정수, N은 0보다 크거나 같고, P보다 작거나 같은 정수이다.
# 그리고 모든 점수는 2,000,000,000보다 작거나 같은 자연수 또는 0이다. 둘째 줄에는 현재 랭킹 리스트에 있는 점수가 비오름차순으로 주어진다.
# 둘째 줄은 N이 0보다 큰 경우에만 주어진다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다.

# TC
# 10 1 10
# 10 9 8 7 6 5 4 3 3 0

# Idea
# 내림차로 주니까 정렬할 필요도 없고
# 단순 구현 문제네
# 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀌니까 내 등수랑 나랑 동점인 애들이랑 따로 카운트를 해줘야겠다

# Code
import sys
sys.stdin = open("../input.txt", "r")

def solve():
    N, score, P = map(int, input().split())
    # 랭킹에 아무도 없다?
    if not N:
        print(1)
        return
    rank = list(map(int, input().split()))
    my_rank = 1
    same_score = 0
    for i in rank:
        # 점수가 높다?
        if i > score:
            my_rank += 1
        # 동점을 발견했다?
        elif i == score:
            same_score += 1
        # 성능을 위한 브레이크
        else:
            break

    # 랭킹 리스트가 꽉 찼다?
    if my_rank + same_score > P:
        print(-1)
        return
    # 아니면 프린트
    print(my_rank)

if __name__ == "__main__":
    solve()