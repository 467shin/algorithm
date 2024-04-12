# 햄버거 분배

# 문제
# 기다란 벤치 모양의 식탁에 사람들과 햄버거가 아래와 같이 단위 간격으로 놓여 있다.
# 사람들은 자신의 위치에서 거리가 K 이하인 햄버거를 먹을 수 있다.
# 위의 상태에서 K = 1인 경우를 생각해보자. 이 경우 모든 사람은 자신과 인접한 햄버거만 먹을 수 있다.
# 10번의 위치에 있는 사람은 11번 위치에 있는 햄버거를 먹을 수 있다.
# 식탁의 길이 N, 햄버거를 선택할 수 있는 거리 K, 사람과 햄버거의 위치가 주어졌을 때, 햄버거를 먹을 수 있는 사람의 최대 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 두 정수 N과 K가 있다. 그리고 다음 줄에 사람과 햄버거의 위치가 문자 P(사람)와 H(햄버거)로 이루어지는 길이 N인 문자열로 주어진다.

# 출력
# 첫 줄에 햄버거를 먹을 수 있는 최대 사람 수를 나타낸다.

# TC
# 20 2
# HHHHHPPPPPHPHPHPHHHP

# Idea
# 2중 포문으로 구간 순회를 하면 되지 않을까
# 배열의 앞에서부터 먹고
# 먹으면 탈출하고

# Code
import sys
sys.stdin = open("../input.txt", "r")

def solve():
    N, K = map(int, input().split())
    bench = list(input())
    cnt = 0
    for i in range(len(bench)):
        if bench[i] == 'P': # 사람을 발견했다.
            for j in range(i-K, i+K+1): # 앞에서 부터 섭취
                if 0 <= j < N and bench[j] == 'H':
                    cnt += 1
                    bench[j] = 'N'
                    break # 한 개만 먹어요
    print(cnt)

if __name__ == "__main__":
    solve()
