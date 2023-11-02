#1
#jug1, jug2 are the maximum quantities in the jugs mentioned before
def initializeQuantityOfJugs (n, m, k) :
    jug1 = n 
    jug2 = m
    QuantityWanted = k

#2
#quantityJug1, quantityJug2 are the current quantities of the jars
#starea initiala
def initialState (quantityJug1, quantityJug2) : 
    if(quantityJug1 == 0 and quantityJug2 == 0) :
        return True

# #starea finala
def finalState (quantityJug1, quantityJug2, quantityWanted, jug1, jug2) :
    if ((quantityJug1 <= jug1 and quantityJug2 == quantityWanted) or (quantityJug2 <= jug2 and quantityJug2 == quantityWanted)):
        return True

#3

#umplere completa
def fillJug1 (q, quantityJug1, jug1) : 
    q.append([jug1, quantityJug1] ) 
   
def fillJug2(q, quantityJug2, jug2) :
    q.append([quantityJug2, jug2]) 

#golire
def emptyJug1(q, jug1):
    q.append([jug1, 0])

def emptyJug2(q, jug2):
    q.append([0, jug2])

#transfer
def transferWater (q, jug1, jug2, jug, water) : 
    if(jug == "jug1"):
        c = jug1 - water
        d = jug2 + water
        validMove(q, c, d, jug1, jug2)
    elif(jug == "jug2"):
        c = jug1 + water
        d = jug2 - water
        validMove(q, c, d, jug1, jug2)

def isFinal(jug1, jug2, quantityWanted) :
    if(jug1 == quantityWanted or jug2 == quantityWanted): 
        return True
    else:
        return False

def validMove (q, c, d, jug1, jug2) :
        if ((c == 0 and c >= 0) or d == jug2):
                q.append([c, d])

        if (c == jug1 or (d == 0 and d >= 0)):
            q.append([c, d])

#9
def HasSolution (jug1, jug2, quantityWanted):
    print("The instance has solution:", BFS(jug1, jug2, quantityWanted))

#5 BFS
from collections import deque

def BFS(jug1, jug2, quantityWanted):
    m = {}
    isSolvable = False
    path = []
 
    q = deque()  #states
 
    #initial state
    q.append((0, 0))
 
    while (len(q) > 0):
 
        #Current state
        u = q.popleft()

        # If this state is already visited
        if ((u[0], u[1]) in m):
            continue
            
        #requirments are not met
        if ((u[0] > jug1 or u[1] > jug2 or
             u[0] < 0 or u[1] < 0)):
            continue
 
        # Filling
        path.append([u[0], u[1]])
 
        #marking the state that was 
        m[(u[0], u[1])] = 1
 
        # if it's correct 
        if (isFinal(u[0], u[1], quantityWanted)):
            isSolvable = True
            
            #fill final state
            if (u[0] == quantityWanted):
                if (u[1] != 0):
                    path.append([u[0], 0])
            else:
                if (u[0] != 0):
                    path.append([0, u[1]])

            pathSize = len(path)
            for i in range(pathSize):
                print(path[i][0], ",", path[i][1])
            break

        #the final state was not met
        fillJug2(q, u[0], jug2)
        fillJug1(q, u[1], jug1)  

        for water in range(max(jug1, jug2) + 1):
            # # Pour amount ap from jug2 to jug1
            # transferWater(q, u[0], u[1], "jug2", water)
            # # Pour amount ap from jug1 to jug2
            # transferWater(q, u[0], u[1], "jug1", water)
            c = u[0] + water
            d = u[1] - water
 
            # Check if this state is possible or not
            if (c == jug1 or (d == 0 and d >= 0)):
                q.append([c, d])
 
            # Pour amount ap from jug1 to jug2
            c = u[0] - water
            d = u[1] + water
 
            # Check if this state is possible or not
            if ((c == 0 and c >= 0) or d == jug2):
                q.append([c, d])
 
        # empty jugs
        emptyJug2(q, jug2)
        emptyJug1(q, jug1)
        
    return isSolvable
 
if __name__ == '__main__':
    jug1 = 4 
    jug2 = 3 
    quantityWanted = 2
    BFS(4, 3, 2)
    HasSolution(4,3,2)
    HasSolution(1,1,3)



    


