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

    print()
