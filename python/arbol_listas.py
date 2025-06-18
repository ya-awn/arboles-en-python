# Esta funcion crea un nuevo arbol con un nodo principal (raiz)
# El nodo es una lista con el valor y dos lugares vacios para los hijos izquierdo y derecho
def crear_arbol(valor):
    return [valor, [], []]

# Esta funcion agrega un nodo a la izquierda del nodo actual
# Si ya hay algo a la izquierda, lo baja un nivel y pone el nuevo nodo arriba
def insertar_izquierda(nodo, valor):
    if nodo[1]:
        nodo[1] = [valor, nodo[1], []]
    else:
        nodo[1] = [valor, [], []]

# Esta funcion hace lo mismo que la anterior pero para el lado derecho
def insertar_derecha(nodo, valor):
    if nodo[2]:
        nodo[2] = [valor, [], nodo[2]]
    else:
        nodo[2] = [valor, [], []]
    
# Esta funcion elimina un nodo (referenciado por su valor[clave]) dentro de un arbol especifico
# Maneja tres casos: 
# 1 - Nodo es hoja: Se devuelve una lista vacia.
# 2 - Nodo tiene hijo izq: El nodo a eliminar se reemplaza por su hijo/rama izquierdo.
# 3 - Nodo tiene hijo der: El nodo a eliminar se reemplaza por su hijo/rama derecho.
# 4 - Nodo tiene dos hijos: Se reemplaza el nodo padre por su hijo izquierdo y se conecta el hijo 
#     derecho (ahora huerfano) al hijo mas hacia la derecha del "ex" hijo izquierdo (nuevo padre).

def eliminar_nodo(arbol, valor):
    if not arbol:
        return []
    
    if arbol[0] == valor:
        # Caso 1 - "Nodo es hoja"
        if not arbol[1] and not arbol[2]:
            return []
        # Caso 2 - "Nodo tiene hijo izquierdo."
        elif arbol[1] and not arbol[2]:
            return arbol[1]
        # Caso 3 - "Nodo tiene hijo derecho."
        elif not arbol[1] and arbol[2]:
            return arbol[2]
        # Caso 4 - "Nodo tiene dos pibes, caos."
        else:
            hijo_izq = arbol[1]
            hijo_der = arbol[2]
            
            # Se reemplaza el nodo padre por su hijo izquierdo *
            actual = hijo_izq
            
            # Se busca al hijo mas hacia la derecha del "ex" hijo izquierdo (nuevo padre). *
            while actual[2]:
                actual = actual[2]
            # Se conecta el hijo derecho al subarbol u hoja mas hacia la derecha encontrada en las lineas anteriores. *
            actual[2] = hijo_der
            
            return hijo_izq
    
    # Búsqueda recursiva
    arbol[1] = eliminar_nodo(arbol[1], valor)
    arbol[2] = eliminar_nodo(arbol[2], valor)
    return arbol
            
# Recorre el arbol en preorden: primero muestra el nodo, despues va a la izquierda y despues a la derecha
def recorrido_preorden(nodo):
    if nodo:
        print(nodo[0], end=' ')
        recorrido_preorden(nodo[1])
        recorrido_preorden(nodo[2])

# Recorre el arbol en inorden: primero va a la izquierda, luego muestra el nodo, y despues va a la derecha
def recorrido_inorden(nodo):
    if nodo:
        recorrido_inorden(nodo[1])
        print(nodo[0], end=' ')
        recorrido_inorden(nodo[2])

# Recorre el arbol en postorden: primero izquierda, luego derecha, y al final el nodo
def recorrido_postorden(nodo):
    if nodo:
        recorrido_postorden(nodo[1])
        recorrido_postorden(nodo[2])
        print(nodo[0], end=' ')

# Esta funcion muestra el arbol rotado 90 grados hacia la izquierda
def imprimir_arbol(nodo, nivel=0):
    if nodo:
        imprimir_arbol(nodo[2], nivel + 1)
        print('   ' * nivel + str(nodo[0]))
        imprimir_arbol(nodo[1], nivel + 1)

#Esta funcion busca un valor en el arbol
def buscar_valor(nodo, valor):
    if not nodo:
        return False
    if nodo[0] == valor:
        return True
    return buscar_valor(nodo[1], valor) or buscar_valor(nodo[2], valor)

#Esta funcion busca calcular la altura del arbol
def altura(nodo):
    if not nodo:
        return 0
    return 1 + max(altura(nodo[1]), altura(nodo[2]))

#Esta funcion cuenta la cantidad total de nodos
def contar_nodos(nodo):
    if not nodo:
        return 0
    return 1 + contar_nodos(nodo[1]) + contar_nodos(nodo[2])

#Esta funcion cuenta solo los nodos hoja
def mostrar_hojas(nodo):
    if nodo:
        if not nodo[1] and not nodo[2]:
            print(nodo[0], end=' ')
        mostrar_hojas(nodo[1])
        mostrar_hojas(nodo[2])


# aca armamos el arbol y probamos las funciones
if __name__ == "__main__":
    # Creamos el nodo raiz con valor 'A'
    arbol = crear_arbol('A')

    # Agregamos hijos a izquierda y derecha
    insertar_izquierda(arbol, 'B')
    insertar_derecha(arbol, 'C')

    # Agregamos nodos al segundo nivel
    insertar_izquierda(arbol[1], 'D')
    insertar_derecha(arbol[1], 'E')
    insertar_izquierda(arbol[2], 'F')
    insertar_derecha(arbol[2], 'G')

    # Mostramos los recorridos
    print("Recorrido Preorden:")
    recorrido_preorden(arbol)

    print("\nRecorrido Inorden:")
    recorrido_inorden(arbol)

    print("\nRecorrido Postorden:")
    recorrido_postorden(arbol)

    # Mostramos el arbol rotado
    print("\n\nVisualizacion del arbol rotado:")
    imprimir_arbol(arbol)

    #Mostramos la altura
    print("\n\nAltura del árbol:", altura(arbol))

    #Mostramos el total de nodos
    print("Cantidad total de nodos:", contar_nodos(arbol))   

    #Mostramos la busqueda de un nodo
    print("¿Existe el nodo 'E'?:", buscar_valor(arbol, 'E'))

    #Mostramos los nodo hoja
    print("Nodos hoja:", end=' ')
    mostrar_hojas(arbol)
    
    print("\n\nEliminando 'B':")
    arbol = eliminar_nodo(arbol, 'B')
    imprimir_arbol(arbol)
    
    
    # Caso práctico: Chat de diagnostico simple.
    print("\n\n---- ÁRBOL DE DIAGNÓSTICO ----")

    # Creamos el nodo raíz con la primera pregunta
    diagnostico = crear_arbol("¿Tenés fiebre?")

    # Rama izquierda = sí
    insertar_izquierda(diagnostico, "¿Tenés dolor muscular?")
    insertar_izquierda(diagnostico[1], "Parece una gripe")
    insertar_derecha(diagnostico[1], "Parece un resfrío")

    # Rama derecha = no
    insertar_derecha(diagnostico, "¿Tenés congestión nasal?")
    insertar_izquierda(diagnostico[2], "Parece un resfrío")
    insertar_derecha(diagnostico[2], "Estás bien")
    
    # Ejecutamos el "chat" de diagnostico
    def diagnosticar(nodo):
        while nodo:
            pregunta = nodo[0]
            if not nodo[1] and not nodo[2]: # Cuando el nodo/rama es un hoja:
                # Mostramos el diagnostico final
                print("Diagnóstico:", pregunta)
                return
            respuesta = input(f"{pregunta} (sí/no): ").strip().lower()
            # Evaluamos respuesta del usuario con una validacion basica
            if respuesta in ["sí", "si"]:
                nodo = nodo[1]
            else:
                nodo = nodo[2]
                
    diagnosticar(diagnostico)

    print()
