
def mulmat(arg_1,arg_2):
    if not isinstance(arg_1,list) or not isinstance(arg_2,list):
        raise ValueError("Ambos argumentos deben ser de tipo lista")
    if len (arg_1[0]) != len(arg_2):
        raise ValueError("El numero de columnas del primer argumento debe ser igual al numero de filas del segundo")
    result=[]
    for i in range(len(arg_1)):
        for j in range(len(arg_2[0])):
            for k in range(len(arg_2)):
                result.append(arg_1[i][k]*arg_2[k][j])
    return(result)




def trasmatriz (arg):
    if type(arg) != list:
        raise TypeError ("El argumento debe ser una lista")
    filas=0
    columnas=0
    for i in arg:
        filas+=1
    for j in arg[0]:
        columnas+=1
    if filas != columnas:
        raise ValueError("La matriz debe ser cuadrada")
    else:
        traspuesta=[[fila[i] for fila in arg] for i in range (len(arg[0]))]
        return(traspuesta)



def determatriz (arg):
    if type(arg) != list:
        raise TypeError ("El argumento debe ser una lista")
    filas=0
    columnas=0
    for i in arg:
        filas+=1
    for j in arg[0]:
        columnas+=1
    if filas != columnas:
        raise ValueError("La matriz debe ser cuadrada")
    for i in range (filas-1):
        for j in range (i+1 ,filas):
            div=arg[j][i]/arg[i][i]
            for k in range(i,filas):
                arg[j][k] -= arg[i][k]*div
            for e in arg:
                print(e)
    det=1
    for i in range(filas):
        det*= arg[i][i]
    return(det)

def invmatriz(ar):
    if type(ar) != list:
        raise TypeError ("El argumento debe ser una lista")
    if determatriz(ar) == 0:
        print("la matriz no es invertible")
    else:
        n = len(ar)
        id=[[float(i==j) for i in range(n)] for j in range(n)]
        for i in range(n):
            ar[i] += id[i]
        
        for i in range(n):
            uno=ar[i][i]
            for j in range(2*n):
                ar[i][j]/=uno

        for k in range(n):
            if k != i:
                div = ar[k][i]
                for j in range (2*n):
                    ar [k][j] -= div*ar[i][j]

    inversa=[r[n:] for r in ar]
    return(inversa)

def eclin(arg_1,arg_2):
    arg_1_inv = invmatriz(arg_1)
    x = [sum(arg_1_inv[i][j] * arg_2[j] for j in range(len(arg_2))) for i in range(len(arg_1))]
    return x


