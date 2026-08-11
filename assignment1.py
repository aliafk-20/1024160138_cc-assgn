for i in range(3):
    print("vrishank")

a = 1
b = 2
c = 4
d = a + b + c
print(a, "+", b, "+", c, "=", d)

q = input("Enter your name: ")
w = input("Enter your age: ")
e = input("Enter your city: ")
r = q + w + e
print(q, "+", w, "+", e, "=", r)

for i in range(1, 11):
    print(7, "*", i, "=", 7 * i)

for i in range(1, 11):
    print(9, "*", i, "=", 9 * i)

n = int(input("enter the number: "))
for i in range(1, 11):
    print(n, "*", i, "=", n * i)
print(sum(range(1, n + 1)))

z = int(input("2nd num: "))
x = int(input("3rd num: "))
print(max(n, z, x))

m = int(input("1st num: "))
s = 0
while m > 0:
    if m % 7 == 0 and m % 9 == 0:
        s += m
    m -= 1
print(s)

d = int(input("number: "))
def sum_of_prime(v: int) -> int:
    sp: int = 0
    while v > 0:
        f = 0
        for i in range(2, v // 2 + 1):
            if v % i == 0:
                f = 1
                break
        if f == 0 and v > 1:
            sp += v
        v -= 1
    return sp

print(sum_of_prime(d))

b = int(input("number: "))
def sum_of_odds(n: int) -> int:
    result: int = 0
    for i in range(n + 1):
        if i % 2 == 0:
            continue
        result += i
    return result

print(sum_of_odds(b))

