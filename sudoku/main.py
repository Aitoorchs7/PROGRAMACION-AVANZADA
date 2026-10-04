tablero1 = [
    [1, 0, 3, 4],
    [0, 4, 1, 0],
    [2, 1, 0, 3],
    [4, 3, 2, 1]
]

def leer_tablero(ruta):
    with open(ruta,"r") as f:
        tablero = []
        linea = f.readline()
        while linea:
            tablero.append(list(linea.split()))
    return tablero

def can_filas(tablero,num_fila,num_columna):
    candidatos_fila = {1,2,3,4}
    for num in tablero[num_fila]:
        if num !=0:
            candidatos_fila.discard(num)
    return candidatos_fila
        
def can_columnas(tablero,num_columna,num_fila):
    candidatos_columna = {1,2,3,4}
    for fila in tablero:
        if fila[num_columna] !=0:
            candidatos_columna.discard(fila[num_columna])
    return candidatos_columna

def resuelto(tablero):
    candidatos = []
    for i in range(len(tablero)):
        fila_candidatos = []
        for j in range(len(tablero)):
            if tablero[i][j] == 0:
                fila_candidatos.append(can_filas(tablero,i,j) & can_columnas(tablero,j,i))
            else:
                fila_candidatos.append(set())
        candidatos.append(fila_candidatos)
    return candidatos

def can_cuadrante(tablero,f,c): 
    
