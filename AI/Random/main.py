global N
N = int(input())

board = [[0]*N for _ in range(N)]

def attacked(i,j):
    for k in range (0,N):
        if board[i][k] == 1 or board[k][j] ==1:
            return 1
    for k in range (0,N):
        for l in range (0,N):
            if k+l == i+j or k-l == i-j:
                if board[k][l] == 1:
                    return 1
    else:
        return 0



# Variables: Q1,.....,Qn
# Domains:   - Q1 : {1,...,n}
#            - .. :    ...
#            - Qn : {1,...,n}
# Restrictions: Q1 != Q2 != ... != Qn                           -       columns
#               Q1,Q2,....,Qn each has an unique value          -       lines
#               diagonal restrictions
#               Blocks given by the instance