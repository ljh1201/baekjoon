# %%
# q1
N = int(input())
n_list = [int(input()) for _ in range(N)]
n_list.sort()
for n in n_list:
    print(n)

# %%
# q2
n_list = [int(input()) for _ in range(5)]
n_list.sort()
print(sum(n_list)//len(n_list))
print(n_list[2])

# %%
# q3
N, k = map(int, input().split())
x_list = list(map(int, input().split()))
x_list.sort(reverse=True)
print(x_list[k-1])

# %%
# q4
import sys
N = int(input())
n_list = [int(sys.stdin.readline()) for _ in range(N)]
n_list.sort()
for n in n_list:
    print(n)

# %%
# q5
import sys
n = int(input())
n_list = [0] * 10001
for _ in range(n):
    n_list[int(sys.stdin.readline())] += 1

for i in range(len(n_list)):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i)

# %%
# q6
N = list(input())
M = ''.join(sorted(N, reverse=True))
print(M)

# %%
# q7
import sys
N = int(input())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
n_list.sort()
for n in n_list:
    print(*n)

# %%
# q8
import sys
N = int(input())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(len(n_list)):
    n_list[i] = n_list[i][::-1]

n_list.sort()

for j in range(len(n_list)):
    print(*n_list[j][::-1])

# %%
# q9
N = int(input())
word_list = sorted(set(input() for _ in range(N)))
len_list = [[] for _ in range(51)]

for word in word_list:
    len_list[len(word)].append(word)

for i in len_list:
    for j in i:
        print(j)


# %%
# q10
import sys
N = int(input())
member_list = [list(sys.stdin.readline().split()) for _ in range(N)]
age_list = [[] for _ in range(201)]
for data in member_list:
    age_list[int(data[0])].append(data[1])

for i in age_list:
    for j in i:
        print(age_list.index(i), j)

# %%
# q11
import sys
N = int(input())
x_list = list(map(int, input().split()))
x_rank = sorted(set(x_list))
x_dic = {x_rank[i]:i for i in range(len(x_rank))}

for x in x_list:
    print(x_dic[x], end = ' ')
