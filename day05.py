#Assignment 8.10 dictionary comprehension으로 squares dictionary 생성. range(10)를 키로 하고, 각 키의 제곱을 값으로 한다.
# squares = {n: pow(n, 2) for n in range(10)}
# squares = {n: n**2 for n in range(10)}
squares = {n: n*n for n in range(10)}
print(squares)

# univ = 'inha university'
# counts_alphabet = {letter: univ.count(letter) for letter in univ} #dictionary comprehension
# print(counts_alphabet)

# univ = 'inha university'
# counts_alphabet = dict()
# for letter in univ:
#     counts_alphabet[letter] = univ.count(letter)
# print(counts_alphabet)