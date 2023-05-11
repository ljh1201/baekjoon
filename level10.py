# %%
# q1
A = int(input())
B = int(input())
print(A * B)

# %%
# q2
x, y, w, h = map(int, input().split())
dis_list = [x, w-x, y, h-y]
print(min(dis_list))

# %%
# q3
xy = [list(map(int, input().split())) for _ in range(3)]
x = [i[0] for i in xy]
y = [i[1] for i in xy]

x_len = max(x) - min(x)
y_len = max(y) - min(y)

xy2 = [[min(x), min(y)], [min(x), min(y) + y_len], [min(x) + x_len, min(y)], [min(x) + x_len, min(y) + y_len]]

for result in xy2:
    if result not in xy:
        print(*result)

# %%
# q4
n = int(input())
print(4 * n)

# %%
# q5
N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
x = [i[0] for i in N_list]
y = [i[1] for i in N_list]

print((max(x) - min(x)) * (max(y) - min(y)))
    
# %%
# q6
angle_list = [int(input()) for _ in range(3)]
if sum(angle_list) != 180:
    print('Error')
elif len(set(angle_list)) == 1:
    print('Equilateral')
elif len(set(angle_list)) == 2:
    print('Isosceles')
elif len(set(angle_list)) == 3:
    print('Scalene')

# %%
# q7
result = []
while True:
    angle = list(map(int, input().split()))
    angle.sort()
    if set(angle) == {0}:
        break
    result.append(angle)

for r in result:
    if r[-1] - sum(r[:-1]) >= 0:
        print('Invalid')
    elif len(set(r)) == 1:
        print('Equilateral')
    elif len(set(r)) == 2:
        print('Isosceles')
    elif len(set(r)) == 3:
        print('Scalene')

# %%
# q8
abc = list(map(int, input().split()))
abc.sort()
if abc[-1] < sum(abc[:-1]):
    print(sum(abc))
else:
    abc[-1] = sum(abc[:-1]) - 1
    print(sum(abc))
