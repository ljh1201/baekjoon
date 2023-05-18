# %%
# q1
import sys
T = int(input())
t_list = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
a = [t[0] for t in t_list]
b = [t[1] for t in t_list]

for i in range(T):
    c = max(a[i], b[i])
    d = min(a[i], b[i])
    for j in range(c, a[i] * b[i]+1, c):
        if j % d == 0:
            print(j)
            break

# %%
# q2
a, b = map(int, input().split())
c = max(a, b)
d = min(a, b)
for j in range(c, a * b+1, c):
    if j % d == 0:
        print(j)
        break

# %%
# q3
def primes(n1, n2):
    prime = max(n1, n2)
    n_max = min(n1, n2)
    while prime != 0:
        remainder = n_max % prime
        n_max = prime
        prime = remainder

    return n_max

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a = a1 * b2 + a2 * b1
b = b1 * b2

c = primes(a, b)

print(a//c, b//c)

# %%
# q4
import math
n = int(input())
n_list = sorted([int(input()) for _ in range(n)])
n_set = set()
for i in range(1, n):
    n_set.add(n_list[i] - n_list[i-1])

n_set = list(n_set)

prime = []
if len(n_set) > 1:
    for j in range(1, len(n_set)):
        prime.append(math.gcd(n_set[j-1], n_set[j]))
else:
    prime = n_set
print((n_list[-1] - n_list[0]) // min(prime) - (n - 1))

# %%
# q5
import math, sys
def next_primes(num):
    while True:
        if num < 2:
            num = 2
        prime = []
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                prime.append(i)
                prime.append(num//i)
                break
        if len(prime) == 0:
            return num
        num += 1

n = int(input())
n_list = [int(input()) for _ in range(n)]
for i in n_list:
    print(next_primes(i))

# %%
# q6
M, N = map(int, input().split())
n_list = list(range(max(2, M)), N+1)
for i in range(M, N+1):
    cnt = 0
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            cnt += 1
            break
    if cnt == 0:
        print(i)

# %%
# q7
def primes_length(num):
    array = [False, False] + [True] * (num*2-1)
    # while True:
    for i in range(2, num*2+1):
        if array[i]:
            j = 2
            while i * j <= num*2:
                array[i * j] = False
                j += 1
        
    return sum(array[num+1:num*2+1])
    
n_list = []
while 0 not in n_list:
    n_list.append(int(input()))

del n_list[-1]

for n in n_list:
    print(primes_length(n))

# %%
# q8
import sys
def primes_sum(num):
    primes = [False, False] + [True] * (num - 1)
    for i in range(2, int(num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * 2, num + 1, i):
                primes[j] = False
    
    cnt = set()
    for r in range(2, num // 2 + 1):
        if primes[r] and primes[num - r]:
            cnt.add(min(r, num - r))
    
    return len(cnt)

N = int(input())
n_list = [int(input()) for _ in range(N)]
for n in n_list:
    print(primes_sum(n))

# %%
# q9
N = int(input())