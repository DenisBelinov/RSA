import argparse
import random
import multiprocessing


def get_args():
    parser = argparse.ArgumentParser('Matrix multiplicator')
    parser.add_argument('-m', type=int, help='number of rows of A', required=True)
    parser.add_argument('-n', type=int, help='number of columns of A', required=True)
    parser.add_argument('-k', type=int, help='number of columns of B', required=True)
    # TODO
    # parser.add_argument('--tasks, -t', type=int, help='number of threads', required=True)

    parser.add_argument('--input, -i', help='imput file')  # TODO
    parser.add_argument('--output, -o', help='output file')  # TODO
    return parser.parse_args()


def generate_matrix(m, n):
    '''
    Generates a matrix
    :param m: number of rows
    :param n: number of columns
    :return:
    '''
    random.seed()
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            # matrix[i].append(random.randrange(sys.maxsize))
            matrix[i].append(random.randrange(10))

    return matrix


def generate_empty_matrix(m, n):
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append(None)
    return matrix


def generate_empty_matrix_in_list(l, m, n):
    for i in range(m):
        temp=[]
        for j in range(n):
            temp.append(1)
        l.append(temp)
    return l


def generate_matrices(m, n, k):
    '''
    Generates two matrices with the given sizes
    :param m: number of rows of A
    :param n: number of column of A
    :param k: number of columns of B
    :return: tuple of two matrices
    '''

    return generate_matrix(m, n), generate_matrix(n, k)


def print_matrix(a):
    '''
    Prints a matrix the appropriate way(not like a list)
    :param a: matrix
    '''

    for i in a:
        print(i)


def multiply_matrices(a, b):
    c = generate_empty_matrix(len(a), len(b[0]))

    for n in range(len(a)):
        for p in range(len(b[0])):
            sum = 0
            for j in range(len(a[n])):
                sum = sum + a[n][j] * b[j][p]
            c[n][p] = sum
    return c


def dot_product(vector1, vector2):
    sum = 0
    if len(vector1) != len(vector2):
        raise Exception
    for i in (len(vector1)):
        sum = sum + vector1[i] * vector2[i]


def main():
    args = get_args()

    m = args.m
    n = args.n
    k = args.k

    matrixA, matrixB = generate_matrices(m, n, k)
    matrixC = multiply_matrices(matrixA, matrixB)

    print_matrix(matrixA)
    print('=============')
    print_matrix(matrixB)
    print('=============')
    print_matrix(matrixC)

    with multiprocessing.Manager() as manager:
        test = manager.list([])
        print(test)
        generate_empty_matrix_in_list(test, 2, 3)
        print(test)

if __name__ == "__main__":
    main()
