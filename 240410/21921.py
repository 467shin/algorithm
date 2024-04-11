# 블로그

# 문제
# X일 동안 가장 많이 들어온 방문자 수와 그 기간들을 알고 싶다.
# X일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구해주자.

# 입력
# 첫째 줄에 블로그를 시작하고 지난 일수 N와 X가 공백으로 구분되어 주어진다.
# 둘째 줄에는 블로그 시작 1일차부터 N일차까지 하루 방문자 수가 공백으로 구분되어 주어진다.

# 출력
# 첫째 줄에 X일 동안 가장 많이 들어온 방문자 수를 출력한다.
# 만약 최대 방문자 수가 0명이라면 SAD를 출력한다.
# 만약 최대 방문자 수가 0명이 아닌 경우 둘째 줄에 기간이 몇 개 있는지 출력한다.

# 제한
# 1 <= X <= N <= 250,000
# 0 <= 방문자 수 <= 8,000

# TC
# 5 2
# 1 4 2 5 1

# Idea
# 반복문 돌며 배열 인덱싱해서 기록하면 될 것 같다.
# 과도한 슬라이싱으로 인해 시간 초과를 두들겨 맞아서 범위 합을 변수에 기록해두고 i를 빼고 i+N을 더하는 식으로 로직을 바꾸었다.

# Code
import sys
sys.stdin = open("../input.txt", "r")

def solve():
    X, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # 내 블로그 같으면
    if sum(arr) == 0:
        print('SAD')
        return

    # 첫 번째 구간합은 과감하게 슬라이싱
    visitor = sum(arr[:N])
    max = 0
    cnt = 1
    for i in range(X):
        # max값 갱신
        if max < visitor:
            max = visitor
            cnt = 1
        # 중복값 카운팅
        elif max == visitor:
            cnt += 1
        # N+i가 배열의 마지막일 경우 루프 종료
        if N + i >= X:
            break
        # 구간합 갱신
        visitor = visitor - arr[i] + arr[N+i]

    print(max)
    print(cnt)

if __name__ == "__main__":
    solve()
