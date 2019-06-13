import argparse
import random
import multiprocessing
import time


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


def generate_matrix_in_list(l, m, n):
    '''
    Generates a matrix and stores it in l
    :param l: empty list to be filled with matrix values
    :param m: number of rows
    :param n: number of columns
    :return:
    '''
    random.seed()
    for i in range(m):
        temp = []
        for j in range(n):
            # matrix[i].append(random.randrange(sys.maxsize))
            temp.append(random.randrange(10))
        l.append(temp)

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


def multiply_row_and_column(args_dict):
    matrixA = args_dict[0]
    matrixB = args_dict[1]
    rowA = args_dict[2]
    columnB = args_dict[3]
    result_dict = args_dict[4]
    sum = 0
    for j in range(len(matrixA[rowA])):
        sum = sum + matrixA[rowA][j] * matrixB[j][columnB]
    result_dict[(rowA, columnB)] = sum
    return 0

def add_to_dict(d):
    d["asd"] = 123

def add_to_list(l):
    l.append("Asds")
    time.sleep(1)
    return 2

class ObjectIterator:
    def __init__(self, obj, count):
        self.obj = obj
        self.iterations = count
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.iterations:
            self.counter += 1
            return self.obj

        else:
            raise StopIteration

class MatrixMultiplicationIterator:
    '''
    iterates over rows and columns that have to be dot-multiplied
    '''
    def __init__(self, mA, mB, result_dict):
        self.mA = mA
        self.mB = mB
        self.result_dict = result_dict

        self.mA_row_count = len(mA)
        self.mB_column_count = len(mB[0])
        self.rowA = 0
        self.columnB = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.columnB >= self.mB_column_count:
            if self.rowA >= self.mA_row_count - 1:
                raise StopIteration

            self.columnB = 0
            self.rowA += 1
            return {0: self.mA, 1: self.mB, 2: self.rowA, 3: self.columnB, 4: self.result_dict}

        self.columnB += 1
        return {0: self.mA, 1: self.mB, 2: self.rowA, 3: self.columnB - 1, 4: self.result_dict}

def main():
    # args = get_args()
    #
    # m = args.m
    # n = args.n
    # k = args.k

    m = 2
    n = 3
    k = 2

    with multiprocessing.Manager() as manager:
        # shared objects init
        matrixA = manager.list()
        matrixB = manager.list()
        result_dict = manager.dict()

        # matrix generation
        generate_matrix_in_list(matrixA, m, n)
        generate_matrix_in_list(matrixB, n, k)

        matrix_iterator = MatrixMultiplicationIterator(matrixA, matrixB, result_dict)

        print_matrix(matrixA)
        print('=============')
        print_matrix(matrixB)
        print('=============')

        with multiprocessing.Pool(1) as pool:
            #multiply matrices
            for i in pool.imap_unordered(multiply_row_and_column, matrix_iterator):
                pass

        print(result_dict)



if __name__ == "__main__":
    main()
