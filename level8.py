# %%
# q1
def change(n, b):
    data = {str(num):num for num in range(10)}
    data.update({f'{chr(A)}':A-55 for A in range(65, 91)})
    result = 0
    for i in range(len(n)):
        result += int(b) ** (len(n) - (i+1)) * data[n[i]]
    return result

N, B = input().split()

print(change(N, B))

# %%
# q2
def change(n, b):
    data = {num:str(num) for num in range(10)}
    data.update({A-55:f'{chr(A)}' for A in range(65, 91)})
    result = ''
    while n != 0:
        result += data[n % b]
        n = n // b

    return result[::-1]

N, B = map(int, input().split())

print(change(N, B))

# %%
# q3
T = int(input())
get_money = [int(input()) for _ in range(T)]
put_money = [25, 10, 5, 1]
result = [[0] * 4 for _ in range(T)]

for g in range(len(get_money)):
    for p in range(len(put_money)):
        result[g][p] = get_money[g] // put_money[p]
        get_money[g] %= put_money[p]

for ret in result:
    print(*ret)

# %%
# q4
N = int(input())
size = 2

for i in range(N):
    size += 2 ** i

result = 1 * (size ** 2)
    
print(result)

# %%
# q5
N = int(input())
sum = 1
floor = 0
result = 0

while True:
    if sum < N:
        floor += 1
        sum += 6 * floor
    else:
        result = floor + 1
        break
    
print(result)

# %%
# q6
X = int(input())
cnt = 0
floor = 1
a = 1
b = 1

while cnt < X:
    cnt += floor
    floor += 1
floor -= 1
cnt -= floor

a = 1
b = floor
cnt += 1
while a != floor:
    if cnt == X:
        break 
    a += 1
    b -= 1
    cnt += 1

print(f'{a}/{b}' if floor % 2 == 0 else f'{b}/{a}')

# %%
# q7
A, B, V = map(int, input().split())
print((V-B) // (A-B) if (V-B) % (A-B) == 0 else (V-B) // (A-B) + 1)

# %%
# q8
A, B = map(int, input().split())
print(A + B)