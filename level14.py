# %%
# q1
import sys
N = int(input())
n_list = set(map(int, sys.stdin.readline().split()))
M = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

for m in m_list:
    if m in n_list:
        print(1, end=' ')
    else:
        print(0, end=' ')


# %%
# q2
import sys
N, M = map(int, input().split())
n_in = set(sys.stdin.readline() for _ in range(N))
m_list = [sys.stdin.readline() in n_in for _ in range(M)]

print(sum(m_list))

# %%
# q3
import sys

N = int(input())
n_dict = {}
for _ in range(N):
    a, b = sys.stdin.readline().split()
    if b == 'enter':
        n_dict[a] = b
    else:
        if a in n_dict:
            del n_dict[a]
    
for j in sorted(n_dict, reverse=True):
    print(j)

# %%
# q4
import sys
N, M = map(int, input().split())
pokemon_list = {sys.stdin.readline().strip():i+1 for i in range(N)}
re_pokemon_list = dict(map(reversed, pokemon_list.items()))
question_list = [sys.stdin.readline().strip() for _ in range(M)]

for q in question_list:
    if q in pokemon_list:
        print(pokemon_list[q])
    else:
        print(re_pokemon_list[int(q)])
        


# %%
test = {'a':1, 'b':2}
print(test['a'])