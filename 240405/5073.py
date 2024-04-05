while True:
    arr = list(map(int, input().split()))
    # 종료 조건
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
        # (1, 0), (2, 0), (2, 1) 순으로 빈틈없이 비교하게 된다
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