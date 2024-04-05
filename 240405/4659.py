# 비밀번호 발음하기

# 높은 품질을 가진 비밀번호의 조건은 다음과 같다.
# 1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

# 입력
# 입력은 여러개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 테스트할 패스워드가 주어진다.
# 마지막 테스트 케이스는 end이며, 패스워드는 한글자 이상 20글자 이하의 문자열이다. 또한 패스워드는 대문자를 포함하지 않는다.

# 출력
# 각 테스트 케이스를 '예제 출력'의 형태에 기반하여 품질을 평가하여라.
# <a> is acceptable.
# <tv> is not acceptable.

# Idea
# stack에 넣어가면서 판별하면 되겠네
# 반복문 내부에 cnt로 자음 혹은 모음이 3개가 되면 바로 터뜨려버리고

# Code
import sys
sys.stdin = open("../input.txt", "r")

# 이것은 모음입니까?
def is_vowel(a):
    vowel_arr = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowel_arr:
        if a == vowel:
            return True
    else:
        return False
def solve():
    while True:
        word = input()
        stk = []
        cnt = 1
        is_in_vowel = False
        res = 'is acceptable.'
        # 종료 조건
        if word == 'end':
            break
        for char in word:
            # 1. 모음이 하나라도 들어 있을 것
            if not is_in_vowel and is_vowel(char):
                is_in_vowel = True
            # 스택이 비어있거나, 같은 문자가 두개 연달아 오지 않거나, 3. e나 o라면 통과
            if not stk or char != stk[-1] or char == 'e' or char == 'o':
                # 자음 혹은 모음이 연달아 왔을 경우
                if stk and is_vowel(char) == is_vowel(stk[-1]):
                    # 2. 그게 세 번째일 경우
                    if cnt == 2:
                        res = 'is not acceptable.'
                        break
                    cnt += 1
                # 아닐 경우
                else:
                    cnt = 1
                stk.append(char)
            else:
                res = 'is not acceptable.'
                break
        else:
            # 1. 다 돌았는데 모음이 없을 경우
            if not is_in_vowel:
                res = 'is not acceptable.'

        print(f'<{word}>', res)

if __name__ == "__main__":
    solve()