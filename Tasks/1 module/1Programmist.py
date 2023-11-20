n = int(input())
if n % 10 == 1 and n % 100 != 11:
    print(n, 'программист')
elif n % 10 == 0 or 5 <= n % 10 <= 9 or 11 <= n % 100 <= 19 :
    print(n, 'программистов')
elif 2 <= n % 10 <= 4:
    print(n, 'программиста')