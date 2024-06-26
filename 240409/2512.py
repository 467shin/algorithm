# 예산

# 문제
# 국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다.
# 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다.
# 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.
# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
# 3. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.
# 여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다.
# 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다.
# 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다.

# 출력
# 첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다.

# TC
# 4
# 120 110 140 150
# 485

# Idea
# M이 예산의 총합보다 크거나 같으면 배열의 max값 반환
# M을 N으로 나눈 평균값을 내는 것으로 최솟값을 보장해주고 나머지 백업
# 배열을 정렬하고 반복문을 돌며 평균값에서 예산을 뺀 값을 백업해둔 나머지에 계속 더해준다
# 평균값보다 큰 값이 나오면 나머지를 분배하고 그 값을 평균값으로 한다
# 그래도 평균값보다 크면 남은 돈을 남은 지역의 수로 나누고 브레이크를 한다.

# Code
import sys
sys.stdin = open("input.txt", "r")

def solve():
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    M = int(input())

    # 예산이 더 많거나 딱 떨어질 경우
    if M >= sum(arr):
        print(max(arr))
        return

    budget = M // N # 기본값은 평균
    remainder = M % N # 남은 예산 주머니
    for i in range(N):
        # 예상보다 예산이 적은 도시의 경우
        if arr[i] <= budget:
            remainder += budget - arr[i] # 넘친 예산을 나머지에 넣어 준다
            continue
        # 아닐 경우 나머지를 남은 도시들의 수로 나눠 고루 분배한다.
        else:
            budget += remainder // (N - i)
            remainder = remainder % (N - i)

        # 나머지를 분배한 뒤에도 예산이 모자랄 시, 남은 돈을 남은 지역에 전부 분배한다.
        if arr[i] > budget:
            budget = (M - sum(arr[:i])) // (N - i)
            break
    print(budget)

if __name__ == "__main__":
    solve()
