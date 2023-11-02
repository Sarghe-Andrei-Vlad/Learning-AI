def read_matrix(filename):
    f = open("game.txt", "r")
    values = f.read()
    lines = values.split("\n")
    subjects = []
    values = []
    temp = []
    for i in range(0,2):
        subjects.append(lines[i].split())
    for i in range(2,len(lines)):
        temp = lines[i].split()
        store = []
        for j in range(len(temp)):
            store.append([int(x) for x in temp[j].split("/")])
            if j% (len(lines)-2) == 0:
                values.append(store)
    return (subjects,values)

def search_dominant_and_nash(subjects,values):
    # search dominant strat for Player A
    max_values_A = dict()
    max_lines_index_A = dict()
    for line_index,line in enumerate(values):
        for col_index,col in enumerate(line):
            if max_values_A.get(col_index, 0) < col[0]:
                max_values_A[col_index] = col[0] # valoarea maxima pe coloana
                max_lines_index_A[col_index] = line_index # salvez linia cu maximul pe coloana
    if len(list(set(list(max_lines_index_A.values())))) == 1: # verific daca toti maximii sunt pe aceeasi linie 
        print(subjects[0][0] + " has dominant strategy " + subjects[0][max_lines_index_A[0]+1])

    # search dominant strat for Player B
    max_values_B = dict()
    max_lines_index_B = dict()
    for line_index,line in enumerate(values):
        for col_index,col in enumerate(line):
            if max_values_B.get(line_index, 0) < col[1]:
                max_values_B[line_index] = col[1]
                max_lines_index_B[line_index] = col_index
    if len(list(set(list(max_lines_index_B.values())))) == 1:
        print(subjects[1][0] + " has dominant strategy " + subjects[1][max_lines_index_B[0]+1])
    print()
    print("Nash:")
    for line_index,line in enumerate(values):
        for col_index,col in enumerate(line):
            if max_values_A[col_index] == col[0] and max_values_B[line_index] == col[1]:
                print(max_values_A[col_index], "/", max_values_B[col_index])

subjects,values = read_matrix("game.txt")
search_dominant_and_nash(subjects,values)