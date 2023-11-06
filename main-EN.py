def func():
    
    # Asks how many dimensions and points
    dimensions = int(input('How many dimensions? '))
    quantity_of_points = int(input('How many points? '))

    # Makes those things, global
    terms = []
    List = []
    almost_there = []
    resulllt = []

    # Asks the coordinates
    for point in range(0, quantity_of_points):
        for dimension in range(0, dimensions):
            termm = float(input(f'Diga qual o {point + 1} termo, da {dimension + 1} dimensão: '))
            terms.append(termm)

    # It computes x1 - x2 for n dimensions with s pontos
    for permutation2 in range(0, quantity_of_points):
        for permutation1 in range(1, quantity_of_points - permutation2):
            for j in range(0, dimensions):
                # In j, it's made an permutation between 2 points, after that, in permutation1 i make her considering
                # the permutation that occurs in the x axis (look at the end of the code), and last but not least
                # the one that happens in the y axis, take in mind taht in permutation1 it's taken out its part of it
                # by the number of permutation 2, it's possible to see it, in the graph i made
                List.append((terms[j + (permutation2 * dimensions)] - terms[
                    j + (dimensions * (permutation1 + permutation2))]) ** 2)
                
    # Computes the number of results using the graph theory formula
    np = int((quantity_of_points * (quantity_of_points - 1)) / 2)

    # Turns the list into a list of lists to use sum() in each one of them
    for s in range(0, np):
        almost_there.append(List[s * dimensions: s * dimensions + dimensions])
        
    # Here we sum and compute the square root and put the final result in the list resulllt
    for final_result in range(0, np):  # i make it np times, cause there is np results
        resulllt.append(sum(almost_there[final_result]) ** (1 / 2))
        
    print('=' * 70)
    for RESULT in range(0, np):
        print(f'The distance between {RESULT + 1} pair of points is {resulllt[RESULT]}')
    print('=' * 70)


if __name__ == "__main__":
    func()



# For 2 dimensions with 5 points, it goes like this:
#
# 11   12   21   22   31   32    41    42    51   52
#                                                          x axis-----------------
# j1  j2   jd1 jd2  -      -     -     -     -    -      = |  I I I I
# j1  j2   -   -    j2d1   j2d2  -     -     -    -      = |  I I     I I
# j1  j2   -   -    -       -    j3d1 j2d2   -    -      = y  I I         I I
# j1  j2   -   -    -       -     -     -   j4d1 j4d2    =    I I             I I
#                                                          a
#  -   -   jd1 jd2  j2d1   j2d2   -     -    -    -      = x      I I I I
#  -   -   jd1 jd2  -       -     j3d1 j3d2  -    -      = i      I I     I I
#  -   -   jd1 jd2  -       -     -     -   j4d1 j4d2    = s      I I         I I
#                                                          |
#  -   -    -   -   j2d1   j2d2   j3d1 j3d2  -    -      = |          I I I I
#  -   -    -   -   j2d1   j2d2   -     -   j4d1 j4d2    = |          I I     I I
#                                                          |
#  -   -    -   -   -       -     j3d1 j3d2 j4d1 j4d2    = |              I I I I
