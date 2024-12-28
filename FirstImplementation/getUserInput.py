from collections import deque
import time
import os
import sys
if os.name == 'nt':
    os.system('')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def draw_matrix(mat):
    print("\033[H", end="")
    for i in range(N):
        for j in range(N):
            if (i, j) in visited:
                print(bcolors.OKBLUE + mat[i][j], end=" ")
            elif [i, j] in q:
                print(bcolors.FAIL + mat[i][j], end=" ")
            else:
                print(bcolors.WARNING + mat[i][j], end=" ")
        print("\033[0m")
N = int(input("Enter N: "))

response = ""
obstacles = []
while response != ['q']:
    obstacles.append(response)
    response = [x for x in input("Enter obstacle coords: ").split(" ")]

obstacles.pop(0)
obstacles = [[int(x), int(y)] for x,y in obstacles]
mat = [['*' for _ in range(N)] for _ in range(N)]

for a, b in obstacles:
    mat[a][b] = "#"

for i in mat:
    print(*i)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start = [0, 0]
end = [N - 1, N - 1]

dist = {}
for i in range(N):
    for j in range(N):
        dist[(i, j)] = float('inf')

dist[(0, 0)] = 0

visited = set()
q = deque([start])
print("\033[2J", end="")


def draw_matrix_with_path(mat, end):
    pass


while q:
    currX, currY = q.popleft()
    visited.add((currX, currY))
    if currX == end[0] and currY == end[1]:
        draw_matrix_with_path(mat, end)
        print("Path found!")
        break
    for dx, dy in directions:
        nx, ny = currX + dx, currY + dy
        if 0 <= nx < N and 0 <= ny < N:
            newDist = dist[(currX, currY)] + 1
            if mat[nx][ny] == "*" and newDist < dist[(nx, ny)]:
                dist[(nx, ny)] = newDist
                q.append([nx, ny])

    temp = draw_matrix(mat)
    time.sleep(0.2)
    os.system('CLS')

print(dist)




