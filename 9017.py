# 크로스 컨트리

# 문제
# 한 팀은 여섯 명의 선수로 구성되며, 팀 점수는 상위 네 명의 주자의 점수를 합하여 계산한다.
# 점수는 자격을 갖춘 팀의 주자들에게만 주어지며, 결승점을 통과한 순서대로 점수를 받는다.
# 이 점수를 더하여 가장 낮은 점수를 얻는 팀이 우승을 하게 된다.
# 여섯 명의 주자가 참가하지 못한 팀은 점수 계산에서 제외된다.
# 동점의 경우에는 다섯 번째 주자가 가장 빨리 들어온 팀이 우승하게 된다.

# 입력
# 입력은 T 개의 테스트 케이스로 주어진다.
# 입력 파일의 첫 번째 줄에 테스트 케이스의 수를 나타내는 정수 T 가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (6 ≤ N ≤ 1,000)이 주어진다.
# 두 번째 줄부터는 두 줄에 하나의 테스트 케이스에 해당하는 데이터가 주어진다.
# 두 번째 줄에는 팀 번호를 나타내는 N 개의 정수 t1, t2, …, tN 이 공백을 사이에 두고 주어진다.
# 각 팀은 1 과 M(1 ≤ M ≤ 200)사이의 정수로 표현된다.

# 출력
# 하나의 테스트 케이스에 대한 우승팀의 번호를 한 줄에 출력한다.

# TC
# 2
# 15
# 1 2 3 3 1 3 2 4 1 1 3 1 3 3 1
# 18
# 1 2 3 1 2 3 1 2 3 3 3 3 2 2 2 1 1 1


# Idea
# 첫 번째 순회에서 팀 별 인원수 구하고 두 번째 순회에서 점수 재는 걸로 총 두 번 도는게 아이디어였으나
# 리스트.count() 메소드로 하면 손쉽게 걸러지겠는걸
# 팀 정보가 사전에 주어지지 않으니까 점수 계산은 딕셔너리 사용해서 하면 되겠다.
# 점수 계산 시 필요한 딕셔너리는 팀 계산, 주자 카운트, 5번째 주자 점수 기록
# 우승자 계산 시 필요한 변수는 우승팀이랑 우승팀의 5번째 주자의 점수면 되겟지

# Code
import sys
sys.stdin = open("input.txt", "r")

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        score = 0
        team_score = {}
        player_count = {}
        fifth_player = {}
        for i in range(N):
            # 팀원이 6명 이하면 점수를 반영하지 않는다.
            if arr.count(arr[i]) < 6:
                continue
            score += 1
            if arr[i] in team_score:
                # 상위 4명의 점수가 이미 합산됐나요?
                if player_count[arr[i]] >= 4:
                    # 5번 주자 점수 기록
                    if player_count[arr[i]] == 4:
                        fifth_player[arr[i]] = score
                else:
                    team_score[arr[i]] += score
                # 그들은 계속 달린다.
                player_count[arr[i]] += 1
            # dictionary initialize
            else:
                team_score[arr[i]] = score
                player_count[arr[i]] = 1

        # 우승을 가린다
        winner = None
        winners_fifth_score = 0
        for k, v in team_score.items():
            # 가장 성적이 좋은 팀의 5번째 주자들의 점수를 비교해서 우승자를 가려낸다.
            if v == min(team_score.values()) and (not winner or winners_fifth_score > fifth_player[k]):
                winner = k
                winners_fifth_score = fifth_player[k]

        # 결과 출력
        print(winner)

if __name__ == "__main__":
    solve()