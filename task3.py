def maximumrect(matrix):


    rows,cols= len(matrix),len(matrix[0])
    heigths=[0]*cols
    left=[0]*cols
    right=[cols]*cols


    max_area=0
        # Updating Heights
    for i in range(rows):
        c_left,c_right=0,cols

        for j in range(cols):

            if matrix[i][j]==1:
                heigths[j]+=1
            else:
                heigths[j]=0
        #updating left boundaries
        for j in range(cols):
            if matrix[i][j]==1:
                 left[j]=max(left[j],c_left)
            else:
                 left[j]=0
                 c_left=j+1
     
        for j in range(cols-1,-1,-1):
            if matrix[i][j]==1:
                right[j]=min(right[j],c_right)
            else:
                right[j]=cols
                c_right=j
    
        for j in range(cols):
            max_area=max(max_area,(right[j]-left[j])*heigths[j])
    return max_area
    
matrix=[
            [1,0,1,0,0],
            [1,0,1,1,0],
            [1,1,1,1,0],
            [1,0,0,1,0],

    ]
print("Rectangle Area", maximumrect(matrix))

