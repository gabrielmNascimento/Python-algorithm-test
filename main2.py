from typing import List

def lake_areas(matrix: List[List[int]], column: int = 0) -> List[int]:

    # Size counter of lake areas
    count: int = 0
    # Array to return the sizes of the lakes
    sizes = []
    # Array to store the return of the recursion
    result = []

    # Matrix Nested Loop
    for i in range(len(matrix)):

        # Check if it has a size to count
        if matrix[i][column] == 1:

            count = count + 1
            matrix[i][column] = 0

            # If condition to check if the iteration is inside the limits of the matrix
            if column + 1 < len(matrix[i]):

                # Loop through the line of founded size 1 / to continue to count size horizontally
                for j in range(column + 1, len(matrix[i])):

                    # Check if it has a size to count
                    if matrix[i][j] == 1:

                        count = count + 1
                        matrix[i][j] = 0

                        # If condition to check if the iteration is inside the limits of the matrix
                        if i - 1 != 0:

                            # Searching for 1's upside
                            for up in range(i - 1, 0, -1):

                                # Check if it has a size to count
                                if matrix[up][j] == 1:

                                    count = count + 1
                                    matrix[up][j] = 0

                                    # If condition to check if the iteration is inside the limits of the matrix
                                    if j != 0:

                                        # Searching for 1's upside left
                                        for upleft in range(j - 1, 0, -1):

                                            # Check if it has a size to count
                                            if matrix[up][upleft] == 1:

                                                count = count + 1
                                                matrix[up][upleft] = 0

                                            else:
                                                # Break the loop if found a 0
                                                break

                                    # If condition to check if the iteration is inside the limits of the matrix
                                    if j + 1 < len(matrix[i]):

                                        # Searching for 1's upside right
                                        for upright in range(j + 1, len(matrix[i])):

                                            # Check if it has a size to count
                                            if matrix[up][upright] == 1:

                                                count = count + 1
                                                matrix[up][upright] = 0

                                            else:
                                                # Break the loop if found a 0
                                                break


                                else:
                                    # Break the loop if found a 0
                                    break

                        # If condition to check if the iteration is inside the limits of the matrix
                        if i + 1 < len(matrix):

                                # Searching for 1's below
                               for down in range(i + 1, len(matrix)):

                                   # Check if it has a size to count
                                   if matrix[down][j] == 1:

                                       count = count + 1
                                       matrix[down][j] = 0

                                       # If condition to check if the iteration is inside the limits of the matrix
                                       if j != 0:

                                           # Searching for 1's down left
                                           for downleft in range(j - 1, 0, -1):

                                               # Check if it has a size to count
                                               if matrix[down][downleft] == 1:

                                                   count = count + 1
                                                   matrix[down][downleft] = 0

                                               else:
                                                   # Break the loop if found a 0
                                                   break

                                       # If condition to check if the iteration is inside the limits of the matrix
                                       if j + 1 < len(matrix[i]):

                                           # Searching for 1's down right
                                           for downright in range(j + 1, len(matrix[i])):

                                               # Checking if it is a size to count
                                               if matrix[down][downright] == 1:

                                                   count = count + 1
                                                   matrix[down][downright] = 0

                                               else:
                                                   # Break the loop if found a 0
                                                   break
                                   else:
                                       # Break the loop if found a 0
                                       break

                    else:
                        # Break the loop if found a 0
                        break

        else:
            if(count != 0):
                #Add the count to the size array
                sizes.append(count)
            count = 0

    if (count != 0):
        sizes.append(count)

    if(column + 1 < len(matrix[i])):
        # Recursion to pass through all columns
        result = lake_areas(matrix, column + 1)
        # Uniting the arrays
        sizes = sizes + result

    sizes.sort()
    return sizes


if __name__ == '__main__':
    matrix = [
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0]
    ]
    print(lake_areas(matrix))