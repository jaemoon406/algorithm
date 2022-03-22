"""
1~6 눈의 주사위 3개
같은 눈 2개 10000 + 눈* 1000
다르면 가장 큰눈* 100
"""
a,b,c = map(int,input().split())

if a == b or a == c:
    print(1000 + a * 100)
elif b == c: 
    print(1000 + b * 100)
elif c == a:
    print(1000 + a * 100)
elif a == b == c:
    print(10000 + a * 1000)
else:
    print(max(a,b,c) * 100)
