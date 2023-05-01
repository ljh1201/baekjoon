# %%
# q1
A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

# %%
# q2
score = int(input())
if 90 <= score <= 100:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('F')

# %%
# q3
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('1')
else:
    print('0')

# %%
# q4
x = int(input())
y = int(input())
if x > 0:
    print('1' if y > 0 else '4')
else:
    print('2' if y > 0 else '3')

# %%
# q5
hour, minute = map(int, input().split())
if minute >= 45:
    minute = minute - 45
else:
    hour = hour - 1 if hour > 0 else 23
    minute = 60 - (45 - minute)

print(f'{hour} {minute}')

# %%
# q6
hour, minute = map(int, input().split())
waiting = int(input())

w_hour = hour + (waiting // 60)
w_minute = minute + (waiting % 60)
if w_minute >= 60:
    w_hour += w_minute // 60
    w_minute = w_minute % 60

if w_hour >= 24:
    w_hour %= 24

print(f'{w_hour} {w_minute}')

# %%
# q7
dice = list(map(int, input().split()))
point = 0
same_num = max(dice)

for j in range(len(dice)):
    if dice[j] == dice[j-1]:
        point += 1
        same_num = dice[j]

if point == 3:
    print(10000 + same_num * 1000)
elif point == 1:
    print(1000 + same_num * 100)
else:
    print(same_num * 100)
