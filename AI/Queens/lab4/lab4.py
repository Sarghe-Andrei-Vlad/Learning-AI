def block(matrix, row, column):
    matrix[row-1][column-1] = 'b'

#domenii
def domenii(matrix):
    domenii = dict()
    list2 = []
    
    for j in range(len(matrix[0])):
        list1 = []
        for i in range(len(matrix)):
            if(matrix[i][j] != 'b'):
                list1.append(i+1)
        list2.append(list1)

    counter = 0
    for elem in list2:
        counter = counter + 1
        domenii['X' + str(counter)] = elem
    return domenii

#restrictie
def verificaDiagonalaSus(matrice, row, column):
    iterRow = row
    iterCol = column
    while iterCol >= 0 and iterRow >= 0:
        if matrice[iterRow][iterCol] == 1:
            return False
        iterCol -= 1
        iterRow -= 1
    return True

#restrictie
def verificaDiagonalaJos(matrice, row, column):
    iterRow = row
    iterCol = column
    while iterCol >= 0 and iterRow < len(matrice):
        if matrice[iterRow][iterCol] == 1:
            return False
        iterRow += 1
        iterCol -= 1
    return True

#restrictie
def unicDiagonala(matrice, row, column):
    return verificaDiagonalaSus(matrice, row, column) and verificaDiagonalaJos(matrice, row, column)

#restrictie
def unicRand(matrice, row):
    for col in range(len(matrice)):
        if matrice[row][col] == 1:
            return False
    return True

#restrictie
def unicColoana(matrice, column):
    for row in range(len(matrice)):
        if matrice[row][column] == 1:
            return False
    return True

#restrictie
def isCorrect(matrice, row, column):
    return unicRand(matrice, row) and unicColoana(matrice, column) and unicDiagonala(matrice, row, column)

def ForwardChecking(matrice, regine):
    if len(matrice) == regine:
        for i in matrice:
            print(i)
        return True
    rowsProposition = getRowsProposition(matrice, regine)
    for row in rowsProposition:
        matrice[row][regine] = 1
        domainWipeOut = False
        for variable in getFromConstraint(matrice, regine):
            if fc(matrice, variable.row, variable.column):
                domainWipeOut = True
                break
        if not domainWipeOut:
            if ForwardChecking(matrice, regine + 1):
                return True
        matrice[row][regine] = 0


def fc(matrice, row, regine):
    actualDomain = getRowsProposition(matrice, regine)
    tempDomain = list(actualDomain)
    for propositionRow in actualDomain:
        if not isCorrect(matrice, propositionRow, regine):
            tempDomain.remove(propositionRow)
    return len(tempDomain) == 0



def getFromConstraint(matrice, regine):
    result = []
    for row in range(len(matrice)):
        for col in range(regine + 1, len(matrice)):
            if matrice[row][col] == 0 and isCorrect(matrice, row, col):
                result.append(Unassigned(row, col))
    return result


def getRowsProposition(matrice, regine):
    rows = []
    for row in range(len(matrice)):
        if isCorrect(matrice, row, regine):
            rows.append(row)
    return rows


def ForwardCheckingOrder(grid, queen):
    if len(grid) == queen:
        for i in grid:
            print(i)
        return True
    rowsProposition = getHeuristicRowsProposition(grid, queen)
    for row in rowsProposition:
        grid[row.row][queen] = 1
        domainWipeOut = False
        for variable in getUnassignedFromConstraint(grid, queen):
            if fc(grid, variable.row, variable.column):
                domainWipeOut = True
                break
        if not domainWipeOut:
            if ForwardCheckingOrder(grid, queen + 1):
                return True
        grid[row.row][queen] = 0


def getHeuristicRowsProposition(grid, queen):
    rows = []
    for row in range(len(grid)):
        if isCorrect(grid, row, queen):
            tempGrid = grid.copy()
            tempGrid[row][queen] = 1
            rows.append(HeuristicRow(row, queen, rateForHeuristic(tempGrid, queen + 1)))
    rows.sort(key=lambda x: x.rate)
    return rows


def rateForHeuristic(grid, queen):
    return len(getRowsProposition(grid, queen))


class HeuristicRow:

    def __init__(self, row, column, rate):
        self.row = row
        self.column = column
        self.rate = rate

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash(self.row) ^ hash(self.column)


class Unassigned:

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash(self.row) ^ hash(self.column)


matrix = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

print("Original ", matrix)
block(matrix,1,1), block(matrix,2,2), block(matrix,4,3)
print("With blocks ", matrix)
print("Domenii", domenii(matrix))

print("Forward checking")
print(ForwardChecking(matrix, 0))

