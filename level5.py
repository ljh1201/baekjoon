# %%
# q1
S = input()
i = int(input())
print(S[i-1])

# %%
# q2
print(len(input()))

# %%
# q3
T = int(input())
words = [input() for _ in range(3)]
for word in words:
    print(word[0] + word[-1])

# %%
# q4
print(ord(input()))

# %%
# q5
N = int(input())
word = input()

print(sum(map(int, list(word))))

# %%
# q6
import string
S = input()
alphabet = list(string.ascii_lowercase)
result = [-1] * 26

for letter in S:
    result[alphabet.index(letter)] = S.index(letter)

print(*result)


# %%
# q7
T = int(input())
num_and_words = [list(input().split()) for _ in range(T)]

for i in num_and_words:
    for j in i[1]:
        print(j*int(i[0]), end='')
    print('')


# %%
# q8
print(len(input().split()))

# %%
# q9
A, B = map(list, input().split())
A_num = ''.join(A[::-1])
B_num = ''.join(B[::-1])

print(A_num if int(A_num) > int(B_num) else B_num)


# %%
# q10
alphabet = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
A_num = list(input())
result = 0

for ABC in alphabet:
    for alpha_to_num in A_num:
        if alpha_to_num in ABC:
            result += alphabet.index(ABC) + 3

print(result)


# %%
# q11
while True:
    try:
        word = input()
        print(word)
    except:
        break