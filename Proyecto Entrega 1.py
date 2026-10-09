"""

División de Trabajo:
Integrante 1:
Hace el esqueleto del archivo, se encargar de la carga y el provcesamiento del archivo scv.
Integrante 2:
Se encarga de el desarrollo de la primera función obligatoria. 
Integrante 3:
Se encarga de el desarrolllo de la segunda función obligatoria.
Integrante 4:
Define y desarrolla la función opcional para el código.
Integrante 5:
Desarrolla dos funciones del código propias para completar y tenere el requerimiento minimo a sustentar en el proyecto
también se encarga del entregable en donde explicamos y desarrollamos la división de roles.
Integrante 6:
Desarrolla el video desmostrativo y el read.me del proyecto.
"""

def cargar_archivo(ruta_documento):
    """
    Guía para usarlo:
    Lee el archivo CSV utilizando la función nativa open() y procesa cada línea con el método .split(',').

    Parámetros:
        ruta_documento: Ruta del archivo csv con los 50 registros iniciales

    Retorna:
        tupla: (nombres_columna, fila_):
            -nombres_columna: lista con los nombres de las columnas    
            -fila_#: Listas de listas donde contempla las filas y sus valores
    """

    #inciar tuplas
    #hacer el open
    #sino esta vacion recorrer y llenar las tuplas
    #retornar las tuplas

    columnas = []
    filas = []

    with open(ruta_documento, mode='r', encoding='utf-8') as f:#Invoca el gestor de contexto en modo lectura, soportando caracteres especiales y tildes
        Lineas = f.readlines()#Lee la totalidad del archivo
        if len(Lineas) > 0:#Verifica si la lista tiene archivos
            columnas = Lineas[0].strip().split(',')# hagarra los encabezados y los guarda limpios

            for Linea in Lineas[1:]:#itera toda la lista
                Linea_nueva = Linea.strip()#Limpia la linea
                if Linea_nueva:#verifica si esta vacia
                    arreglo_filas = Linea_nueva.split(',')#Divide toda la fila en un arreglo
                    filas.append(arreglo_filas)#los agrega a la lista previamente creada
    return columnas, filas

def cargar_menu():

    print("\n" + "="*55)
    print("   DATALAB - EXPLORADOR DE GOLES DEL MUNDIAL   ")
    print("="*55)
    print("1. Buscar registros por texto (Texto)")
    print("2. Ver estadísticas básicas del minuto de los goles")
    print("3. Agrupar goles por Selección (Categoría)")
    print("4. Analizar criterios del 'Mejor Equipo de la Historia'")
    print("5. Salir")
    print("="*55)

def ejecutar_code():
    Data_set = "goals.csv"
    try:# intenta realizar la acción y si dispara un error manda el except
        columnas, filas = cargar_archivo(Data_set)
        print(f" Dataset cargado exitosamente: {len(filas)} registros cargados.")
    except FileNotFoundError:# si no puede abrir el archivo dispara esto
        print(f" Error: No se encontró el archivo '{Data_set}'. Verifique la ruta.")
        return
    
    while True:# inicia el while para siempre hasta que usen el breka
        cargar_menu()
        opcion = input(" Seleccione una opción (1-5): ").strip()
            
        if opcion == "1":
            print("\n--- BÚSQUEDA POR TEXTO ---")
                    
        elif opcion == "2":
            print("\n--- ESTADÍSTICAS BÁSICAS DEL MINUTO DE REGULACIÓN ---")

                    
        elif opcion == "3":
            print("\n--- AGRUPACIÓN POR SELECCIÓN (CATEGORÍA) ---")

        elif opcion == "4":
            print("\n--- ANÁLISIS CRITERIOS MEJOR EQUIPO DE LA HISTORIA ---")
            
        elif opcion == "5":
            print("\n Saliendo del sistema DataLab. ¡Hasta luego!")
            break
        else:
            print(" Opción no válida. Por favor, ingrese un número del 1 al 5.")
    
ejecutar_code()