# 타노스

# 문제
# 어느 날, 타노스는 0과 1로 이루어진 문자열 S를 보았다.
# 신기하게도, S가 포함하는 0의 개수와 S가 포함하는 1의 개수는 모두 짝수라고 한다.
# 갑자기 심술이 난 타노스는 S를 구성하는 문자 중 절반의 0과 절반의 1을 제거하여 새로운 문자열 S'를 만들고자 한다.
# S'로 가능한 문자열 중 사전순으로 가장 빠른 것을 구하시오.

# 입력
# 문자열 S가 주어진다.

# 출력
# S'로 가능한 문자열 중 사전순으로 가장 빠른 것을 출력한다.

# TC
# 000011

# Idea
# 1은 앞에서 부터, 0은 뒤에서 부터 지우면 되는거 아녀?

# Code
import sys
sys.stdin = open("input.txt", "r")

def solve():
    S = list(input())
    zero_cnt = S.count('0')
    one_cnt = S.count('1')
    deleted = 0
    for i in range(len(S) - 1, -1, -1):
        if deleted <= zero_cnt // 2 and S[i] == '0':
            print(S[i])
            S[i] = ''
            deleted += 1
            print(deleted, S, S[i])
        print(i)
    deleted = 0
    while deleted <= one_cnt // 2:
        if S[deleted] == '1':
            S[deleted] = ''
        deleted += 1
        print(S)
    res = ''.join(S)
    print(len(res))
    print(str(res))
    print('00000000111111111111111111111111111111111111111111111111111111111111111111111111111111')
if __name__ == "__main__":
    solve()