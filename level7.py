# %%
# q1
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()

# %%
# q2
num_list = [(list(map(int, input().split()))) for _ in range(9)]

max_value = []
for nlist in num_list:
    max_value += nlist

max_value = max(max_value)

for nlist in num_list:
    if max_value in nlist:
        max_row = num_list.index(nlist)
        max_col = num_list[max_row].index(max_value)

print(max_value)
print(max_row + 1, max_col + 1)

# %%
# q3
words = [list(input()) for _ in range(5)]

result = [[] for _ in range(15)]

for word in words:
    for cnt in range(len(word)):
        result[cnt].append(word[cnt])

for i in result:
    for j in range(len(i)):
        print(i[j], end='')

# %%
# q4
background = [[0] * 100 for _ in range(100)]
N = int(input())
color_paper = [list(map(int, input().split())) for _ in range(N)]
result = 0

for size in color_paper:
    for col in range(size[1], size[1]+10):
        for row in range(size[0], size[0]+10):
            background[col][row] = 1
    
for b in background:
    result += sum(b)

print(result)


# %%
test = [[1] * 10] * 10
print(test[5][5])
