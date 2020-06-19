import random
width = int(input("Enter The Width:"))
height = int(input("Enter The Height:"))

def grid(width,height,sym_ver="+",sym_col="+"):
##    ver = [f"{sym_ver} " for i in range(width+1)]
##    hor = [f"{sym_col}"*2 for i in range(width)]
##    ver = [f"{sym_ver} " for i in range(width+1)]
##    hor = [f"{sym_col}"*2 for i in range(width)]
    if(height%2 != 1):
        height += 1
    if width%2 != 1:
        width += 1
    walls = []
    for _ in range(height//2+1):
        if _ == height//2:
            walls.append([hor])
            walls.append([hor])
        else:
            
            ver = ""
            hor = ""
            #print("#"*width)
            hor += "#"*width
            walls.append([hor])
            __ = 0
            if _< height//2:
                while __ != width:
                    #print("#",end="")
                    __ += 1
                    ver += "#" 
                    if __ <width-1:
                        #print(" ",end="")
                        __ += 1
                        ver += " "
                    
            walls.append([ver])
##    a = " "
##    #walls.append([a if ( _ == width) "#" else " " for _ in range(width+1) ])
##    for i in range(width):
##        if i==width-1:
##            a+="#"
##        else:
##            a+=" "
##            
    walls.append([hor])
    return walls

def wall_matrix(width,height,filename,sym_ver="+",sym_hor="+"):
    
    gd = grid(width,height,sym_ver,sym_hor)
    file = open(filename,"w")
    for i in range(len(gd)):
        for j in range(len(gd[i])):
            file.write(gd[i][j])
            #print(gd[i][j])
            #if gd[i][j] == f"{sym_hor}"*3 or gd[i][j].find() 
                #walls.append(True)
            #else:
                #walls.append(False)
        file.write("\n")
    file.close()
    with open(filename) as f:
            contents = f.read()
        #print(type(contents))
        #print(contents)

        # Validate start and goal
##        if contents.count("A") != 1:
##            raise Exception("maze must have exactly one start point")
##        if contents.count("B") != 1:
##            raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
    contents = contents.splitlines()
    h = len(contents)
    w = max(len(line) for line in contents)
    spaces = 0
    allowed = []
        # Keep track of walls
    walls = []
    for i in range(height):
        row = []
        for j in range(width):
            try:
                if contents[i][j] == "A":
                    start = (i, j)
                    row.append(False)
                elif contents[i][j] == "B":
                    goal = (i, j)
                    row.append(False)
                elif contents[i][j] == " ":
                    #spaces += 1
                    allowed.append((i,j))
                    row.append(False)
                else:
                    row.append(True)
            except IndexError:
                #allowed.append((i,j))
                #row.append(False)
                pass
        walls.append(row)

        #solution = None
        #print(walls)
    go = []
    for row in range(1,h,2):
        go.append([(row,col) for col in range(1,w+1,2)])
    #print(go)
    def IsConnected(node):
        row = node[0]
        col = node[1]

        direction = {
                "LEFT": (row,col-2),
                "UP": (row-2,col),
                "RIGHT": (row,col+2),
                "DOWN": (row+2,col)
            }
        directionrub = {
                "LEFT": (row,col-1),
                "UP": (row-1,col),
                "RIGHT": (row,col+1),
                "DOWN": (row+1,col)
            }
        
        lst = []
        sfl = ["LEFT","UP",'DOWN','RIGHT']
        random.shuffle(sfl)
        lst2 = []
        for _ in sfl:
            
            r = direction.get(_)[0]
            c = direction.get(_)[1]
            if (0<=r<h and 0<=c<w):
                _r = directionrub.get(_)[0]
                _c = directionrub.get(_)[1]
                lst2.append((_r,_c))
                lst.append((r,c))
        return lst,lst2
    
    def DFS(mat):
        start = mat[0][0]
        #goal = mat[-1][-1]
        visited = [start]
        stack = [start]
        path = []
        #distance = []
        l = []
        for i in range(h):
            path.append([0 for j in range(w+1)])
            #distance.append([0 for j in range(h+1)])
        while stack != []:
            node = stack.pop(-1)
            conn,rub = IsConnected(node)
            for i in range(len(conn)):
                if conn[i] not in visited:
                    l.append((rub[i][0],rub[i][1]))
                    visited.append(conn[i])
                    stack.append((conn[i]))
                    #distance[conn[i][0]] [conn[i][1]] = distance[node[0]][node[1]] + 1
                    #print(node[0],node[1])
                    #print("------->",path[conn[i][0]][conn[i][1]])
                    r,c = node
                    path[conn[i][0]][conn[i][1]] = (r,c)
                    #print(r,c)
        #print(visited)
        return visited,l
        


        
            
            
        
    visited,l = DFS(go)
    file = open(filename,"w")
    for i in range(len(contents)):
        for j in range(len(contents[i])):
            #print(walls[i][j],end="")
            if (i,j) in visited or (i,j) in l:
                #walls[i][j]==" "
                print(" ",end="")
                file.write(" ")
            else:
                print("█",end="")
                file.write("#")
##                print("#",end="")
        print()
        file.write("\n")
    
    
    
wall_matrix(width,height,"maze.txt")

