def read_matrix(name):
    op = int
    lines, cols = map(int, input(f'Enter size of{name}').split(' '))
    matrix = []
    print(f'Enter{name}')

    for _ in range(lines):
        line = input()

        if '.' in line:
            op = float

        line = list(map(op, line.split(' ')))
        matrix.append(line)

    return matrix


def print_matrix(matrix, fmt="d"):
    if fmt == "f":
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0.0:
                    matrix[i][j] = "0"
                    continue
                matrix[i][j] = str(matrix[i][j])

    for line in matrix:
        print(*line, sep=' ')


def add_matrix():
    m1 = read_matrix(' first matrix: ')
    m2 = read_matrix(' second matrix: ')

    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print('The operation cannot be performed.')
        return None

    ans = []

    for l in range(len(m1)):
        line = []
        for c in range(len(m1[0])):
            line.append(m1[l][c] + m2[l][c])
        ans.append(line)

    print('The result is:')
    print_matrix(ans)


def mult_const(m, n):
    for l in range(len(m)):
        for c in range(len(m[0])):
            if m[l][c] == 0:
                continue
            m[l][c] *= n
    return m


def multiply_matrix_const():
    m = read_matrix(' matrix: ')
    n = input('Enter constant: ')

    if '.' in n:
        n = float(n)
    else:
        n = int(n)

    prod = mult_const(m, n)

    print('The result is:')
    print_matrix(prod)


def multiply_matrix():
    m1 = read_matrix(' first matrix: ')
    m2 = read_matrix(' second matrix: ')

    if len(m1[0]) != len(m2):
        print('The operation cannot be performed.')
        return None

    ans = []

    for l in range(len(m1)):
        li = []
        for c in range(len(m2[0])):

            li.append(prod_vector(m1[l], [row[c] for row in m2]))
        ans.append(li)

    print('The result is:')
    print_matrix(ans)


def prod_vector(v1, v2):
    ans = 0
    for i in range(len(v1)):
        ans += v1[i] * v2[i]
    return float(ans)


def transpose(m, ls=0, le=0, lp=1, cs=0, ce=0, cp=1, diag=True):
    m2 = []
    for l in range(ls, le, lp):
        line = []
        for c in range(cs, ce, cp):
            if diag:
                line.append(m[c][l])
            else:
                line.append(m[l][c])
        m2.append(line)
    return m2


def transpose_menu():

    def main_diag(m):
        return transpose(m, le=len(m), ce=len(m[0]))

    def side_diag(m):
        return transpose(m, ls=len(m)-1, le=-1, lp=-1,
                         cs=len(m[0])-1, ce=-1, cp=-1)

    def vert_line(m):
        return transpose(m, le=len(m), cs=len(m[0])-1, ce=-1, cp=-1, diag=False)

    def horizon_line(m):
        return transpose(m, ls=len(m)-1, le=-1, lp=-1, ce=len(m[0]), diag=False)

    tranp_types = {'1': main_diag, '2': side_diag, '3': vert_line,
                   '4': horizon_line}
    print("\n1.Main diagonal\n"
          "2. Side diagonal\n"
          "3. Vertical line\n"
          "4. Horizontal line\n")

    opt = input('Your choice: ')
    matrix = read_matrix(' matrix: ')
    ans = tranp_types[opt](matrix)
    print("the result is:")
    print_matrix(ans)


def determinant(x):
    det = 0
    if len(x) == 1:
        return x[0][0]

    if len(x) == 2:
        return cofactor(x, 0, 0)

    for i in range(len(x)):
        det += (-1)**i*x[0][i]*cofactor(x[:], 0, i)
    return det


def determinant_menu():
    matrix = read_matrix(' matrix: ')
    det = determinant(matrix)
    print(f'The result is:\n {det}')

def cofactor(m, l, c):

    if len(m[0]) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    aux = [x[:] for x in m[:]]
    del aux[l]

    for l in aux:
        del l[c]

    if len(aux) == 2:
        return cofactor(aux, 0, 0)

    dt = 0
    for i in range(len(aux)):
        dt += (-1)**i*aux[0][i]*cofactor(aux[:], 0, i)

    return dt

def inverse_matrix():
    matrix = read_matrix(' matrix: ')
    det_m = determinant(matrix)

    if det_m == 0.0:
        print("This matrix doesn't have an inverse.")
        return None

    c_matrix = []

    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[0])):
            line.append((-1)**(i+j)*cofactor(matrix, i, j))
        c_matrix.append(line)

    c_matrix = transpose(c_matrix, le=len(c_matrix), ce=len(c_matrix[0]))
    inv_matrix = mult_const(c_matrix, 1 / det_m)
    print("The result is:\n")
    print_matrix(inv_matrix, fmt="f")


def menu():
    functions = {'1': add_matrix, '2': multiply_matrix_const,
                 '3': multiply_matrix, '4': transpose_menu,
                 '5': determinant_menu, '6': inverse_matrix,
                 '0': exit}
    print("1. Add matrices\n"
          "2. Multiply matrix by a constant\n"
          "3. Multiply matrices\n"
          "4. Transpose matrix\n"
          "5. Calculate a determinant\n"
          "6: Inverse matrix\n"
          "0. Exit")

    cmd = input('Your choice: ')
    functions[cmd]()
    print()


while True:
    menu()
