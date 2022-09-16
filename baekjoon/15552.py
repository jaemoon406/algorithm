# # 2438
# a = int(input())
# for i in range(1,a+1):
#     print('*'*i)

# # 2439
# N = int(input())

# for i in range(1,N+1):
#     a = '*'
#     b = ' '*(N-i)
#     print(f'{b}{a*i}')


# # 2480
# """
# 1~6 눈의 주사위 3개
# 같은 눈 2개 10000 + 눈* 1000
# 다르면 가장 큰눈* 100
# """
# a,b,c = map(int,input().split())

# if a == b or a == c:
#     print(1000 + a * 100)
# elif b == c: 
#     print(1000 + b * 100)
# elif c == a:
#     print(1000 + a * 100)
# elif a == b == c:
#     print(10000 + a * 1000)
# else:
#     print(max(a,b,c) * 100)


# # 2525
# """
# 또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 끝나는 시각을 알려 주는 디지털 시계가 있다. 
# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때,
# 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다. 
# """
# a, b = map(int,input().split())
# c = int(input())

# total_min = a * 60 + b + c
# h = total_min // 60
# m = total_min % 60

# if total_min > 1439:
#     print(a + ((b + c) // 60) - 24 ,m)
# else:
#     print(h,m)

# # 2739
# # n = int(input())
# n = 2

# for i in range(1,10):
#     print(f'{n} * {i} = {n*i}')


# # 2741
# import sys

# n = int(sys.stdin.readline())+1
# for i in range(n-1):
#     n=n-1
#     print(n)


# # 2742
# import sys
# n = int(sys.stdin.readline())
# a = n
# for i in range(n):
#     print(a+1)


# # 2884
# """이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다.
# 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.
# 현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.
# 입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다."""

# H,M = map(int,input().split())

# if M > 44:
#     print(H,45 - M)
# elif M < 45 and H > 0:
#     print(H-1,M + 15)
# else:
#     print(23,M+15)


# # 8393
# n = int(input())

# a = [i+1 for i in range(n)]
# b = sum(a)
# print(b)
# # print(a*(a+1)//2)


# # 10871
# '''
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# '''
# # range : N, maximum : X

# N,X = map(int,input().split())
# A =list(''.join(input()).split())
# B = [A[i] for i in range(len(A)) if int(A[i]) < X]
# print(' '.join(B))


# # ================================================

# N,X = map(int,input().split())
# score = [x for x in input().split() if int(x) < X]
# print(' '.join(score))


# # 10950
# T = int(input())
# for i in range(T):
#     a,b = map(int,input().split())
#     print(a+b)


# # 11021
# T = int(input())

# for i in range(T):
#     a,b = map(int,input().split())
#     print(f'Case #{i+1}: {a} + {b} =', a+b)

# # import sys
# # input()
# # for i,line in enumerate(sys.stdin.readlines()):
# #     A,B=map(int,line.split())
# #     print(f"Case #{i+1}: {A} + {B} = {A+B}")


# # 10952
# import sys

# a = 1
# while a == 1:
#     A,B = map(int,sys.stdin.readline().split())
#     if A and B != 0:
#         print(A+B)
#     else:
#         a = 0


# # 15552
# import sys

# T = input()
# T = sys.stdin.readline().rstrip()
# for i in range(int(T)):
#     a,b = sys.stdin.readline().split()
#     print(int(a)+int(b))

# # for _ in range(int(input())):
# #     print(sum(map(int,sys.stdin.readline().split())))


# # 10951 
# import sys

# for line in sys.stdin:
#     print(sum(map(int,(line.split()))))


# # 1110

# # 틀림 재 풀이 필요함

# # 8958

# """
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 
# 문자열은 O와 X만으로 이루어져 있다.
# """

# a = input()
n = input()  # 테스트 횟수
score = 0
for _ in range(n):
    score_list = list(input())
    for i in range(len(score_list)):
        if score_list[i] == 'O':
            score + 1
print(score)

"""
4344
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
"""
from cgitb import reset
from codecs import ascii_decode
import sys

n = int(sys.stdin.readline())
for i in range(n):
    score = list(map(int,sys.stdin.readline().split()))[1:]
    sum_score = sum(score)/len(score)
    l = sum(1 for score in score if score > sum_score)
    print(f"{(l/len(score))*100:.3f}%")

"""
15596
정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

a: 합을 구해야하는 정수 n개가 저장되어 있는 배열
return: a에 포함되어 있는 정수 n개의 합
"""
def solve(a):
    ans = sum(a)
    return ans

