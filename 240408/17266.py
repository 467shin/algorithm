# 크로스 컨트리

# 문제
# 굴다리 모든 길 0~N을 밝히게 가로등을 설치해 달라고 인천광역시에 민원을 넣었다.
# 인천광역시에서 가로등을 설치할 개수 M과 각 가로등의 위치 x들의 결정을 끝냈다.
# 각 가로등은 높이만큼 주위를 비출 수 있다. (가로등의 높이가 H라면 왼쪽으로 H, 오른쪽으로 H만큼 주위를 비춘다.)
# 최소한의 높이로 굴다리 모든 길 0~N을 밝히고자 한다.
# 단 가로등은 모두 높이가 같아야 하고, 정수이다.

# 입력
# 첫 번째 줄에 굴다리의 길이 N 이 주어진다. (1 ≤ N ≤ 100,000)
# 두 번째 줄에 가로등의 개수 M 이 주어진다. (1 ≤ M ≤ N)
# 다음 줄에 M 개의 설치할 수 있는 가로등의 위치 x 가 주어진다. (0 ≤ x ≤ N)
# 가로등의 위치 x는 오름차순으로 입력받으며 가로등의 위치는 중복되지 않으며, 정수이다.

# 출력
# 굴다리의 길이 N을 모두 비추기 위한 가로등의 최소 높이를 출력한다.

# TC
# 5
# 2
# 2 4

# Idea
# 가자, while loop
# arr에 들어있는 가로등의 위칫값 2는 밝힐 구간의 idx 1과 2의 사이라는 것에만 유의하자.
# 라고 생각했지만 시간초과를 두들겨 맞고 그리디하게 풀기로 마음을 먹었다.
# 거리 재서 max값 뽑으면 되는 것 아닌가

# Code
import sys
sys.stdin = open("../input.txt", "r")

def solve():
    N = int(input())
    M = int(input())
    arr = list(map(int, input().split()))
    distance_arr = [1]
    last_light = 0
    for i in arr:
        now = i
        # 가로등의 사이사이는 2로 나누고 나머지가 있을 경우 1을 더한다
        if len(distance_arr) > 1:
            now = ((i - last_light) // 2)
            if (i - last_light) % 2:
                now += 1
        # 마지막 가로등이면 끝까지의 거리를 배열에 넣는다.
        if i == arr[-1]:
            distance_arr.append(N - i)

        # 이전 가로등의 위치 백업
        last_light = i
        distance_arr.append(now)

    print(max(distance_arr))

if __name__ == "__main__":
    solve()

# 소감
# 마지막 가로등의 위치 백업을 안 해서 823418번 틀렸다. 아무래도 치과 때문에 심신미약이었나보다.