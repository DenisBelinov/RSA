import argparse
import random
import sys


def get_args():
    parser = argparse.ArgumentParser('Matrix multiplicator')
    parser.add_argument('-m', type=int, help='number of rows of A', required=True)
    parser.add_argument('-n', type=int, help='number of columns of A', required=True)
    parser.add_argument('-k', type=int, help='number of columns of B', required=True)
    #TODO
    #parser.add_argument('--tasks, -t', type=int, help='number of threads', required=True)

    parser.add_argument('--input, -i', help='imput file') #TODO
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
            #matrix[i].append(random.randrange(sys.maxsize))
            matrix[i].append(random.randrange(10))

    return matrix


def generate_matrices(m, n, k):
    '''
    Generates two matrices with the given sizes
    :param m: number of rows of A
    :param n: number of column of A
    :param k: number of columns of B
    :return: tuple of two matrices
    '''

    return generate_matrix(m, n), generate_matrix(n, k)


def main():
    args = get_args()

    m = args.m
    n = args.n
    k = args.k

    matrixA, matrixB = generate_matrices(m, n, k)

    print(matrixA)
    print(matrixB)

if __name__ == "__main__":
    main()