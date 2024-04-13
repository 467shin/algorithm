# 진우의 달 여행 (Small)

# 문제
# 지구와 우주사이는 N X M 행렬로 나타낼 수 있으며 각 원소의 값은 우주선이 그 공간을 지날 때 소모되는 연료의 양이다.
# 진우는 여행경비를 아끼기 위해 조금 특이한 우주선을 선택하였다. 진우가 선택한 우주선의 특징은 아래와 같다.
# 1. 지구 -> 달로 가는 경우 우주선이 움직일 수 있는 방향은 아래로 3방향.
# 2. 우주선은 전에 움직인 방향으로 움직일 수 없다. 즉, 같은 방향으로 두번 연속으로 움직일 수 없다.
# 진우의 목표는 연료를 최대한 아끼며 지구의 어느위치에서든 출발하여 달의 어느위치든 착륙하는 것이다.
# 최대한 돈을 아끼고 살아서 달에 도착하고 싶은 진우를 위해 달에 도달하기 위해 필요한 연료의 최소값을 계산해 주자.

# 입력
# 첫줄에 지구와 달 사이 공간을 나타내는 행렬의 크기를 나타내는 N, M (2≤ N, M ≤ 6)이 주어진다.
# 다음 N줄 동안 각 행렬의 원소 값이 주어진다. 각 행렬의 원소값은 100 이하의 자연수이다.

# 출력
# 달 여행에 필요한 최소 연료의 값을 출력한다.

# TC
# 6 4
# 5 8 5 1
# 3 5 8 4
# 9 77 65 5
# 2 1 5 2
# 5 98 1 5
# 4 95 67 58

# Idea
# 백트래킹

# Code
import sys
sys.stdin = open("../input.txt", "r")

def backtracking(cost, row, col, before):
    global res
    if row == N: # 도착했나요?
        res = cost
        return
    cost += matrix[row][col]
    if res and res < cost: # 이전 결과보다 값이 커졌나요?
        return
    for i in range(col-1, col+2):
        if i - col == before: # 혹시 이전행동을 반복하려 하지 않나요?
            continue
        if 0 <= i < M:
            backtracking(cost, row+1, i, i - col) # 째귀

if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for i in range(M):
        backtracking(0, 0, i, 2)
    print(res)