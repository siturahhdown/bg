
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#matrix[0][2] = 20 #allows to change it to a variable in that list
#print(matrix[0][1]) #0= 1st line 1= 2nd optian in 1st list

for row in matrix:
    for item in row:
        print(item)