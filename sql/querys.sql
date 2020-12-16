<<<<<<< HEAD
/* 9 Querys hechas */
=======
>>>>>>> origin/main
-- 1 Mostrar la Carta inicial más repetida por cada jugador. (mostrar nombre jugador y carta)
SELECT u.username, t.carta_inicial FROM usuario u
INNER JOIN participante p ON p.id_participante=u.idusuario
INNER JOIN turnos t ON t.idparticipante=p.id_participante
GROUP BY username;

-- 2 Jugador que realiza la apuesta más alta por partida. (Mostrar nombre jugador)
SELECT nombre,MAX(apuesta),idpartida
FROM
(
SELECT
CASE
WHEN username IS NOT NULL THEN usuario.username
ELSE descripcion
END
AS nombre,MAX(turnos.apuesta) AS apuesta,partida.idpartida AS idpartida FROM jugador
LEFT JOIN bot ON bot.idbot=jugador.idbot
LEFT JOIN usuario ON usuario.idusuario=jugador.idusuario
INNER JOIN participante ON jugador.idjugador=participante.id_jugador
INNER JOIN turnos ON participante.id_participante=turnos.idparticipante
INNER JOIN partida ON turnos.idpartida=partida.idpartida
WHERE turnos.apuesta IS NOT NULL
GROUP BY partida.idpartida,username
) tabla
WHERE (apuesta,idpartida) IN
(
SELECT
MAX(turnos.apuesta),partida.idpartida  AS apuesta from jugador
LEFT JOIN bot ON bot.idbot=jugador.idbot
LEFT JOIN usuario ON usuario.idusuario=jugador.idusuario
INNER JOIN participante ON jugador.idjugador=participante.id_jugador
INNER JOIN turnos ON participante.id_participante=turnos.idparticipante
INNER JOIN partida ON turnos.idpartida=partida.idpartida
GROUP BY partida.idpartida
ORDER BY MAX(turnos.apuesta) DESC
)
GROUP BY idpartida limit 5;

-- 3 Jugador que realiza apuesta más baja por partida. (Mostrar nombre jugador)
SELECT nombre,MIN(apuesta),idpartida
FROM
(
SELECT
CASE
WHEN username IS NOT NULL THEN usuario.username
ELSE descripcion
END
AS nombre,MIN(turnos.apuesta) AS apuesta,partida.idpartida AS idpartida FROM jugador
LEFT JOIN bot ON bot.idbot=jugador.idbot
LEFT JOIN usuario ON usuario.idusuario=jugador.idusuario
INNER JOIN participante ON jugador.idjugador=participante.id_jugador
INNER JOIN turnos ON participante.id_participante=turnos.idparticipante
INNER JOIN partida ON turnos.idpartida=partida.idpartida
WHERE turnos.apuesta IS NOT NULL
GROUP BY partida.idpartida,username
) tabla
WHERE (apuesta,idpartida) IN
(
SELECT
MIN(turnos.apuesta),partida.idpartida  AS apuesta FROM jugador
LEFT JOIN bot ON bot.idbot=jugador.idbot
LEFT JOIN usuario ON usuario.idusuario=jugador.idusuario
INNER JOIN participante ON jugador.idjugador=participante.id_jugador
INNER JOIN turnos ON participante.id_participante=turnos.idparticipante
INNER JOIN partida ON turnos.idpartida=partida.idpartida
GROUP BY partida.idpartida
ORDER BY MIN(turnos.apuesta) DESC
)
GROUP BY idpartida LIMIT 5;

-- 4 Ratio  de turnos ganados por jugador en cada partida (%),mostrar columna Nombre jugador, Nombre partida, nueva columna 'porcentaje %'.

-- 5 Porcentaje de partidas ganadas Bots en general. Nueva columna 'porcentaje %'.

-- 6 Mostrar los datos de los jugadores y el tiempo que han durado sus partidas ganadas cuya puntuación obtenida es mayor que la media puntos de las partidas ganadas totales.


-- 7 Cuántas rondas se ganan en cada partida según el palo. Ejemplo: Partida 1 - 5 rondas - Bastos como carta inicial.
SELECT numero_turno, idpartida, tipo FROM turnos
INNER JOIN cartas ON turnos.carta_inicial=cartas.numero_carta
WHERE resultado = 'gana turno'
GROUP BY idpartida;

-- 8 Cuantas rondas gana la banca en cada partida.
SELECT numero_turno, idpartida FROM turnos
WHERE resultado = 'gana turno' and es_banca = 1
GROUP BY idpartida;

-- 9 Cuántos usuarios han sido la banca en cada partida
SELECT COUNT(es_banca), idpartida FROM turnos
WHERE es_banca=1
GROUP BY idpartida;

-- 10 Partida con la puntuación más alta final de todos los jugadores, mostrar nombre jugador, nombre partida,así como añadir una columna nueva en la que diga si ha ganado la partida o no.

-- 11 Calcular la apuesta media por partida.
SELECT AVG(apuesta), idpartida FROM turnos
GROUP BY idpartida;

-- 12 Mostrar los datos de los usuarios que no son bot, así como cual ha sido su última apuesta en cada partida que ha jugado.
SELECT *,(
SELECT MAX(apuesta) FROM turnos
GROUP BY idpartida
ORDER BY idpartida DESC LIMIT 1
) AS ultima_apuesta
FROM usuario;

-- 13 Calcular el valor total de las cartas y el numero total de cartas que se han dado inicialmente en las manos en la partida. Por ejemplo, en la partida se han dado 50 cartas y el valor total de las cartas es 47,5.
SELECT COUNT(carta_inicial) AS total, idpartida ,(
SELECT SUM(valor) FROM cartas c
WHERE t.idturnos=cartas.idcartas
) AS valor_total
FROM turnos t
GROUP BY idpartida;

-- 14 Diferencia de puntos de los participantes de las partidas entre la ronda 1 y 5. Ejemplo: Rafa tenia 20 puntos, en la ronda 5 tiene 15, tiene -5 puntos de diferencia.


