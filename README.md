## Proyecto Siete y medio
El siete y medio es un juego de cartas que utiliza la baraja española de 40 cartas. El juego consiste en obtener siete puntos y medio, o acercarse a esta puntuación lo másposible. Las cartas tienen, indistintamente de su palo, el valor que indica su propioíndice, excepto las figuras (sota, caballo y rey) que tienen una valor de medio punto cada una. El objetivo es ganar los puntos apostados en cada tanda. En cada apuesta, cada jugador compite contra la banca, para ganar la apuesta el objetivo es intentar sumar siete y medio o el número más cercano sin pasarse de esta cantidad.

### Tabla de Contenidos
- [Resumen](#resumen)
- [Requerimientos](#requerimientos)
- [Instalacion](#instalacion)
- [Configuration](#configuration)
- [Contacto](#contacto)

### Resumen
- El número de jugadores debe estar entre 2 y 8.
- Se jugará un máximo de 30 manos.
- Cada jugador inicia la partida con 20 puntos.
- El programa reparte una carta a cada jugador. A partir de aquí, cada jugador realiza dos acciones:
  * En primer lugar, escoge cuantos puntos apuesta en esta jugada. 
  * En segundo lugar, decide si quiere recibir más cartas del mazo. Si noquiere más cartas, se planta. Puede pedir tantas cartas del mazo comocrea conveniente y se puede plantar cuando quiera.
- Cuando todos han acabado de escoger cartas, juega la banca, si la banca no sepasa, se compara la puntuación de la banca con la de cada jugador. 
  * Si el jugador tiene igual puntos de puntos o menos que la banca, paga lo apostado a la banca.
  * Si el jugador se ha pasado, igualmente paga lo apostado a la banca.
  * Si el jugador tiene siete y medio y la banca no, gana el doble de lo apostado. 
  * En caso de no tener siete y medio pero tener más puntos que la banca, la bancale paga lo apostado.
  * Si la banca se pasa, pagará a todos los jugadores que no se hayan pasado, lo que hayan apostado.
- El jugador que pierde todos sus puntos, queda eliminado de la partida.
- El jugador ganador es el que más puntos ha obtenido después de todas las partidas jugadas.

### Requerimientos
- python3
- git

<a name="instalacion"></a>
### Instalacion

```
$ git clone git://github.com/AlexDltg/proyecto_1_siete_y_medio.git
$ cd proyecto_1_siete_y_medio
```
##### Linux
```
$ ./run.sh
```
##### Windows
```
$ ./run.bat
```

### Configuration
- `Basic_Config_Game.xml`:  contiene la configuracion basica de la partida.
```
<Num_Min_Players>2</Num_Min_Players>
<Num_Max_Players>8</Num_Max_Players>
<Num_Max_Rounds>30</Num_Max_Rounds>
<Num_Initial_Points>20</Num_Initial_Points>
<Is_Allowed_Auto_Mode>True</Is_Allowed_Auto_Mode>
```
- `Cartas.xml`: contiene la informacion de las cartas 
```
<codigo>1</codigo>
<valor>1</valor>
<palo>Oros</palo>
<valor_juego>1</valor_juego>
<activa>SI</activa>
```

### Contacto
- AlexDltg: dltgalex@gmail.com
- MourinRaul: 
- dcabrerairache: 

