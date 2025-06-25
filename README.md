# Trabajo Integrador – Árboles Binarios en Python

Este proyecto implementa un árbol binario en Python utilizando únicamente listas, sin clases ni objetos. La idea es representar la estructura de forma simple para enfocarnos en la lógica del árbol y sus recorridos. Permite crear un árbol, insertar nodos, visualizarlo rotado en consola y recorrerlo en diferentes órdenes.

---

## Marco teórico (resumen)

Un árbol binario es una estructura jerárquica donde cada nodo puede tener hasta dos hijos: izquierdo y derecho. Se utilizan en algoritmos de búsqueda, bases de datos, inteligencia artificial, sistemas de archivos, entre otros. En este trabajo usamos listas anidadas para construir nodos del tipo:


Esto permite trabajar sin clases, enfocándonos en la recursividad y la estructura.

---

## Funcionalidades implementadas

- `crear_arbol(valor)`  
- `insertar_izquierda(nodo, valor)`  
- `insertar_derecha(nodo, valor)`  
- `recorrido_preorden(nodo)`  
- `recorrido_inorden(nodo)`  
- `recorrido_postorden(nodo)`  
- `imprimir_arbol(nodo)` → muestra el árbol rotado 90° en consola  
- `altura(nodo)` → calcula la altura del árbol  
- `contar_nodos(nodo)` → cuenta la cantidad total de nodos  
- `buscar_valor(nodo, valor)` → busca un valor en el árbol  
- `mostrar_hojas(nodo)` → imprime los nodos hoja (sin hijos)

---

## Archivos incluidos

- `arbol_listas.py`: código fuente con comentarios

- `Trabajo_Integrador_Arboles`.pdf: informe completo del trabajo

- `video_youtube.txt`: link de video explicativo del proyecto

---

## Autores

- `Kenyi Meza` – mezakenyi@gmail.com
- `Roberto Méndez` – robermen02@gmail.com

---

## Cátedra

- `Materia`: Programación I

- `Comisión`: 17

- `Docente`: Julieta Agustina Trapé

- `Carrera`: Tecnicatura Universitaria en Programación (UTN)

---

## Fuentes consultadas

- Python Software Foundation. (2024). Python 3 Documentation

- Cormen, T., Leiserson, C., Rivest, R., & Stein, C. (2009). Introduction to Algorithms

- Material de clase: presentación “Implementación de Árboles en Python utilizando listas”

- YouTube: Árboles binarios en Python – Tutorial de apoyo