# %%
# q1
N = int(input())
stack = []
result = []
for _ in range(N):
    cmd = input()
    if 'push' in cmd:
        stack.append(int(cmd.replace('push ', '')))
    elif 'pop' == cmd:
        try:
            pop_val = stack.pop()
        except:
            pop_val = -1
        result.append(pop_val)
    elif 'size' == cmd:
        result.append(len(stack))
    elif 'empty' == cmd:
        result.append(1 if len(stack) == 0 else 0)
    elif 'top' == cmd:
        try:
            top_val = stack[-1]
        except:
            top_val = -1
        result.append(top_val)

for i in result:
    print(i)

# %%
# q2
K = int(input())
result = []
for _ in range(K):
    num = int(input())
    if num != 0:
        result.append(num)
    else:
        result.pop()

print(sum(result))

# %%
# q3
N = int(input())
vps = []
for _ in range(N):
    v = list(input())
    p = []
    for i in v:
        if i == '(':
            p.append(i)
        elif i == ')':
            try:
                p.pop()
            except:
                p = 'NO'
                break
    if len(p) == 0 and p != 'NO':
        vps.append('YES')
    else:
        vps.append('NO')

for s in vps:
    print(s)

# %%
# q4
result = []
while True:
    sentence = input()

    if sentence == '.':
        break
    
    elif '(' not in sentence and ')' not in sentence and '[' not in sentence and ']' not in sentence:
        result.append('yes')

    else:
        check = []
        for s in list(sentence):
            try:
                if s == '(' or s == '[':
                    check.append(s)
                elif s == ')':
                    if check[-1] == '(':
                        check.pop()
                    else:
                        check = 'no'
                        break
                elif s == ']':
                    if check[-1] == '[':
                        check.pop()
                    else:
                        check = 'no'
                        break
            except:
                check = 'no'
                break

        if len(check) == 0:
            result.append('yes')
        else:
            result.append('no')

for i in result:
    print(i)

# %%
# q5
import sys
n = int(input())
result = []
check = []
max_num = 0
b = ''
for _ in range(n):
    stack = []
    num = int(input())
    for i in range(max_num+1, num+1):
        stack.append(i)
        result.append('+')
    
    print(stack)
    if num > max_num:
        max_num = num

    result.append('-')
    check += stack
    a = check.pop()
    if a != num:
        b = 'NO'

if b != 'NO':
    for k in result:
        print(k)
else:
    print(b)