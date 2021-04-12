#!/usr/bin/env python
# coding: utf-8

# In[15]:


import json
with open('movies.json', encoding='utf-8') as movies_file:
    movies = json.load(movies_file)  ##se encuentra en carpeta A1


# In[16]:


class Pelicula:
    def __init__(self, title, year, cast, genres):
        self.title  = title
        self.year   = year
        self.cast   = cast
        self.genres = genres
        
    def elencoRepetido(self, otra_pelicula):
        elenco_otra = otra_pelicula.cast
        for actor in self.cast:
            if not actor in elenco_otra:
                return False
        return True


# In[17]:


class Padre:
    def __init__(self, peliculas):
        self.peliculas = peliculas
        
    def addPelicula(self, ide):
        self.peliculas.append(ide)

class Actor(Padre):
    def __init__(self, peliculas, nombre):
        super().__init__(peliculas) ##https://realpython.com/python-super/ referencia para utilizar super correctamente.
        self.nombre    = nombre
        
class Año(Padre):
    def __init__(self, peliculas, numero):
        super().__init__(peliculas)
        self.numero    = numero
        
class Genero(Padre):
    def __init__(self, peliculas, tipo):
        super().__init__(peliculas)
        self.tipo      = tipo


# In[18]:


peliculas = {}
actores   = {}
años      = {}
generos   = {}

ide = 1 ##se creo un id pues existieron problemas en los ejercicios siguientes, dado que existen películas con el mismo nombre. Por esto, le creé un ID único a cada película.
##se llama ide pues el nombre -id- ya estaba definido en python
for movie in movies:
    pelicula = Pelicula(movie["title"], movie["year"], movie["cast"], movie["genres"])
    peliculas[ide] = pelicula
    
    for nombre in pelicula.cast:
        if nombre in actores:
            actor = actores[nombre]
        else:
            actor = Actor([], nombre)
            actores[nombre] = actor
            
        actor.addPelicula(ide)
        
    if pelicula.year in años:
        año = años[pelicula.year]
    else:
        año = Año([], pelicula.year)
        años[pelicula.year] = año
        
    año.addPelicula(ide)
    
    for tipo in pelicula.genres:
        if tipo in generos:
            genero = generos[tipo]
        else:
            genero = Genero([], tipo)
            generos[tipo] = genero
            
        genero.addPelicula(ide)
        
    ide += 1


# In[29]:


def criterio(tupla):
    return tupla[1]
##es importante notar que el quinto puesto lo comparten Horror y Musical, sin embargo,
##puse sólo Horror pues está dentro de los primeros 5 que imprime la función.

def generosPopulares(dic_generos, n):
    lista_generos = []
    for tipo in dic_generos:
        genero = dic_generos[tipo]
        cantidad_peliculas = len(genero.peliculas)
        lista_generos.append((tipo, cantidad_peliculas))
        
    lista_generos.sort(reverse= True, key= criterio) ##referencia http://elclubdelautodidacta.es/wp/2014/05/python-un-poco-de-orden/ e intro a programación
    n_generos_populares = lista_generos[:n]
    print("Los",n,"géneros más populares son:")
    print()
    for i in range(n):
        print("%s.- %s (%s películas)" % (i + 1, n_generos_populares[i][0], n_generos_populares[i][1]))##https://www.learnpython.org/es/String%20Formatting ##función %s sirve para escribir de manera ordenada de la forma que se le desee estructurar. En este caso la utilicé para plasmar en orden la respuesta.

generosPopulares(generos, 5)


# In[20]:


def añosPopulares(dic_años, n):
    lista_años = []
    for numero in dic_años:
        año = dic_años[numero]
        cantidad_peliculas = len(año.peliculas)
        lista_años.append((numero, cantidad_peliculas))
        
    lista_años.sort(reverse= True, key= criterio)
    n_años_populares = lista_años[:n]
    print("Los",n,"años con mayor cantidad de películas estrenadas son:")
    print()
    for i in range(n):
        print("%s.- %s (%s películas)" % (i + 1, n_años_populares[i][0], n_años_populares[i][1])) ##https://www.learnpython.org/es/String%20Formatting ##función %s sirve para escribir de manera ordenada de la forma que se le desee estructurar. En este caso la utilicé para plasmar en orden la respuesta.

añosPopulares(años, 3)


# In[24]:


def añosTrayectoria(actor, dic_peliculas):
    mayor_año = 0
    menor_año = 9999
    
    for titulo in actor.peliculas:
        pelicula = dic_peliculas[titulo]
        año = pelicula.year
        if año >= mayor_año:
            mayor_año = año
        if año <= menor_año:
            menor_año = año
    
    trayectoria = mayor_año - menor_año + 1
    return trayectoria
##función necesaria para pregunta 3


# In[25]:


##ojo que se imprimieron los primeros 7, dado que existe un error en la base de datos
##es por esto, que el primer actor corresponde a "." y el segundo "and", por ende
##sólo se considera del dato 2 al 7, anulando la respuesta de los primeros dos.
def actoresMayorTrayectoria(dic_actores, dic_peliculas, n): 
    lista_actores = []
    for nombre in dic_actores:
        actor = dic_actores[nombre]
        años_trayectoria = añosTrayectoria(actor, peliculas)
        lista_actores.append((nombre, años_trayectoria))
        
    lista_actores.sort(reverse= True, key= criterio)
    n_actores_populares = lista_actores[:n]
    print("Los",n,"actores con más años de trayectoria son:")
    print()
    for i in range(n):
        print("%s.- %s (%s años de trayectoria)" % (i + 1, n_actores_populares[i][0], n_actores_populares[i][1])) ##https://www.learnpython.org/es/String%20Formatting ##función %s sirve para escribir de manera ordenada de la forma que se le desee estructurar. En este caso la utilicé para plasmar en orden la respuesta.


# In[23]:


def elencoMasRepetido(dic_peliculas):

    elencos = []
    for ide in dic_peliculas:
        if len(dic_peliculas[ide].cast) > 1:
            elencos.append(dic_peliculas[ide].cast)
    mayores_repeticiones = 0
    elenco_repetido = []

    analisis_anterior = None    
    for i in range(len(elencos)):
        elenco = elencos[i]
        if elenco != analisis_anterior:
            repeticiones = elencos.count(elenco)
            if repeticiones >= mayores_repeticiones:
                mayores_repeticiones = repeticiones
                elenco_repetido = elenco
            analisis_anterior = elenco  
    print("El reparto que se ha repetido en la mayor cantidad de películas, es el de %s, el cual se ha repetido %s veces" % 
             (", ".join(elenco_repetido), mayores_repeticiones))
    
elencoMasRepetido(peliculas)

