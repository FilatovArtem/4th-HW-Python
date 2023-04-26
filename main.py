import sys
import numpy as np
import string

file_name = sys.argv[1]
file = open(file_name, "r")
str = file.read()

str = str.split(' ')

for i in str:
    if (i == ''):
        sys.exit("Incorrect input")
    for el in i:
        if(el < '0' or el > '9'):
            sys.exit("Incorrect input")

matrix_size = int(str[0])

if(len(str) != matrix_size**2 + 1):
    sys.exit("Incorrect matrix")

matrix_elems = [int(str[i]) for i in range(1, len(str))]
array_of_arrays = [[matrix_elems[i] for i in range(j * matrix_size, matrix_size * (j + 1))] for j in range(matrix_size)]
matrix_A = np.array(array_of_arrays)
matrix_A_rang = np.linalg.matrix_rank(matrix_A)

print(matrix_A_rang)
print(matrix_A)
print(matrix_size)
print(matrix_elems)

file.close()