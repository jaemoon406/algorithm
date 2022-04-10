import sys

T = input()
T = sys.stdin.readline().rstrip()
for i in range(int(T)):
    a,b = sys.stdin.readline().split()
    print(int(a)+int(b))


for _ in range(int(input())):
    print(sum(map(int,sys.stdin.readline().split())))