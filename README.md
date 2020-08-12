# Prueba universo de Star Wars
A continuación una corta descriptión del contenido de la prueba y su instalación

## Estructura

El sistema contiene 3 aplicaciones correspondientes a los planetas, personajes y películas de Star Wars

1. Aplicación de planetas: se encarga de crear las consultas y las mutaciones de los planetas de Star Wars
2. Aplicación de personajes: se encarga de crear las consultas y las mutaciones de los personajes de Star Wars
3. Aplicación de películas: se encarga de crear las consultas y las mutaciones de las películas de Star Wars

Las peliculas tienen una relación de muchos a muchos con los planetas y los personajes por lo que es necesario que exitan almenos uno de cada uno. Y por parte de los personajes tambien se tiene como llave foranea el planeta al que pertence cada uno de ellos.

## Instalación

Para el creación se utilizo **pipenv** para manejar el entorno de desarrollo por lo que las instrucciones a continuación se haran bajo esta herramienta.

1. Para crear el entorno de desarrollo es el siguiente comando -> `~/star-wars$ pipenv shell`. Antes de realizar este paso debe estar ubicado en el dorectorio raiz del proyecto.
2. Navegar a la aplicación principal llamada ***starwars*** y enseguida se realiza la instalación de los modulos con -> `~/star-wars/starwars$ pipenv install -r requeriments.txt`. De esta manera se hace la instalación a partir del archivo requirements que contiene las versiones utilizadas en el desarrollo.
3. Para inicializar la base de datos usamos los siguientes comandos ->
   - `~/star-wars/starwars$ python manage.py makemigrations`.
   - `~/star-wars/starwars$ python manage.py migrate`.
4. Si se desea realizar la carga de los datos iniciales que se encuentran en la carpeta fixtures -> `~/star-wars/starwars$ python ./manage.py loaddata fixtures/file.json` .
5. Para su ejecución es posible utilizar la _shell_ llamada ***run.sh*** -> `~/star-wars/starwars$ . run.sh` .
6. Para ingresar al consola de graphql -> _http://localhost:8000/graphql_.

## Pruebas unitarias

Para realizar las pruebas correspondientes a cada aplicación se ejecutan los siguientes comandos.

- `~/star-wars/starwars$ python manage.py test applications/planet/test/tests.py -s`
- `~/star-wars/starwars$ python manage.py test applications/person/test/tests.py -s`
- `~/star-wars/starwars$ python manage.py test applications/film/test/tests.py -s`

<br>

---

### Ejemplo Output

```bash
~/star-wars/starwars$ python manage.py test applications/person/test/tests.py -s
nosetests applications/planet/test/tests.py -s --verbosity=1
Creating test database for alias 'default'...
Resultado Mutation {'data': OrderedDict([('createPlanet', {'planet': {'name': 'test'}})])}
.Resultado Query {'data': {'planets': {'edges': [{'node': {'name': 'Tatooine', 'terrain': 'dessert', 'climate': 'arid', 'population': '200000'}}]}}}
.
----------------------------------------------------------------------
Ran 2 tests in 0.010s

OK
```

---
