array = [[75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [95, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [17, 47, 82, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [18, 35, 87, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [20, 4, 82, 47, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [19, 1, 23, 75, 3, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [88, 2, 77, 73, 7, 63, 67, 0, 0, 0, 0, 0, 0, 0, 0],
         [99, 65, 4, 28, 6, 16, 70, 92, 0, 0, 0, 0, 0, 0, 0],
         [41, 41, 26, 56, 83, 40, 80, 70, 33, 0, 0, 0, 0, 0, 0],
         [41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 0, 0, 0, 0, 0],
         [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 0, 0, 0, 0],
         [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 0, 0, 0],
         [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 0, 0],
         [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 0],
         [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
array_distances = []
gridWidth = 15

for x in range(gridWidth):
    array_distances.append([])
    for y in range(gridWidth):
        array_distances[x].append(0)

for x in range(gridWidth):
    for y in range(gridWidth):

        if not array[x][y] == 0:
            if not (x == 0 and y == 0):
                # left side of the pyramid
                if y == 0:
                    array_distances[x][y] = array[x][y] + array_distances[x - 1][y]
                # right side of the pyramid
                if x == y:
                    array_distances[x][y] = array[x][y] + array_distances[x - 1][y - 1]

                # choose the higher parent
                if array_distances[x - 1][y] > array_distances[x - 1][y - 1]:
                    array_distances[x][y] = array[x][y] + array_distances[x - 1][y]
                if array_distances[x - 1][y] <= array_distances[x - 1][y - 1]:
                    array_distances[x][y] = array[x][y] + array_distances[x - 1][y - 1]

            else:
                # top of the pyramid
                array_distances[x][y] = array[x][y]
        print(f"now column: {x} and row : {y} with value: {array_distances[x][y]}")

print(array_distances)

biggest = -1
for elem in array_distances[gridWidth-1]:
    if elem > biggest:
        biggest = elem
print(f"The biggest number is {biggest}")
