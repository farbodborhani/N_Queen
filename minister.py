N=int(input('Number of Queen:'))
board=[[0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0]]

count=0

def isSafe(board,i,j,N):
    for row in range(0,i):
        if(board[row][j]==1):
            return False
    x=i
    y=j
    while(x>=0 and y>=0):
        if(board[x][y]==1):
            return False
        x=x-1
        y=y-1
    x=i
    y=j
    
    while(x>=0 and y<N):
        if(board[x][y]==1):
            return False
        x=x-1
        y=y+1
        
    return True    
        
        
            


def solveQueen(board,i,N):
    global count
    if(i==N):
        for i in range(0,N):
            for j in range(0,N):
                if(board[i][j]==1):
                    print('Q',end=' ')
                else:
                    print('_',end=' ')
            print('\n')
        print('\n')
        count=count+1
        return False
    for j in range(0,N):
        if(isSafe(board,i,j,N)):
            board[i][j]=1
            nextQueen=solveQueen(board,i+1,N)
            if(nextQueen):
                return True
            board[i][j]=0
    return False
        
        

solveQueen(board,0,N)
print(count)