# Creación de aplicación web flask + mariadb

Para la creación de una aplicación web, he realizado la siguiente configuración. Mi aplicación web, está en un entorno virtual, para que se ejecute con seguridad, y se ejecuta con python con el siguiente comando: 

<pre>
  python3 app.py 
</pre>

Para comprobar que accede a distintos usuarios y distintas bases de datos, he creado dos usuarios con sus respectivas bases de datos:

*Usuario estibaliz
contraseña: estibaliz
base de datos: musica
Usuario pepa
contraseña pepa
base de datos: series*

La sintaxis de configuración del usuario y base de datos “estibaliz” es la siguiente: 

### USUARIO ESTIBALIZ

<pre>
MariaDB [(none)]> CREATE USER 'estibaliz'@'localhost' IDENTIFIED BY 'estibaliz';
Query OK, 0 rows affected (0,007 sec)

MariaDB [(none)]> CREATE DATABASE musica;
Query OK, 1 row affected (0,001 sec)

MariaDB [(none)]> GRANT ALL PRIVILEGES ON musica.* TO 'estibaliz'@'localhost';
Query OK, 0 rows affected (0,002 sec)
</pre>

### CREACIÓN DE TABLAS

<pre>
  
CREATE TABLE cantantes (
    id_cantante INT(5) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50),
    fecha_nacimiento DATE NOT NULL,
    nacionalidad VARCHAR(50) NOT NULL,
    CONSTRAINT pk_cantantes PRIMARY KEY (id_cantante)
);


CREATE TABLE grupos (
    id_grupo INT(5) NOT NULL,
    nombre_grupo VARCHAR(50) NOT NULL,
    fecha_inicio INT(4) NOT NULL,
    pais_origen VARCHAR(50) NOT NULL,
    CONSTRAINT pk_grupos PRIMARY KEY (id_grupo)
);


CREATE TABLE canciones (
    id_cancion INT NOT NULL,
    id_grupo INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    anio_lanzamiento INT(4) NOT NULL,
    duracion_seg INT(4) NOT NULL,
    CONSTRAINT pk_canciones PRIMARY KEY (id_cancion)
);
</pre>

### INSERCIÓN DE DATOS
<pre>
INSERT INTO cantantes (id_cantante, nombre, apellido, fecha_nacimiento, nacionalidad) VALUES
(1, 'Freddie', 'Mercury', '1946-09-05', 'Británico'),
(2, 'Elvis', 'Presley', '1935-01-08', 'Estadounidense'),
(3, 'Michael', 'Jackson', '1958-08-29', 'Estadounidense'),
(4, 'Aretha', 'Franklin', '1942-03-25', 'Estadounidense'),
(5, 'David', 'Bowie', '1947-01-08', 'Británico'),
(6, 'Whitney', 'Houston', '1963-08-09', 'Estadounidense'),
(7, 'Prince', '', '1958-06-07', 'Estadounidense'),
(8, 'Madonna', '', '1958-08-16', 'Estadounidense'),
(9, 'Bob', 'Dylan', '1941-05-24', 'Estadounidense'),
(10, 'Stevie', 'Wonder', '1950-05-13', 'Estadounidense'),
(11, 'John', 'Lennon', '1940-10-09', 'Británico'),
(12, 'Paul', 'McCartney', '1942-06-18', 'Británico'),
(13, 'Beyoncé', '', '1981-09-04', 'Estadounidense'),
(14, 'Kurt', 'Cobain', '1967-02-20', 'Estadounidense'),
(15, 'Janis', 'Joplin', '1943-01-19', 'Estadounidense'),
(16, 'Jim', 'Morrison', '1943-12-08', 'Estadounidense'),
(17, 'Elton', 'John', '1947-03-25', 'Británico'),
(18, 'Adele', '', '1988-05-05', 'Británica'),
(19, 'Celine', 'Dion', '1968-03-30', 'Canadiense'),
(20, 'Mariah', 'Carey', '1969-03-27', 'Estadounidense');


INSERT INTO grupos (id_grupo, nombre_grupo, fecha_inicio, pais_origen) VALUES
(1, 'Queen', 1970, 'Reino Unido'),
(2, 'The Beatles', 1960, 'Reino Unido'),
(3, 'Nirvana', 1987, 'Estados Unidos'),
(4, 'ABBA', 1972, 'Suecia'),
(5, 'U2', 1976, 'Irlanda'),
(6, 'Led Zeppelin', 1968, 'Reino Unido'),
(7, 'Pink Floyd', 1965, 'Reino Unido'),
(8, 'The Rolling Stones', 1962, 'Reino Unido'),
(9, 'Backstreet Boys', 1993, 'Estados Unidos'),
(10, 'Spice Girls', 1994, 'Reino Unido'),
(11, 'Metallica', 1981, 'Estados Unidos'),
(12, 'Imagine Dragons', 2008, 'Estados Unidos'),
(13, 'Coldplay', 1996, 'Reino Unido'),
(14, 'Red Hot Chili Peppers', 1983, 'Estados Unidos'),
(15, 'Genesis', 1967, 'Reino Unido'),
(16, 'The Doors', 1965, 'Estados Unidos'),
(17, 'Fleetwood Mac', 1967, 'Reino Unido'),
(18, 'Eagles', 1971, 'Estados Unidos'),
(19, 'Oasis', 1991, 'Reino Unido'),
(20, 'The Police', 1977, 'Reino Unido');


INSERT INTO canciones (id_cancion, id_grupo, titulo, anio_lanzamiento, duracion_seg) VALUES
(1, 1, 'Bohemian Rhapsody', 1975, 354),
(2, 1, 'We Will Rock You', 1977, 122),
(3, 2, 'Hey Jude', 1968, 431),
(4, 2, 'Let It Be', 1970, 243),
(5, 3, 'Smells Like Teen Spirit', 1991, 301),
(6, 4, 'Dancing Queen', 1976, 230),
(7, 5, 'With or Without You', 1987, 295),
(8, 6, 'Stairway to Heaven', 1971, 482),
(9, 7, 'Comfortably Numb', 1979, 384),
(10, 8, '(I Can\'t Get No) Satisfaction', 1965, 222),
(11, 9, 'I Want It That Way', 1999, 213),
(12, 10, 'Wannabe', 1996, 172),
(13, 11, 'Enter Sandman', 1991, 331),
(14, 12, 'Radioactive', 2012, 186),
(15, 13, 'Yellow', 2000, 269),
(16, 14, 'Californication', 1999, 330),
(17, 15, 'Invisible Touch', 1986, 235),
(18, 16, 'Light My Fire', 1967, 420),
(19, 17, 'Go Your Own Way', 1976, 217),
(20, 18, 'Hotel California', 1976, 390);
</pre>

### USUARIO PEPA
<pre>
MariaDB [(none)]> CREATE USER 'pepa'@'localhost' IDENTIFIED BY 'pepa';
Query OK, 0 rows affected (0,003 sec)
MariaDB [(none)]> CREATE DATABASE series;
Query OK, 1 row affected (0,001 sec)
MariaDB [(none)]> GRANT ALL PRIVILEGES ON series.* TO 'pepa'@'localhost';
Query OK, 0 rows affected (0,003 sec)
</pre>

### CREACIÓN DE TABLAS
<pre> 
CREATE TABLE series (
id_serie INT(11),
nombre_serie VARCHAR(100) NOT NULL,
anio_inicio INT(11) NOT NULL,
CONSTRAINT pk_series PRIMARY KEY (id_serie)
);

CREATE TABLE personajes (
id_personaje INT(11),
id_serie INT(11),
nombre_personaje VARCHAR(100) NOT NULL,
CONSTRAINT pk_personajes PRIMARY KEY (id_personaje),
CONSTRAINT fk_series FOREIGN KEY (id_serie) REFERENCES series(id_serie)
);

CREATE TABLE actores (
id_actor INT(11),
id_personaje INT(11),
nombre_actor VARCHAR(100) NOT NULL,
CONSTRAINT pk_actores PRIMARY KEY (id_actor),
CONSTRAINT fk_personajes FOREIGN KEY (id_personaje) REFERENCES personajes(id_personaje)
);
</pre>

### INSERCIÓN DE DATOS

<pre>
INSERT INTO series (id_serie, nombre_serie, anio_inicio) VALUES
(1, 'Los Serrano', 2003),
(2, 'Aída', 2005),
(3, 'Física o Química', 2008),
(4, 'El Internado', 2007),
(5, 'Hospital Central', 2000),
(6, 'Águila Roja', 2009),
(7, 'Cuéntame cómo pasó', 2001),
(8, 'Los Misterios de Laura', 2009);
INSERT INTO personajes (id_personaje, id_serie, nombre_personaje) VALUES
(1, 1, 'Diego Serrano'),
(2, 2, 'Aída Recacha'),
(3, 3, 'Héctor Ocaña'),
(4, 4, 'Marcos Novoa'),
(5, 5, 'Macarena Fernández'),
(6, 6, 'Gonzalo de Montalvo'),
(7, 7, 'Carlos Alcántara'),
(8, 8, 'Laura Lebrel');

INSERT INTO actores (id_actor, id_personaje, nombre_actor) VALUES
(1, 1, 'Antonio Resines'),
(2, 2, 'Carmen Machi'),
(3, 3, 'Marc Clotet'),
(4, 4, 'Yon González'),
(5, 5, 'Patricia Vico'),
(6, 6, 'David Janer'),
(7, 7, 'Ricardo Gómez'),
(8, 8, 'María Pujalte');

</pre>

Cuando ejecutamos el fichero, estando dentro del entorno virtual: 

<pre>
  python3 app.py
</pre>
 Nos aparece la siguiente interfaz: 
<img width="1244" height="384" alt="imagen" src="https://github.com/user-attachments/assets/f039b1c3-fbd7-4fea-b690-164650cee1f4" />

En ella, tenemos la posibilidad de entrar con el usuario pepa o estibaliz, y la base de datos música o series. 
Si por ejemplo, queremos entrar con la base de datos musica, y el usuario estíbaliz: 

# USUARIO ESTIBALIZ Y BASE DE DATOS MUSICA

<img width="1245" height="415" alt="imagen" src="https://github.com/user-attachments/assets/baa23b98-2a09-473f-b444-1d4c5c88daf9" />

Nos van a aparecer 4 tablas, y si pulsamos en cada una de ellas, aparecen los registros de cada tabla: 

## CANCIONES: 
<img width="1247" height="706" alt="imagen" src="https://github.com/user-attachments/assets/ceaff09e-b34f-4138-b804-be4b6ed418ea" />

## CANTANTES: 
<img width="1513" height="767" alt="imagen" src="https://github.com/user-attachments/assets/1e127731-fdea-4e7c-8afb-705b13026b02" />

## GRUPOS:
<img width="1513" height="767" alt="imagen" src="https://github.com/user-attachments/assets/fac6e56b-79c2-4bd9-84ea-2820c1b4fdc6" />

# USUARIO PEPA Y BASE DE DATOS SERIES

<img width="1276" height="424" alt="imagen" src="https://github.com/user-attachments/assets/2705d10b-e38f-458c-a31d-ea1d4f9ce431" />

## ACTORES:

<img width="1281" height="581" alt="imagen" src="https://github.com/user-attachments/assets/344cc167-0c04-4571-a3bc-24d3f9f22da3" />

## PERSONAJES:

<img width="1281" height="581" alt="imagen" src="https://github.com/user-attachments/assets/97533be3-eab8-4ae7-81a0-38b9efadc089" />

## SERIES:
<img width="1287" height="618" alt="imagen" src="https://github.com/user-attachments/assets/db97f59c-0080-44a5-9e9b-de63b0eb7c52" />
