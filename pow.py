'''def power(p, n):
    if n == 0:
        return 1
    else:
        return p * power(p, n - 1)#error

p = float(input("get me the amount:\t"))
n = int(input("agreed years:\t"))
print(power(p, n))'''


def launch(n):
    if n >= 1:
        print(n)
        launch(n - 1)

launch(5)

print("LAUNCH")

