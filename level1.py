# %%
# q1
print('Hello World!')

# %%
# q2
A, B = map(int, input().split(' '))
print(A + B)

# %%
# q3
A, B = map(int, input().split(' '))
print(A - B)

# %%
# q4
A, B = map(int, input().split(' '))
print(A * B)

# %%
# q5
A, B = map(int, input().split(' '))
print(A / B)

# %%
# q6
A, B = map(int, input().split(' '))
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)

# %%
# q7
ID = input()
print(ID+'??!')

# %%
# q8
B_year = int(input())
print(B_year - 543)

# %%
# q9
A, B, C = map(int, input().split(' '))
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

# %%
# q10
num1 = int(input())
num2 = list(map(int, input()))
result = 0

for i in range(len(num2)):
    print(num1 * num2[-i-1])
    result += int(str(num1 * num2[-i-1]) + '0'*i)

print(result)

# %%
# q11
A, B, C = map(int, input().split(' '))
print(A + B + C)

# %%
# q12
cat = '''\    /\\
 )  ( ')
(  /  )
 \(__)|'''

print(cat)

# %%
# q13
dog = '''|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|'''

print(dog)