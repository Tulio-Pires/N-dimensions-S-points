# Dimensao, ponto
X1 = float(input('x1: '))
Y1 = float(input('y1: '))
Z1 = float(input('z1: '))
X2 = float(input('x2: '))
Y2 = float(input('y2: '))
Z2 = float(input('z2: '))
X3 = float(input('x3: '))
Y3 = float(input('y3: '))
Z3 = float(input('z3: '))

x12 = (X1 - X2) ** 2
y12 = (Y1 - Y2) ** 2
z12 = (Z1 - Z2) ** 2
x13 = (X1 - X3) ** 2
y13 = (Y1 - Y3) ** 2
z13 = (Z1 - Z3) ** 2
x23 = (X2 - X3) ** 2
y23 = (Y2 - Y3) ** 2
z23 = (Z2 - Z3) ** 2

result12 = (x12 + y12 + z12) ** (1 / 2)
result13 = (x13 + y13 + z13) ** (1 / 2)  # exists N points, we can calculate the number of results the following way:
result23 = (x23 + y23 + z23) ** (1 / 2)  # Nr = ((N-1)*n)/2 Exemple: 6 points = (6-1)*4/2 = 20/2 = 10 results

print(f'Dinstance between points 1 and 2: {result12}')
print(f'Dinstance between points 1 and 3: {result13}')
print(f'Dinstance between points 2 and 3: {result23}')

# for an in range(0, quantidade_de_pontos):
#    Np += an  # Np = (N-1) + N(p-1). # Example: 5 pontos = 5-1 + 5-2 + 5-3 + 5-4 + 5-5 = 10 results
#
# For 3 dimensions and 3 it goes like this:
#
# [0   1   2   3   4   5   6   7   8 ]
# [x1, y1, z1, x2, y2, z2, x3, y3, z3]
#  j1  j2  j3 j1d j2d j3d  ?   ?   ?      == x12 y12 z12  == (j1 - j1d)  (j2 - j2d)  (j3 - j3d)
#  ?  ?  ? j1d  j2d  j3d  2j1d 2j2d 2j3d  == x23 y23 z23  == (j1d - 2j1d)  (j2d - 2j2d)  (j3d - 2j3d)
#  j1  j2  j3  ?   ?   ?  2j1d 2j2d 2j3d  == x13 y13 z13  == (j1 - 2j1d)  (j2 - 2j2d)  (j3 - 2j3d)
#
# For 2 dimensions and 5 points is goes like this:


# 11  12    21   22   31   32    41    42    51   52
# j1  j2   jd1 jd2  -      -     -     -     -    -      =   I I I I
# j1  j2   -   -    j2d1   j2d2  -     -     -    -      =   I I     I I
# j1  j2   -   -    -       -    j3d1 j2d2   -    -      =   I I         I I
# j1  j2   -   -    -       -     -     -   j4d1 j4d2    =   I I             I I
#
#  -   -   jd1 jd2  j2d1   j2d2   -     -    -    -      =       I I I I
#  -   -   jd1 jd2  -       -     j3d1 j3d2  -    -      =       I I     I I
#  -   -   jd1 jd2  -       -     -     -   j4d1 j4d2    =       I I         I I
#
#  -   -    -   -   j2d1   j2d2   j3d1 j3d2  -    -      =           I I I I
#  -   -    -   -   j2d1   j2d2   -     -   j4d1 j4d2    =           I I     I I
#
#  -   -    -   -   -       -     j3d1 j3d2 j4d1 j4d2    =               I I I I
