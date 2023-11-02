# restrictii = []
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         for elem in domenii(matrix):
#             for casuta in elem:
#                 if(casuta != 'b'):
#                     matrix[i][j] = 1
                
#                 if isCorrect(matrix, i, j) == False:
#                     restrictii.append(matrix[i][j])

# for i in range(domenii(matrix)):
#         if(matrix[i][j] != 'b' and isCorrect(matrix, i, j)): 
#             matrix[i][j] = 1

# print(restrictii)
# print("With queens", matrix)
# print("Forward Checking:")
# print(ForwardChecking(d, 4))
