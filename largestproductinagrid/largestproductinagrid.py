grid = []
mx = 0

with open('grid.txt') as file:
    for line in file.readlines():
        grid.append([int(x) for x in line.split()])

for i in range(len(grid)-3):
    for j in range(len(grid[0])):
        n = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
        if n > mx:
            mx = n

for i in range(len(grid)):
    for j in range(len(grid[0])-3):
        n = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        if n > mx:
            mx = n

for i in range(len(grid)-3):
    for j in range(len(grid[0])-3):
        n = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
        if n > mx:
            mx = n

for i in range(len(grid)-3):
    for j in range(3, len(grid[0])):
        n = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
        if n > mx:
            mx = n

print(mx)
