import copy

queue = []
visited = []

class Puzzle:
    def __init__(self, state, x, y):
        self.state = state
        self.x = x
        self.y = y

    def compare(self, puzzle):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != puzzle.state[i][j]:
                    return False
        return True

    def generateChildren(self):
        new = []

        if self.x - 1 >= 0:
            new.append([self.x - 1, self.y])
        if self.y + 1 <= 2:
                new.append([self.x, self.y + 1])
        if self.x + 1 <= 2:
            new.append([self.x + 1, self.y])
        if self.y - 1 >= 0 :
                new.append([self.x, self.y - 1])

        for i in new:
            temp = copy.deepcopy(self.state)
            t = temp[self.x][self.y]
            temp[self.x][self.y] = temp[i[0]][i[1]]
            temp[i[0]][i[1]] = t

            puzzle = Puzzle(temp, i[0], i[1])

            flag = False
            for visited_puzzle in visited:
                if puzzle.compare(visited_puzzle):
                    flag = True
                    break
            if flag == False:
                queue.append(puzzle)

    def display(self):

        for i in range(3):
            print(self.state[i])

        print(" ")


def findGoal(startPuzzle, endPuzzle):
    if startPuzzle.compare(endPuzzle):
        print("here")
        queue.clear()
        return 1

    startPuzzle.generateChildren()

    while len(queue) != 0:

        current = queue[0]
        queue.pop(0)

        if current.compare(endPuzzle):
            print("here1")
            queue.clear()
            return 1
        else:
            current.display()
            visited.append(current)
            findGoal(current, endPuzzle)


startPuzzle = Puzzle([['1', '8', '2'], ['_', '4', '3'], ['7', '6', '5']],1 , 0)
endPuzzle = Puzzle([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']], 2, 2)

visited.append(startPuzzle)
findGoal(startPuzzle, endPuzzle)
