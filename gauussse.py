import numpy as np


def det(matrix, n):
    s = 1
    for i in range(n):
        s *= matrix[i][i]
    return s


if __name__ == '__main__':

    is_file_input = input('Читаем из файла (y/n): ') == 'y'

    if is_file_input:
        filename = input('Введите имя файла: ')
        with open(filename) as file:
            n = int(file.readline())
            a = np.zeros((n, n + 1))

            for i in range(n):
                data = file.readline().split()
                for j in range(n + 1):
                    a[i][j] = float(data[j])
    else:
        n = int(input('Размерность? :'))
        a = np.zeros((n, n + 1))

        print('Enter Augmented Matrix Coefficients:')
        for i in range(n):
            for j in range(n + 1):
                a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

    a_copy = np.copy(a)
    x = np.zeros(n)

    # Applying Gauss Elimination
    for i in range(n):
        for j in range(i + 1, n):
            if a[i][i] != 0:
                ratio = a[j][i] / a[i][i]
                for k in range(n + 1):
                    a[j][k] = a[j][k] - ratio * a[i][k]
            else:
                print('not correct')
                exit(0)

    # Back Substitution
    if a[n - 1][n - 1] != 0:
        x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
    else:
        print('zero')
        exit(0)

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]
        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    # Displaying solution

    r = np.zeros(n)

    for i in range(n):
        for j in range(n):
            r[i] += a_copy[i][j] * x[j]

        r[i] = abs(a_copy[i][n] - r[i])

    print('Matrix')
    print(a)

    print('\nDET is: ')
    print('det = %0.2f' % det(a, n))

    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.10f' % (i, x[i]), end='\t')

    print('\nDelta is: ')
    for i in range(n):
        print('R%d = %0.20f' % (i, r[i]), end='\t')