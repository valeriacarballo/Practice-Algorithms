# matrix A = 3x3
A = [
        [0, 1, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

# tic tac toe
t3 = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

t3[0][0] = 'O'
t3[2][0] = 'x'
t3[2][2] = 'O'
t3[1][1] = 'x'
t3[0][2] = 'O'
t3[1][2] = 'x'
t3[0][1] = 'O'

for row in range(len(t3)):
    for column in range(len(t3[row])):
        print(t3[row][column])

#or 

for row in t3:
    for col in row:
        print(col)