# Trabajo Integrador – Árboles Binarios en Python

Este proyecto implementa un árbol binario en Python utilizando únicamente listas, sin clases ni objetos. La idea es representar la estructura de forma simple para enfocarnos en la lógica del árbol y sus recorridos. Permite crear un árbol, insertar nodos, visualizarlo rotado en consola y recorrerlo en diferentes órdenes.

---

## Marco teórico (resumen)

Un árbol binario es una estructura jerárquica donde cada nodo puede tener hasta dos hijos: izquierdo y derecho. Se utilizan en algoritmos de búsqueda, bases de datos, inteligencia artificial, sistemas de archivos, entre otros. En este trabajo usamos listas anidadas, esto permite trabajar sin clases, enfocándonos en la recursividad y la estructura.

---

## Funcionalidades implementadas

- `crear_arbol(valor)`  
  Crea un nuevo nodo raíz con el valor dado y sin hijos.

- `insertar_izquierda(nodo, valor)`  
  Inserta un nuevo nodo como hijo izquierdo del nodo actual. Si ya había uno, lo desplaza hacia abajo.

- `insertar_derecha(nodo, valor)`  
  Inserta un nuevo nodo como hijo derecho. Si ya existe, también lo reubica como hijo del nuevo nodo.

- `recorrido_preorden(nodo)`  
  Muestra los valores del árbol recorriéndolo desde la raíz, luego por la izquierda, y por último por la derecha.

- `recorrido_inorden(nodo)`  
  Recorre el árbol en el orden: izquierda → nodo actual → derecha. Útil para árboles binarios de búsqueda.

- `recorrido_postorden(nodo)`  
  Visita primero los subárboles izquierdo y derecho, y al final el nodo actual.

- `imprimir_arbol(nodo)`  
  Muestra el árbol rotado 90° hacia la izquierda en consola. Ayuda a visualizar jerarquías.

- `altura(nodo)`  
  Devuelve la altura máxima del árbol, es decir, el número de niveles.

- `contar_nodos(nodo)`  
  Cuenta cuántos nodos (elementos) tiene todo el árbol.

- `buscar_valor(nodo, valor)`  
  Busca un valor dentro del árbol y devuelve `True` si lo encuentra.

- `mostrar_hojas(nodo)`  
  Muestra todos los nodos que no tienen hijos, también llamados hojas.

---

## Archivos incluidos

- `arbol_listas.py`: código fuente con comentarios

- `Trabajo_Integrador_Arboles.pdf`: informe completo del trabajo

- `video_youtube.txt`: link de video explicativo del proyecto 
   (https://youtu.be/77-jTl_vkk8)

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