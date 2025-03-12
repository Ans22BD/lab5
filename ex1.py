def ali(n):
    for i in range(n + 1):
        yield i ** 2

N = 77
for num in ali(N):
    print(num, end=" ")