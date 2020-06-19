import random
width = int(input("Enter The Width:"))
height = int(input("Enter The Height:"))

def grid(width,height,sym_ver="+",sym_col="+"):
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
            hor += "#"*width
            walls.append([hor])
            __ = 0
            if _< height//2:
                while __ != width:
                    __ += 1
                    ver += "#" 
                    if __ <width-1:
                        __ += 1
                        ver += " "
                    
            walls.append([ver]) 
    walls.append([hor])
    return walls

def wall_matrix(width,height,filename,sym_ver="+",sym_hor="+"):
    
    gd = grid(width,height,sym_ver,sym_hor)
    file = open(filename,"w")
    for i in range(len(gd)):
        for j in range(len(gd[i])):
            file.write(gd[i][j])
        file.write("\n")
    file.close()
    with open(filename) as f:
            contents = f.read()
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
                    allowed.append((i,j))
                    row.append(False)
                else:
                    row.append(True)
            except IndexError:
                pass
        walls.append(row)
    go = []
    for row in range(1,h,2):
        go.append([(row,col) for col in range(1,w+1,2)])
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
        visited = [start]
        stack = [start]
        path = []
        l = []
        for i in range(h):
            path.append([0 for j in range(w+1)])
        while stack != []:
            node = stack.pop(-1)
            conn,rub = IsConnected(node)
            for i in range(len(conn)):
                if conn[i] not in visited:
                    l.append((rub[i][0],rub[i][1]))
                    visited.append(conn[i])
                    stack.append((conn[i]))
                    r,c = node
                    path[conn[i][0]][conn[i][1]] = (r,c)
        return visited,l
        


        
            
            
        
    visited,l = DFS(go)
    file = open(filename,"w")
    for i in range(len(contents)):
        for j in range(len(contents[i])):
            if (i,j) in visited or (i,j) in l:
                print(" ",end="")
                file.write(" ")
            else:
                print("█",end="")
                file.write("#")
        print()
        file.write("\n")
    
    
    
wall_matrix(width,height,"maze.txt")

