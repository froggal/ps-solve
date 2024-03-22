a, b = map(int, input().split())
p = a * b
news = list(map(int, input().split()))

for i in news:
    print(i - p, end=' ')