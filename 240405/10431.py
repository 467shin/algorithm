# 줄세우기

# 우선 아무나 한 명을 뽑아 줄의 맨 앞에 세운다. 그리고 그 다음부터는 학생이 한 명씩 줄의 맨 뒤에 서면서 다음 과정을 거친다.
# 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
# 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다. 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.

# 입력
# 첫 줄에 테스트 케이스의 수 P (1 ≤ P ≤ 1000) 가 주어진다.
# 각 테스트 케이스는 테스트 케이스 번호 T와 20개의 양의 정수가 공백으로 구분되어 주어진다.
# 20개의 정수는 줄서기를 할 아이들의 키를 줄서기 차례의 순서대로 밀리미터 단위로 나타낸 것이다.
# 모든 테스트 케이스는 독립적이다.

# 출력
# 각각의 테스트 케이스에 대해 테스트 케이스의 번호와 학생들이 뒤로 물러난 걸음 수의 총합을 공백으로 구분하여 출력한다.

# TC
# 4
# 1 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919
# 2 919 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900
# 3 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919 900
# 4 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900 919

# Idea
# 버블 정렬 비스무리한 것

# Code
import sys
sys.stdin = open("../input.txt", "r")
def solve():
    T, *arr = map(int, input().split())
    # res의 초깃값 설정
    res = [arr.pop(0)]
    # 학생이 뒤로 물러난 횟수
    cnt = 0
    # 20 - 1
    for _ in range(19):
        # 다음 학생
        student = arr.pop(0)
        # res의 뒤부터 한 칸씩 비교 전진
        for i in range(len(res), 0, -1):
            # 학생의 키가 현재 보고 있는 res의 i-1 인덱스에 서 있는 학생보다 작으면
            if student < res[i-1]:
                # 카운트 증가
                cnt += 1
            # 클 경우
            else:
                res.insert(i, student)
                break
        # 어라? 정신 차려보니 맨 앞이야
        else:
            res.insert(0, student)

    print(T, cnt)
    return

if __name__ == "__main__":
    P = int(input())
    for _ in range(P):
        solve()