# %%
from collections import deque
import sys
N = int(input())
Q = deque()

cmd_list = {'push':lambda x:Q.append(x),
       'pop':lambda: Q.popleft() if Q else -1,
       'front': lambda: Q[0] if Q else -1,
        'back': lambda: Q[-1] if Q else -1,
        'size': lambda: len(Q),
        'empty': lambda: 1 if not Q else 0}

for _ in range(N):
    cmd = sys.stdin.readline().strip().split()
    if len(cmd) > 1:
        num = int(cmd[1])
        (cmd_list[cmd[0]])(num)
    elif cmd[0] in cmd_list:
        print(cmd_list[cmd[0]]())

# %%
# q2
from collections import deque
N = int(input())
card_list = deque([c for c in range(1, N+1)])

while len(card_list) != 1:
    card_list.popleft()
    card_list.append(card_list.popleft())

print(card_list[0])

# %%
# q3
from collections import deque
N, K = map(int, input().split())
man_list = deque([m for m in range(1, N+1)])
man_list.rotate(-K+1)

result = ['<']+[', ' for _ in range(N-1)]+['>']
idx = 1

while man_list:
    result.insert(idx, man_list[0])
    man_list.popleft()
    man_list.rotate(len(man_list)+1-K)
    idx+=2

for re in result:
    print(re, end='')

# %%
# q4
from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    document_list = deque(list(input().split()))
    max_value = max(document_list)
    document_list[M] = int(document_list[M])
    cnt = 0
    while True:
        if str(document_list[0]) == max_value:
            pop_value = document_list.popleft()
            cnt += 1
            if type(pop_value) == int:
                break
            max_value = max(map(str, document_list))
        else:
            document_list.rotate(-1)
    print(cnt)

# %%
test = ['1','2']
print(sum(map(int, test)))
print(test)
print('2' == 2)