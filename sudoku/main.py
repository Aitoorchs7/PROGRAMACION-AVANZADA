import os

tablero1 = [
    [1, 0, 3, 4],
    [0, 4, 1, 0],
    [2, 1, 0, 3],
    [4, 3, 2, 1]
]

def leer_tablero(ruta):
    tablero = []
    with open(ruta,"r") as f:
        for linea in f:
            if linea.strip():
                tablero.append([int(num) for num in linea.replace("|"," ").split()])
    return tablero

def escribir_tablero(ruta,tablero):
    with open(ruta,"w") as f:
        for fila in tablero:
            f.write(" ".join(str(num) for num in fila) + "\n")

def can_filas(tablero,num_fila,num_columna):
    candidatos_fila = set(range(1,len(tablero)+1))
    for num in tablero[num_fila]:
        if num !=0:
            candidatos_fila.discard(num)
    return candidatos_fila
        
def can_columnas(tablero,num_columna,num_fila):
    candidatos_columna = set(range(1,len(tablero)+1))
    for fila in tablero:
        if fila[num_columna] !=0:
            candidatos_columna.discard(fila[num_columna])
    return candidatos_columna

def can_cuadrante(tablero,num_fila,num_columna):
    candidatos_cuadrante = set(range(1,len(tablero)+1))
    lado = int(len(tablero) ** 0.5)
    fila_inicio = num_fila - (num_fila % lado)
    col_inicio = num_columna - (num_columna % lado)
    for i in range(fila_inicio,fila_inicio+lado):
        for j in range(col_inicio,col_inicio+lado):
            if tablero[i][j] != 0:
                candidatos_cuadrante.discard(tablero[i][j])
    return candidatos_cuadrante

def resuelto(tablero):
    candidatos = []
    for i in range(len(tablero)):
        fila_candidatos = []
        for j in range(len(tablero)):
            if tablero[i][j] == 0:
                fila_candidatos.append(can_filas(tablero,i,j) & can_columnas(tablero,j,i) & can_cuadrante(tablero,i,j))
            else:
                fila_candidatos.append(set())
        candidatos.append(fila_candidatos)
    return candidatos

def resolver(tablero):
    cambio = True
    while cambio:
        cambio = False
        candidatos = resuelto(tablero)
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if tablero[i][j] == 0 and len(candidatos[i][j]) == 1:
                    tablero[i][j] = candidatos[i][j].pop()
                    cambio = True
    return tablero

def esta_completo(tablero):
    return all(num != 0 for fila in tablero for num in fila)

if __name__ == "__main__":
    carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)),"tableros")
    tablero = leer_tablero(os.path.join(carpeta,"tablero.txt"))
    resolver(tablero)
    escribir_tablero(os.path.join(carpeta,"solucion.txt"),tablero)
    for fila in tablero:
        print(fila)
    print("Resuelto" if esta_completo(tablero) else "No se pudo resolver solo con candidatos únicos")
