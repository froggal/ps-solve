n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n+1):
    if a[i] < x:
        print(a[i], end=' ')