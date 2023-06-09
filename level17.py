# %%
# q1
N = int(input())
n_list = sorted(list(map(int, input().split())))
print(min(n_list) * max(n_list))

# %%
# q2
N = int(input())
n_list = [input() for _ in range(N)]
check_set = set()
result = 0

for i in range(N-1, -1, -1):
    if n_list[i] != 'ENTER':
        check_set.add(n_list[i])
    else:
        result += len(check_set)
        check_set = set()

print(result)

# %%
# q3
N = int(input())
check_list = set(['ChongChong'])
n_list = [list(input().split()) for _ in range(N)]

for i in range(N):
    if n_list[i][0] in check_list:
        check_list.add(n_list[i][1])
    elif n_list[i][1] in check_list:
        check_list.add(n_list[i][0])

print(len(check_list))

# %%
# q4
import sys
from collections import Counter
n = int(input())
n_list = [int(sys.stdin.readline()) for _ in range(n)]
cnt = 1
mode = set()

for num, count in Counter(n_list).items():
    if count >= cnt:
        if count > cnt:
            mode = set()
        cnt = count
        mode.add(num)

if len(mode) == 1:
    mode = list(mode)[0]
else:
    mode = sorted(mode)[1]

print(round(sum(n_list) / n))
print(sorted(n_list)[n//2])
print(mode)
print(max(n_list) - min(n_list))

# %%
# q5
import sys
n, m = map(int, input().split())
words = {}
for _ in range(n):
    w = sys.stdin.readline().rstrip()
    if len(w) >= m:
        if w in words.keys():
            words[w] += 1
        else:
            words[w] = 1

words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word in words:
    print(word[0])
