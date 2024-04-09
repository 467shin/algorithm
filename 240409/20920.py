# 영단어 암기는 괴로워

# 문제
# 화은이는 이번 영어 시험에서 틀린 문제를 바탕으로 영어 단어 암기를 하려고 한다.
# 그 과정에서 효율적으로 영어 단어를 외우기 위해 영어 단어장을 만들려 하고 있다.
# 만들고자 하는 단어장의 단어 순서는 다음과 같은 우선순위를 차례로 적용하여 만들어진다.
# 1. 자주 나오는 단어일수록 앞에 배치한다.
# 2. 해당 단어의 길이가 길수록 앞에 배치한다.
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
# M보다 짧은 길이의 단어의 경우 읽는 것만으로도 외울 수 있기 때문에 길이가 M이상인 단어들만 외운다고 한다.

# 입력
# 첫째 줄에는 영어 지문에 나오는 단어의 개수 N과 외울 단어의 길이 기준이 되는 M이 공백으로 구분되어 주어진다. (1 <= N <= 100,000, 1 <= M <= 10)
# 둘째 줄부터 N + 1번째 줄까지 외울 단어를 입력받는다.
# 이때의 입력은 알파벳 소문자로만 주어지며 단어의 길이는 10을 넘지 않는다.
# 단어장에 단어가 반드시 1개 이상 존재하는 입력만 주어진다.

# 출력
# 단어장에 들어 있는 단어를 단어장의 앞에 위치한 단어부터 한 줄에 한 단어씩 순서대로 출력한다.

# TC
# 12 5
# appearance
# append
# attendance
# swim
# swift
# swift
# swift
# mouse
# wallet
# mouse
# ice
# age

# Idea
# 딕셔너리로 정리해서 밸류별 정렬 하면 되지 않을까...?
# 그 날 떠올렸다. 딕셔너리 정리는 내 마음대로 되지 않는다는 사실을
# 개같은 람다식
# 에 대해 더 자세히 알 수 있는 기회가 된 것 같아 좋았다.

# Code
import sys
sys.stdin = open("../input.txt", "r")
# 문제의 권장 사항
input = sys.stdin.readline


def solve():
    N, M = map(int, input().rstrip().split())
    voca = {}
    for i in range(N):
        word = input().rstrip()
        if len(word) < M:
            continue
        if word in voca:
            voca[word] += 1
        else:
            voca[word] = 1

    voca = sorted(voca.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    # x에는 voca 내부의 key, value가 튜플 형태로 들어가게 된다.
    # -x[1]: x의 1번째 요소 즉, value를 내림차순으로 정렬해준다. 오름차가 default값이기에 -부호를 붙여추면 reverse=True와 같다
    # -len(x[0]): x의 0번째 요소 즉, key의 길이가 긴 순으로 정렬해준다. 짧은 순이 default이기 때문에 앞에 -부호를 붙여준다.
    # 마지막으로 key의 알파벳 순으로 정렬해준다. default가 알파벳 순이기 때문에 내비둬도 된다.

    for (word, count) in voca:
        print(word)


if __name__ == "__main__":
    solve()
