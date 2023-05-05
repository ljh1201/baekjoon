# %%
# q1
plant = '''         ,r'"7
r`-_   ,'  ,/
 \\. ". L_r'
   `~\\/
      |
      |'''
print(plant)

# %%
# q2
donghyuk = list(map(int, input().split()))
answer = [1, 1, 2, 2, 2, 8]

for i in range(len(answer)):
    print(answer[i] - donghyuk[i], end = ' ')

# %%
# q3
N = int(input())

for i in range(N, 1, -1):
    print(' '*(i-1), end='')
    print('*'*(N*2-i*2+1))

for j in range(1, N+1):
    print(' '*(j-1), end='')
    print('*'*(N*2-j*2+1))

# %%
# q4
N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]
change = [list(map(int, input().split())) for _ in range(M)]

for chg in change:
    basket[chg[0]-1:chg[1]] = basket[chg[2]-1:chg[1]] + basket[chg[0]-1:chg[2]-1]

print(*basket)

# %%
# q5
word = list(input())
reversed_word = list(reversed(word))

if word == reversed_word:
    print('1')
else:
    print('0')

# %%
# q6
import string
word = input()
word = list(word.upper())

alphabet = list(string.ascii_uppercase)
check = [0] * 26
for w in word:
    for abc in range(len(alphabet)):
        if w == alphabet[abc]:
            check[abc] += 1

print(alphabet[check.index(max(check))] if check.count(max(check)) == 1 else '?')

# %%
# q7
C = int(input())
N = [list(map(int, input().split())) for _ in range(C)]
over_mean = 0

for stu_score in N:
    mean = sum(stu_score[1:]) / stu_score[0]
    for score in stu_score[1:]:
        if score > mean:
            over_mean += 1
    print('{:.3f}%'.format(over_mean / stu_score[0] * 100))
    over_mean = 0

# %%
# q8
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
cnt = 0
loop = 0

while loop < len(word):
    found = False
    for cro in croatia:
        if word[loop:].startswith(cro):
            cnt += 1
            loop += len(cro) 
            found = True
    if not found:
        cnt += 1
        loop += 1
            
print(cnt)

# %%
# q9
N = int(input())
word = [input() for _ in range(N)]
abc = []
count = 0

for w in word:
    for i in w:
        if i not in abc or abc[-1] == i:
            abc.append(i)
            continue
        else:
            break
    if len(abc) == len(w):
        count += 1
    abc = []
print(count)

# %%
# q10
score = [list(input().split()) for _ in range(20)]
result = 0
grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 
         'D+':1.5, 'D0':1.0, 'F':0.0, 'P':0.0}
grades = 0

for s in score:
    if s[2] != 'P':
        result += float(s[1]) * grade[s[2]]
        grades += float(s[1])

print('{:.6f}'.format((result / grades) if grades > 0 else grades))

