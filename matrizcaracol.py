def cargar_archivo(lab):
    return open(lab)

def moverDerecha (mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col],end=" ")
            moverDerecha(mat,fil,col+1,aux+1,tam)
        if(aux==tam):
            moverAbajo(mat,fil+1,col-1,0,tam-1)
    else:
        print("")

def moverAbajo(mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col],end=" ")
            moverAbajo(mat,fil+1,col,aux+1,tam)
        if(aux==tam):
            moverIzquierda(mat,fil-1,col-1,0,tam)
    else:
        print("")
def moverIzquierda (mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col],end=" ")
            moverIzquierda(mat,fil,col-1,aux+1,tam)
        if(aux==tam):
            moverArriba(mat,fil-1,col+1,0,tam-1)
    else:
        print("")
        
def moverArriba (mat,fil,col,aux,tam):
    if(tam>0):
        if(aux<tam):
            print(mat[fil][col],end=" ")
            moverArriba(mat,fil-1,col,aux+1,tam)
        if(aux==tam):
            moverDerecha(mat,fil+1,col+1,0,tam)
    else:
        print("finalizo ")

def crear_matriz (mat,lab):
    for x in cargar_archivo(lab):
        mat.append(x.strip().split())
    return mat


        
def recorrematriz(lab):
    moverDerecha(crear_matriz([],lab),0,0,0,len(crear_matriz([],lab)))
                  
recorrematriz("Matriz.txt")
