#Cifrado cesar con clave de cifrado = 14 letras
abc_1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
abc_2=["n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]

#Cifrado
def cif(arg):
    if type(arg) != str:
        raise TypeError ("El argumento debe ser de tipo str")
    else:
        pbra_des=list(arg)
        pbra_cif=[]
        for p in pbra_des:
            for c in range(27):
                if abc_1[c] == p:
                    pbra_cif.append(abc_2[c])
        return("".join(pbra_cif))

#Descifrado
def decif(arg):
    if type(arg) != str:
        raise TypeError ("El argumento debe ser de tipo str")
    else:
        pbra_cif=list(arg)
        pbra_des=[]
        for p in pbra_cif:
            for c in range(27):
                if abc_2[c] == p:
                    pbra_des.append(abc_1[c])
        return("".join(pbra_des))

