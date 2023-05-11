# %%
# q1
print('''1
0''')

# %%
# q2
n = int(input())
print(n)
print('1')

# %%
# q3
n = int(input())
x = 2
print(n ** x)
print(x)

# %%
# q4
n = int(input())
n_sum = 0
for i in range(1, n):
    n_sum += i

print(n_sum)
print('2')

# %%
# q5
n = int(input())
x = 3
print(n ** x)
print(x)

# %%
# q6
n = int(input())
n_sum = 0
for i in range(1, n-1):
    n_sum += i * (n - (1 + i))

print(n_sum)
print('3')

# %%
# q7
a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

f = a1 * n + a0
g = c * n
print('1' if f <= g and a1 <= c else '0')