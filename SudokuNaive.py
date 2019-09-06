import numpy as np
A = np.array([[2, 3, 0, 4, 1, 5, 0, 6, 8],
             [0, 8, 0, 2, 3, 6, 5, 1, 9],
             [1, 6, 0, 9, 8, 7, 2, 3, 4],
             [3, 1, 7, 0, 9, 4, 0, 2, 5],
             [4, 5, 8, 1, 2, 0, 6, 9, 7],
             [9, 2, 6, 0, 5, 8, 3, 0, 1],
             [0, 0, 0, 5, 0, 0, 1, 0, 2],
             [0, 0, 0, 8, 4, 2, 9, 0, 3],
             [5, 9, 2, 3, 7, 1, 4, 8, 6]])
print(A)
A1 = np.transpose(A)


# row wise blocks
B = [[A[0:3,0:3],A[0:3,3:6],A[0:3,6:9]],
     [A[3:6,0:3],A[3:6,3:6],A[3:6,6:9]],
     [A[6:9,0:3],A[6:9,3:6],A[6:9,6:9]]]
#column wise blocks
A1 = np.transpose(A)
B1 = [[A1[0:3,0:3],A1[0:3,3:6],A1[0:3,6:9]],
      [A1[3:6,0:3],A1[3:6,3:6],A1[3:6,6:9]],
      [A1[6:9,0:3],A1[6:9,3:6],A1[6:9,6:9]]]
count = False
c = 1

while not count:
    # j to access all the three blocks column
    count = True
    for j in range(3):
        # i for checking each number from 1 to 10 whether it was there in particular block or not
        for i in range(1,10):
            # will store the row in which i is not present
            index = [0,1,2]
            # will store the block of that index
            dabba = [0,1,2]
            # will store the column of that block in which i is not present will store after examining A
            col = [0,1,2]
            # if i was present in 2 blocks of given row then we have eliminated the two row possibility of i in third block
            # np.argwhere(B[a][b]==i) will return the indexes where elements of B[a][b] is equal to i
            if len(np.argwhere(B[j][0]==i))+len(np.argwhere(B[j][1]==i))+len(np.argwhere(B[j][2]==i)) == 2:
                # if i is present in B[a][b] then remove those indexes from the index and col
                if len(np.argwhere(B[j][0]==i)):
                    #print(B[j][0])
                    #print(np.argwhere(B[j][0]==i),i,j)
                    # remove that row where i is present in jth row blocks
                    index.remove(np.argwhere(B[j][0]==i)[0][0])
                    # remove that block also for consideration
                    dabba.remove(0)
                if len(np.argwhere(B[j][1]==i)):
                    #print(B[j][1])
                    #print(np.argwhere(B[j][1]==i),i,j)
                    index.remove(np.argwhere(B[j][1]==i)[0][0])
                    dabba.remove(1)
                if len(np.argwhere(B[j][2]==i)):
                    #print(np.argwhere(B[j][2]==i),i,j)
                    index.remove(np.argwhere(B[j][2]==i)[0][0])
                    dabba.remove(2)
                row = 3*j + index[0] 
                a = np.argwhere(B[j][dabba[0]][index[0]])
                a = a[:,0]
                for k in range(len(a)):
                    col.remove(a[k])
                if len(col) == 2:
                    if len(np.argwhere(A[:,3*dabba[0] + col[0]]==i)):
                        A[row][3*dabba[0] + col[1]] = i
                        count = False
                    elif len(np.argwhere(A[:,3*dabba[0] + col[1]]==i)):
                        A[row][3*dabba[0] + col[0]] = i
                        count = False
                elif len(col) == 1:
                    A[row][3*dabba[0] + col[0]] = i
                    count = False

                B = [[A[0:3,0:3],A[0:3,3:6],A[0:3,6:9]],
                     [A[3:6,0:3],A[3:6,3:6],A[3:6,6:9]],
                     [A[6:9,0:3],A[6:9,3:6],A[6:9,6:9]]]
    A1 = np.transpose(A)
    B1 = [[A1[0:3,0:3],A1[0:3,3:6],A1[0:3,6:9]],
          [A1[3:6,0:3],A1[3:6,3:6],A1[3:6,6:9]],
          [A1[6:9,0:3],A1[6:9,3:6],A1[6:9,6:9]]]
    # for operation blocks rowwise
    # j to access all the three blocks column
    for j in range(3):
        # i for checking each number from 1 to 10 whether it was there in particular block or not
        for i in range(1,10):
            # will store the row in which i is not present
            index = [0,1,2]
            # will store the block of that index
            dabba = [0,1,2]
            # will store the column of that block in which i is not present will store after examining A
            col = [0,1,2]
            # if i was present in 2 blocks of given row then we have eliminated the two row possibility of i in third block
            # np.argwhere(B[a][b]==i) will return the indexes where elements of B[a][b] is equal to i
            if len(np.argwhere(B1[j][0]==i))+len(np.argwhere(B1[j][1]==i))+len(np.argwhere(B1[j][2]==i)) == 2:
                # if i is present in B[a][b] then remove those indexes from the index and col
                if len(np.argwhere(B1[j][0]==i)):
                    #print(B[j][0])
                    #print(np.argwhere(B[j][0]==i),i,j)
                    # remove that row where i is present in jth row blocks
                    index.remove(np.argwhere(B1[j][0]==i)[0][0])
                    # remove that block also for consideration
                    dabba.remove(0)
                if len(np.argwhere(B1[j][1]==i)):
                    #print(B[j][1])
                    #print(np.argwhere(B[j][1]==i),i,j)
                    index.remove(np.argwhere(B1[j][1]==i)[0][0])
                    dabba.remove(1)
                if len(np.argwhere(B1[j][2]==i)):
                    #print(np.argwhere(B[j][2]==i),i,j)
                    index.remove(np.argwhere(B1[j][2]==i)[0][0])
                    dabba.remove(2)
                row = 3*j + index[0] 
                a = np.argwhere(B1[j][dabba[0]][index[0]])
                a = a[:,0]
                for k in range(len(a)):
                    col.remove(a[k])
                if len(col) == 2:
                    if len(np.argwhere(A1[:,3*dabba[0] + col[0]]==i)):
                        A1[row][3*dabba[0] + col[1]] = i
                        count = False
                    elif len(np.argwhere(A1[:,3*dabba[0] + col[1]]==i)):
                        A1[row][3*dabba[0] + col[0]] = i
                        count = False
                elif len(col) == 1:
                    A1[row][3*dabba[0] + col[0]] = i
                    count = False

                B1 = [[A1[0:3,0:3],A1[0:3,3:6],A1[0:3,6:9]],
                      [A1[3:6,0:3],A1[3:6,3:6],A1[3:6,6:9]],
                      [A1[6:9,0:3],A1[6:9,3:6],A1[6:9,6:9]]]

    for i in range(9):
        for k in range(9):
            A[i,j] = A1[j,i]
    #if c == len(np.argwhere(A)):
     #   print("break")
      #  break
    c = len(np.argwhere(A))
    

            #print("col",col)
            #print("i",i)
            #print("index",index)
            #print("dabba",dabba)
            #print("row",row)
#print(len(np.argwhere(A)))
#print(A)
#print("section1")


    # applying columnwise and rowise operation
    for l in range(9):
        # will store that rows no elements are present
        row = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # will store that column where no elements are present
        col = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # will store that elements which may be there at those row positions
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # will store that elements which may be there at those column positions
        num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # finding non zero element index at lth row
        a = np.argwhere(A[l,:])
        a = a[:,0]
        for m in range(len(a)):
            col.remove(a[m])
            num1.remove(A[l,a[m]])
        if len(col) == 2:
            #print('kjdf',l,num1,col)
            if len(np.argwhere(A[:,col[0]] == num1[0])):
                A[l,col[0]] = num1[1]
                A[l,col[1]] = num1[0]
                count = False
            elif len(np.argwhere(A[:,col[0]] == num1[1])):
                A[l,col[0]] = num1[0]
                A[l,col[1]] = num1[1]
                count = False
            elif len(np.argwhere(A[:,col[1]] == num1[0])):
                A[l,col[1]] = num1[1]
                A[l,col[0]] = num1[0]
                count = False
            elif len(np.argwhere(A[:,col[1]] == num1[1])):
                print('sj')
                A[l,col[1]] = num1[0]
                A[l,col[0]] = num1[1]
                count = False
                print(A[l,col[1]],A[l,col[0]],num1[0] )
        elif len(col) == 1:
            A[l,col[0]] = num1[0]
            count = False



        a = np.argwhere(A[:,l])
        a = a[:,0]
        for m in range(len(a)):
            row.remove(a[m])
            num.remove(A[a[m],l])
        if len(row) == 2:
            if len(np.argwhere(A[row[0],:]==num[0])):
                A[row[0],l] = num[1]
                A[row[1],l] = num[0]
                count = False
            elif len(np.argwhere(A[row[0],:] == num[1])):
                A[row[0],l] = num[0]
                A[row[1],l] = num[1]
                count = False
            elif len(np.argwhere(A[row[1],:] == num[0])):
                A[row[1],l] = num[1]
                A[row[0],l] = num[0]
                count = False
            elif len(np.argwhere(A[row[1],:] == num[1])):
                A[row[1],l] = num[0]
                A[row[0],l] = num[1]
                count = False
        elif len(row) == 1:
            A[row[0],l] = num[0]
            count = False
    #print(len(np.argwhere(A)))
    #print(A)
    #print("Section2")


    for j in range(3):
        for k in range(3):
            elements = [1,2,3,4,5,6,7,8,9]
            row = [0,1,2]
            col = [0,1,2]
            row1 = []
            col1 = []
            if len(np.argwhere(B[j][k] == 0)) == 2:
                a = np.argwhere(B[j][k] == 0)
                for p in range(3):
                    for o in range(3):
                        if B[j][k][p][o]:
                            elements.remove(B[j][k][p][o])

                if len(np.argwhere(A[:,3*k + a[0][1]]==elements[0])) or len(np.argwhere(A[3*j + a[0][0],:]==elements[0])):
                    A[3*j + a[0][0],3*k + a[0][1]] = elements[1]
                    A[3*j + a[1][0],3*k + a[1][1]] = elements[0]
                    count = False
                elif len(np.argwhere(A[:,3*k + a[1][1]]==elements[0])) or len(np.argwhere(A[3*j + a[1][0],:]==elements[0])):
                    A[3*j + a[0][0],3*k + a[0][1]] = elements[0]
                    A[3*j + a[1][0],3*k + a[1][1]] = elements[1]
                    count = False
                elif len(np.argwhere(A[:,3*k + a[0][1]]==elements[1])) or len(np.argwhere(A[3*j + a[0][0],:]==elements[1])):
                    A[3*j + a[0][0],3*k + a[0][1]] = elements[0]
                    A[3*j + a[1][0],3*k + a[1][1]] = elements[1]
                    count = False
                elif len(np.argwhere(A[:,3*k + a[1][1]]==elements[1])) or len(np.argwhere(A[3*j + a[1][0],:]==elements[1])):
                    A[3*j + a[0][0],3*k + a[0][1]] = elements[1]
                    A[3*j + a[1][0],3*k + a[1][1]] = elements[0]
                    count = False


            elif len(np.argwhere(B[j][k]) == 0) == 1:
                a = np.argwhere(B[j][k] == 0)
                A[3*j + a[0][0],3*k + a[0][1]] = elements[0]
                count = False
print(len(np.argwhere(A)))
print(A)
print("section3")
