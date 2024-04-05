# 올림픽

# 올림픽은 참가에 의의가 있기에 공식적으로는 국가간 순위를 정하지 않는다. 그러나, 많은 사람들이 자신의 국가가 얼마나 잘 하는지에 관심이 많기 때문에 비공식적으로는 국가간 순위를 정하고 있다. 두 나라가 각각 얻은 금, 은, 동메달 수가 주어지면, 보통 다음 규칙을 따라 어느 나라가 더 잘했는지 결정한다.
# 1. 금메달 수가 더 많은 나라
# 2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
# 3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라
# 각 국가는 1부터 N 사이의 정수로 표현된다. 한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1로 정의된다. 만약 두 나라가 금, 은, 동메달 수가 모두 같다면 두 나라의 등수는 같다. 예를 들어, 1번 국가가 금메달 1개, 은메달 1개를 얻었고, 2번 국가와 3번 국가가 모두 은메달 1개를 얻었으며, 4번 국가는 메달을 얻지 못하였다면, 1번 국가가 1등, 2번 국가와 3번 국가가 공동 2등, 4번 국가가 4등이 된다. 이 경우 3등은 없다.
# 각 국가의 금, 은, 동메달 정보를 입력받아서, 어느 국가가 몇 등을 했는지 알려주는 프로그램을 작성하시오.

# Idea
# K를 뽑아서 그거보다 등수가 높은 애들 갈라내면 되겠네
# 금 은 동 순서대로 비교하되 크면 내 앞자리에 더하고 작으면 넘기고 중간이면 암것도 안하도록

import sys
sys.stdin = open("../input.txt", "r")

# K 찾는 함수
def find_K(arr, K):
    for i in arr:
        if i[0] == K:
            return i

# 랭킹
def ranking(arr, my_K):
    global rank
    for i in arr:
        # 자릿수 비교
        for j in range(1, 4):
            # 크면 랭크 더하고 브레이크
            if i[j] > my_K[j]:
                rank += 1
                break
            # 작으면 탈출
            elif i[j] < my_K[j]:
                break

if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 기본 등수는 1등이다
    rank = 1
    my_K = find_K(arr, K)
    ranking(arr, my_K)
    print(rank)
