# 삼각형의 세 변

# Equilateral: 세 변의

# Isosceles: 두 변의

# Scalene: 모두 다른

# TC
# 7 7 7
# 6 5 4
# 3 2 5
# 3 2 2
# 0 0 0

import sys
sys.stdin = open("input.txt", "r")

while True:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    res = None
    cnt = 0
    # 배열 순환
    for i in range(len(arr)):
        # 두 변의 합이 나머지 한 변보다 짧으면 삼각형이 될 수 없다.
        if arr[i-1] + arr[i-2] <= arr[i]:
            res = 'Invalid'
            break
        # j를 활용해서 역순으로 크기 비교
        for j in range(i):
            if arr[i] == arr[j]:
                cnt += 1
    if not res:
        if cnt == 0:
            res = 'Scalene'
        elif cnt == 3:
            res = 'Equilateral'
        else:
            res = 'Isosceles'

    print(res)

