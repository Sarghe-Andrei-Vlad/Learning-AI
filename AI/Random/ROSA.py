def ForwardChecking(matrice, regine):
    if len(matrice) == regine:
        for i in matrice:
            print(i)
        return True
    rowsProposition = getRowsProposition(matrice, regine)
    for row in rowsProposition:
        matrice[row][regine] = 1
        domainWipeOut = False
        for variable in getUnassignedFromConstraint(matrice, regine):
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


def verificaDiagonalaSus(matrice, row, column):
    iterRow = row
    iterCol = column
    while iterCol >= 0 and iterRow >= 0:
        if matrice[iterRow][iterCol] == 1:
            return False
        iterCol -= 1
        iterRow -= 1
    return True


def verificaDiagonalaJos(matrice, row, column):
    iterRow = row
    iterCol = column
    while iterCol >= 0 and iterRow < len(matrice):
        if matrice[iterRow][iterCol] == 1:
            return False
        iterRow += 1
        iterCol -= 1
    return True


def unicDiagonala(matrice, row, column):
    return verificaDiagonalaSus(matrice, row, column) and verificaDiagonalaJos(matrice, row, column)


def isCorrect(matrice, row, column):
    return unicRand(matrice, row) and unicColoana(matrice, column) and unicDiagonala(matrice, row, column)


def unicRand(matrice, row):
    for col in range(len(matrice)):
        if matrice[row][col] == 1:
            return False
    return True


def unicColoana(matrice, column):
    for row in range(len(matrice)):
        if matrice[row][column] == 1:
            return False
    return True


def getUnassignedFromConstraint(matrice, regine):
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


if __name__ == '__main__':
    with open('block-10-14-1.param') as f:
        lines = f.readlines()
    n = int(lines[0].split(" ")[4])
    m = lines[1].split("[")[3]
    i = 2
    restrictii = []
    while (i < len(lines[1].split("["))):
        str = lines[1].split("[")[i]
        j = i
        ok = 0
        nr1 = ""
        nr2 = ""
        for j in range(len(str)):
            if (str[j].isnumeric() and ok == 0):
                while (str[j].isnumeric()):
                    nr1 += str[j]
                    j += 1
                ok = 1
            if (ok == 1):
                if (str[j].isnumeric()):
                    while (str[j].isnumeric()):
                        nr2 += str[j]
                        j = j + 1
                    ok = 2

        restrictii.append([int(nr1), int(nr2)])
        i = i + 1
    a = [[0 for _ in range(0, n)] for _ in range(0, n)]
    b = [[0 for _ in range(0, n)] for _ in range(0, n)]
    for i in restrictii:
        a[i[0] - 1][i[1] - 1] = -1
        b[i[0] - 1][i[1] - 1] = -1
    for i in a:
        print(i)
    x = []
    d = []
    for i in range(n):
        l = []
        for j in range(n):
            if (a[i][j] != -1):
                l.append(j)
        d.append(l)
    print("Domeniul este:")
    print(d)
    print("Forward Checking:")
    ForwardChecking(a, 0)
    print('---------------------------')
    ForwardCheckingOrder(b, 0)
