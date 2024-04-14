# 비슷한 단어

# 문제
# 영문 알파벳 대문자로 이루어진 두 단어가 다음의 두 가지 조건을 만족하면 같은 구성을 갖는다고 말한다.
# 1. 두 개의 단어가 같은 종류의 문자로 이루어져 있다.
# 2. 같은 문자는 같은 개수 만큼 있다.
# 예를 들어 "DOG"와 "GOD"은 둘 다 'D', 'G', 'O' 세 종류의 문자로 이루어져 있으며 양쪽 모두 'D', 'G', 'O' 가 하나씩 있으므로 이 둘은 같은 구성을 갖는다.
# 하지만 "GOD"과 "GOOD"의 경우 "GOD"에는 'O'가 하나, "GOOD"에는 'O'가 두 개 있으므로 이 둘은 다른 구성을 갖는다.
# 두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들 두 단어를 서로 비슷한 단어라고 한다.
# 입력으로 여러 개의 서로 다른 단어가 주어질 때, 첫 번째 단어와 비슷한 단어가 모두 몇 개인지 찾아 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 단어의 개수가 주어지고 둘째 줄부터는 한 줄에 하나씩 단어가 주어진다.
# 모든 단어는 영문 알파벳 대문자로 이루어져 있다. 단어의 개수는 100개 이하이며, 각 단어의 길이는 10 이하이다.

# 출력
# 입력으로 주어진 첫 번째 단어와 비슷한 단어가 몇 개인지 첫째 줄에 출력한다.

# TC
# 4
# DOG
# GOD
# GOOD
# DOLL

# Idea
# for문으로 같은 문자가 나오면 문자열에서 도려낸다
# 다른 문자가 나오면 diff 변수에 +1을 해준다
# diff가 1개면 res에 +1을 해준다
# 디테일한 튜닝을 못 해서 많이 틀렷다 핳ㅎ

# Code
import sys
sys.stdin = open("../input.txt", "r")

def solve():
    N = int(input())
    word = input()
    res = 0
    for _ in range(N-1):
        first_word = word
        new_word = input()
        diff = 0 # 얼마나 다른지 측정해주는 변수
        for i in range(len(new_word)):
            if not first_word: # first_word가 다 빠졌다?
                diff += len(new_word[i:]) # new_word의 남은 알파벳 수를 전부 때려넣어
                break
            if new_word[i] in first_word:
                idx = first_word.find(new_word[i])
                first_word = first_word[:idx] + first_word[idx + 1:] # 하나씩 삭제
            else:
                diff += 1

        else:
            if len(word) > len(new_word): # 역으로 word가 더 길다면 바꿀 만큼 빼고 남은 문자
                diff += len(first_word) - diff
        if diff <= 1:
            res += 1
    print(res)

if __name__ == "__main__":
    solve()