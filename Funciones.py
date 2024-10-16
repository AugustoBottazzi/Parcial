def cargar_existencia():
    provincias = ["PBA", "CABA", "Chubut", "Tucuman", "Mendoza"]
    tipo_juguete = ["Autos", "Muñecas", "Trenes", "Peluches", "Spinners", "Cartas"]
    
    existencias = [[0 for _ in range (3)] for _ in 
    range (len(provincias)) * len(tipo_juguete)]
    
    indice = 0
    
    for i in range(len(provincias)):
        for j in range (len(tipo_juguete)):
            cantidad = int(input(f"Ingrese la cantidad de {tipo_juguete[j]} en {provincias[i]}: "))

    existencias [indice] [0] = provincias [i]
    existencias [indice] [1] = tipo_juguete [j]
    existencias [indice] [2] = cantidad

    indice += 1

    return existencias
    
def mostrar_existencias (existencias):
    print("\nExistencias de Juguete por provincia: ")
    print("\nProvincia - Tipo de juguete - Cantidad")
    print("------------------------------------------")
    for fila in existencias:
        print(f"{fila[0]}\t{fila[1]}\t{fila[2]}")

def calcular_totales(existencias):
    totales_por_provincia = {}  
    for fila in existencias:
        provincia = fila [0]
        cantidad = fila[2]

    if provincia in totales_por_provincia:
        totales_por_provincia[provincia] += cantidad
    else:
        totales_por_provincia[provincia] = cantidad
    
    print("\nTotal de juguetes almacenados por provincia: ")
    print("Provincia\tTotal de los juguetes")
    print("------------------------------------------")

    for provincia in totales_por_provincia:
        Total = totales_por_provincia[provincia]
    print(f"{provincia}\t{Total}")

def juguetes_a_reponer (existencias, minimo_juguetes_a_reponer = 500):
    juguetes_necesarios = []
    for fila in existencias:
        provincia = fila[0]
        tipo_de_juguete = fila [1]
        cantidad = fila [2]

    if cantidad <minimo_juguetes_a_reponer:
        juguetes_necesarios += [(provincia), (tipo_de_juguete), (cantidad)]
        return juguetes_necesarios
    
def maximo_por_tipo (existencias):
    Max = []
    for fila in existencias:
        provincia = fila[0]
        tipo_de_juguete = fila[1]
        cantidad = fila [2]
    
    max_cantidad = Max[tipo_de_juguete] [0] if tipo_de_juguete in Max else 0
    if cantidad > max_cantidad:
        Max [tipo_de_juguete] = (cantidad, provincia)
        return Max
    
def mostrar_maximos (Max):
    print("\nMaxima cantidad de juguetes almacenados por tipo: ")
    print("Tipo de juguete\tCantidad\tProvincia")
    print("------------------------------------------")

    for tipo_de_juguete in Max:
        Cantidad = Max [tipo_de_juguete] [0]
        Provincia = Max [tipo_de_juguete] [1]
    print(f"{tipo_de_juguete}\t{Cantidad}\t{Provincia}")

def recaudacion_por_deposito (existencias, precios):
    recaudaciones = {}
    for fila in existencias:
        provincia = fila [0]
        tipo_de_juguete = fila [1]
        cantidad = fila [2]

    precio = precios [tipo_de_juguete]
    recaudacion = cantidad * precio

    if provincia in recaudaciones:
        recaudaciones [provincia] += recaudacion
    else:
        recaudaciones [provincia] = recaudacion

    return recaudaciones

def deposito_mayor_recaudacion(existencias, precios):
    recaudaciones = recaudacion_por_deposito(existencias, precios)

    maxima_recaudacion = 0
    deposito_maximo = ""

    for provincia in recaudaciones: recaudacion = recaudaciones[provincia]

    if recaudacion > maxima_recaudacion:
        maxima_recaudacion = recaudacion
        deposito_maximo = provincia

        return deposito_maximo, maxima_recaudacion

def contar_depositos_excedidos (existencias, Max = 50000):
    provincias_excedidas = []
    conteo_por_provincia = {}

    for fila in existencias:
        provincia = fila[0]
        cantidad = fila [2]

    if provincia in conteo_por_provincia:
        conteo_por_provincia [provincia] += [cantidad]
    else:
            conteo_por_provincia[provincia] = cantidad

    provincias = []

    for provincia in conteo_por_provincia:
        for i in range(len(provincias)):
            provincia = provincias [i]
            total = conteo_por_provincia [provincia]
        
        if total > Max:
            provincias_excedidas += [provincia]

        return provincias_excedidas
    
    
    
