import math

# Creates the X and Y columns. There's no length limit, but X and Y must have the same length:
def getColumns():
    global n
    columns = []
    a = 1
    
    while (1 < 2):
        var = []
        
        print ("Input the #%d column - A null input closes the list." %(a))
        b = 1
        while (1 < 2):
            if (len(columns) == 1):
                if ((b - 1) == len(columns[0])):
                    break
            x = str(input("Enter the #%d number: " %(b)))
            if (x == ''):
                print()
                break
            var.append(float(x))
            n = b
            b += 1

        columns.append(var)
            
        if (len(columns) == 2):
            print()
            break
        a += 1
    return (columns)



# Sum the X and Y columns' values, append'em in a 2-sized array:
def getSums():
    sums = []
    a = 0
    
    while (a < len(columns)):
        x = 0
        for i in columns[a]:
            x += i
        sums.append(x)
        a += 1
    return (sums)


# Creates both X² and Y² arrays, respectivaly:
def getSquare():
    square = []
    a = 0
    
    while (a < len(columns)):
        square.append([])
        for i in columns[a]:
            square[a].append(i ** 2)
        a += 1
    return (square)



# Sums the X² and Y² columns' values, append'em in a 2-sized array:
def getSquareSums():
    square_sums = []
    a = 0
    
    while (a < len(columns)):
        x = 0
        for i in square[a]:
            x += i
        square_sums.append(x)
        a += 1
    return (square_sums)



# Creates the XY column and also do the sum of theirs values:
def getXY():
    global XY
    global XY_sums
    XY = []
    XY_sums = 0
    a = 0
    
    while (a < n):
        XY.append(columns[0][a] * columns[1][a])
        XY_sums += (columns[0][a] * columns[1][a])
        a += 1



# Do the math to get the correlation value, as it classifies it:
def getResults(XY_sums, sums, square_sums):
    global n
    global r
    global c
    global s
    
    r = ((n * (XY_sums) - (sums[0] * sums[1])) / (math.sqrt(((n * square_sums[0]) - (sums[0] ** 2)) * ((n * (square_sums[1])) - (sums[1] ** 2)))))

    if (r == 0):
        c = "NULL CORRELATION"
    elif (r < 0):
        c = "NEGATIVE CORRELATION"
    elif (r > 0):
        c = "POSITIVE CORRELATION"

    if ((r == 1) or (r == -1)):
        s = "PERFECT"
    elif (((r > 0.6) and (r < 1)) or ((r < -0.6) and (r > -1))):
        s = "STRONG"
    elif (((r > 0.3) and (r < 0.6)) or ((r < -0.3) and (r > -0.6))):
        s = "WEAK"
    elif (((r < 0.3) and(r > 0)) or ((r > -0.3) and(r < 0))):
        s = "REALLY WEAK"
    else:
        s = '\b'
        


# View's result's interface, shows the table and also the math process in a didatical way:
def view(columns, square, sums, XY_sums, square_sums, c, s):
    global n
    N = 0
    
    print ("N_______x_______________y_______________xy______________x²______________y²_________")
    while (N <  n):
        print ("%d\t%.1f\t\t%.1f\t\t%.1f\t\t%.1f\t\t%.1f" %((N + 1), columns[0][N], columns[1][N], XY[N], square[0][N], square[1][N]))
        N += 1
    print ("\tΣx= %.1f\tΣy= %.1f\tΣxy= %.1f\tΣx²= %.1f\tΣy²= %.1f" %(sums[0], sums[1], XY_sums, square_sums[0], square_sums[1]))


    print ('''

    r = ________[(n(Σxy)-(ΣxΣy)]________
        √{[n(Σx²)-(Σx)²][n(Σy²)-(Σy)²]}

    r = _________[(%d(%.1f)-(%.1f*%.1f)]_________
        √{[%d(%.1f)-(%.1f)²][%d(%.1f)-(%.1f)²]}

    r = ___________[(%.1f)-(%.1f)]___________
        √{[(%.1f)-(%.1f)][(%.1f)-(%.1f)]}

    r = ______%.1f______
        √{[%.1f][%.1f]}

    r = ____%.1f____
        √{%.1f}

    r = _%.1f_
        %.1f

    r = %f
    ''' %(n, XY_sums, sums[0], sums[1], n, square_sums[0], sums[0], n, square_sums[1], sums[1],
            (n * XY_sums), (sums[0] * sums[1]), (n * square_sums[0]), (sums[0] ** 2), (n * square_sums[1]), (sums[1] ** 2),
            ((n * XY_sums) - (sums[0] * sums[1])), ((n * square_sums[0]) - (sums[0] ** 2)), ((n * square_sums[1]) - (sums[1] ** 2)),
            ((n * XY_sums) - (sums[0] * sums[1])), (((n * square_sums[0]) - (sums[0] ** 2)) * ((n * square_sums[1]) - (sums[1] ** 2))),
            ((n * XY_sums) - (sums[0] * sums[1])), math.sqrt(((n * square_sums[0]) - (sums[0] ** 2)) * ((n * square_sums[1]) - (sums[1] ** 2))),
            r))
            
    print ("=> %s %s." %(c, s))

    input()



# The main function:
def main():
    global columns
    global sums
    global square
    global square_sums
    global XY
    global XY_sums 
    global r
    global c
    global s

    columns = getColumns()
    sums = getSums()
    square = getSquare()
    square_sums = getSquareSums()
    getXY()
    getResults(XY_sums, sums, square_sums)
    view(columns, square, sums, XY_sums, square_sums, c, s)

    # FOR DEBUG PURPOSES; USE AS YOU WISH:    
    #print ("Σx, Σy =", sums)
    #print ("x², y² =", square)
    #print ("Σx², Σy² =", square_sums)
    #print ("xy =", XY)
    #print ("Σxy =", XY_sums)
    #print ("n =", n)
    #print ("r =", r)

main()
