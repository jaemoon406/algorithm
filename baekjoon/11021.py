T = int(input())

for i in range(T):

    a,b = map(int,input().split())

    print(f'Case #{i+1}: {a} + {b} =', a+b)

# import sys
# input()
# for i,line in enumerate(sys.stdin.readlines()):
#     A,B=map(int,line.split())
#     print(f"Case #{i+1}: {A} + {B} = {A+B}")