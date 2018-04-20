for n in range(2, 10):
    for x in range(2, n):
        print("n == " + str(n) + " x == " + str(x))
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')


for i in range(10):
    print(i)
    if i == 5:
        break

print("done")