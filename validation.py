# Modul de funciones de validacion
    # validaciones numericas
        # validacion de enteros (int)
def valInt (*arg):
    if len(arg) == 1:
        return(isinstance(arg[0],int))
    if len(arg) == 2:
        if not isinstance(arg[1],(tuple,list)):
            raise TypeError("El segundo argumento debe ser una tupla o una lista")
        if len(arg[1]) != 2:
            raise ValueError("El segundo argumento debe contener 2 elementos")
        if arg[1][0] >= arg[1][1]:
            raise ValueError("Los elementos del segundo argumento no deben ser iguales y deben estar ordenados de forma ascendente")
        if not isinstance(arg[0],int):
            return(False)
        else:
            if type(arg[1]) == tuple:
                if arg[0] in range (arg[1][0]+1,arg[1][1]):
                    return(True)
                else:
                    return(False)
            elif type(arg[1]) == list:
                if arg[0] in range (arg[1][0],arg[1][1]+1):
                    return(True)
                else:
                    return(False)
    if len(arg) > 2:
        raise ValueError("Se deben ingresar 2 argumentos en esta función, un número entero y una lista o tupla")

        # validacion de flotantes (float)
def valFloat (*arg):
    if len(arg) == 1:
        return(isinstance(arg[0],float))
    if len(arg) == 2:
        if not isinstance(arg[1],(tuple,list)):
            raise TypeError("El segundo argumento debe ser una tupla o una lista")
        if len(arg[1]) != 2:
            raise ValueError("El segundo argumento debe contener 2 elementos")
        if arg[1][0] >= arg[1][1]:
            raise ValueError("Los elementos del segundo argumento no deben ser iguales y deben estar ordenados de forma ascendente")
        if not isinstance(arg[0],float):
            return(False)
        else:
            if type(arg[1]) == tuple:
                if int(arg[0]*(10**5)) in range (int(arg[1][0]*(10**5))+1,int(arg[1][1]*(10**5))):
                    return(True)
                else:
                    return(False)
            elif type(arg[1]) == list:
                if int(arg[0]*(10**5)) in range (int(arg[1][0]*(10**5)),int(arg[1][1]*(10**5))+1):
                    return(True)
                else:
                    return(False)
    if len(arg) > 2:
        raise ValueError("Se deben ingresar 2 argumentos en esta función, un número flotante (con valores decimales) y una lista o tupla")
    
        # validacion de complejos (complex)
def valComplex (*arg):
    if len(arg) == 1:
        return(isinstance(arg[0],complex))
    if len(arg) == 2:
        if not isinstance(arg[1],(tuple,list)):
            raise TypeError("El segundo argumento debe ser una lista o una tupla")
        if arg[1][0] >= arg[1][1]:
            raise ValueError("El primer elemento del segundo argumento debe ser menor que el segundo elemento")
        if isinstance(arg[0],complex):
            if type(arg[1]) == list:
                if arg[1][0] <= abs(arg[0]) <= arg[1][1]:
                    return(True)
                else:
                    return(False)
            elif type(arg[1]) == tuple:
                if arg[1][0] < abs(arg[0]) < arg[1][1]:
                    return(True)
                else:
                    return(False)
    if len(arg) > 2:
        raise ValueError("Se deben ingresar 2 argumentos en esta función, un número complejo (con una parte real y otra imaginaria) y una lista o tupla")
            
        # validacion de listas (list)
def valList (*arg):
    if len (arg) == 1:
        if type (arg[0]) == list:
            return(True)
        else:
            return(False)
    if len arg == 3:
        if not (type(arg[1])==int and type(arg[2])==str):
            raise TypeError
        if not (type(arg[1])==list and type(arg[2])==str):
            raise TypeError
        if not (type(arg[0]) == list and type(arg[1]) == list):
            return(False)
        if not arg[0] == arg [1]:
            return(False)

 

