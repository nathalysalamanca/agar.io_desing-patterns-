# Implementación AGAR.IO  Grupo 6

> Ingry Nathaly Salamanca Rativa

> Julio Cesar Morales Torres

> Elkin Ortiz Salazar

Implementación del juego AGAR.IO en python utilizando los patrones de diseño de software Object Pool, Builder y Observer para implementación según diagrama

![](imágenes/header.png)

## Object Pool y Builder
```sh
La asignación de memoria de los videojuegos es un tema fundamental porque tiene un impacto en el rendimiento y determina la rapidez 
con la que el usuario lo percibe. Hardware como teléfonos móviles y tabletas tienen recursos limitados en comparación con una PC y 
en algunos casos,se debe evaluar si la gestión que brinda el lenguaje de programación es adecuada para nuestros objetivos.

Por ejemplo, si estamos en las siguientes condiciones:debes asignar y destruir cientos de miles de objetos durante el juego; los 
objetos tienen la misma naturaleza; en un período de tiempo dado, solo es necesario un número limitado de estos objetos.
Entonces puede ser útil organizar un número fijo de estos objetos, que llamaremos Object Pool, y en lugar de crearlos y 
destruirlos continuamente, simplemente los usamos y los volvemos a poner en el pool según sea necesario.

Un enfoque como este no solo aumenta el rendimiento porque no crea objetos cada vez, sino que también evita la fragmentación del 
Heap y la ejecucióncontinua del recolector de basura que podría provocar retrasos.

La administración de un grupo de objetos obviamente complica el código fuente y, por lo tanto, su capacidad de mantenimiento,
por lo que debe usarse si y solo si las 3 condiciones vistas arriba son verdaderas.

En nuestro caso AGAR.IO, requiere usar muchas instancias de los alimentos y virus constantemente, en los cuales se hace una 
destrucción cuando el alimento es comido por una celula y creación ya que los alimentos, así como son destruidos también son
creados en el transcurso del juego así que lo que buscamos optimizar con este patrón es que las instancias sean finitas  desde
el inicio del juego y cuando se ejecute la función alimentar por parte de una célula que representa un jugador, esa instancia
del alimento sea liberada para asignarle unas nuevas coordenadas y así no tener que crear unas nuevas optimizando el manejo
de memoria del dispositivo
Builder:
Es un patrón de diseño creacional, permite construir objetos complejos. El patrón nos permite 
producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.
Problema para solucionar:
En el juego se requieren crear objetos de tipo comida para que el jugador crezca en tamaño y virus para que el jugador se 
divida en partes, construirlos puede ser una tarea laboriosa dado que cada vez que se consuma un grupo de elementos se deben
crear nuevos objetos, de no usarse este patrón se deberá sobrecargar el constructor con n cantidad y parámetros para 
multiplicar los objetos.
Solución:
EL patrón Builder nos sugiere sacar el código de construcción del objetivo de su propia clase y segregarlos en constructores
independientes esto lo hacen por medio de una clase directora la cual escucha está pendiente de ciertos eventos o paso y 
cuando estos se cumpla, define la forma y el momento de comenzar la construcción de los nuevos objetos.
Para la construcción del AGARIO, el role de la clase directora lo ocupa la clase "Creador", este, se encargara de verificar 
la cantidad de existente en el lienzo de los objetos “food” y “virus”, y de la mano del patrón de diseño Pool; crear y reubicar
los objetos en el tablero "Lienzo".
```
![Object Pool and Builder](imágenes/object.png | width=100)
## Observer
```sh
Este patron de comportamiento permite definir un mecanismos de suscripcion para notificar varios objetos sobre
cualquier evento.
El problema a solucionar:
Consite en poder detectar cuando un nuevo jugador se conecta o inicia una partida, seria tedioso tanto para el servidor
como para el cliente estar enviando la solcitud de conexion y entregando la respesra de inicio de partida.
Solucion: 
En este caso, se crea un objeto notificador "event Game", quien tiene como funcion principal llevar el control de los 
jugadores que estan en juego y los puntajes, permitiendo a nuevos jugadores o a los jugadores actualaes llevar un control
independiente de su puntaje e informando el control de tiempo restante de la partida.

El patrón Observer sugiere que añadas un mecanismo de suscripción a la clase notificadora para que los objetos individuales
puedan suscribirse o cancelar su suscripción a un flujo de eventos que proviene de esa notificadora.
```
![](imágenes/observer.png)

## Entorno para Ejecución.
### Python versión 3.7.0 o superior
![](imágenes/python.png)
![](imágenes/pygame.png)
Windows:
```sh
verificación de configuración
```
![](imágenes/terminal1.png)
```sh
Instalación módulos Pygame para desarrollo de video juegos
```
![](imágenes/pygame1.png)
```sh
```
![](imágenes/pygame2.png)
```sh
Configuración del servidor
```
![](imágenes/terminal3.png)
```sh
Configuración cliente
```
![](imágenes/configuracion.png)
```sh
Inicio de partida
```
![](imágenes/terminal2.png)

```sh
```
![](imágenes/juego.png)

