#!/usr/bin/env python
# coding: utf-8

# # IIC2115 - Programación Como Herramienta para la Ingeniería
# ## Actividad 3
# Se importan librerías necesarias:

# In[1]:


import sqlite3


# Se cargan los archivos de datos en diccionarios

# In[2]:


empleados = []
departamentos = []
trabaja_en = []
def llenar_lista(nombre_archivo, lista, llaves):
    with open(nombre_archivo, encoding="utf-8") as archivo:
        contenido = archivo.readlines()
        for linea in contenido:
            elemento = {}
            data = linea.strip("\n").split(",")
            for i in range(len(llaves)):
                elemento[llaves[i]] = data[i]
            lista.append(elemento)
            
llenar_lista("empleado.txt", empleados, ["id","nombre","edad","sueldo"])
llenar_lista("departamento.txt", departamentos, ["id","nombre","presupuesto","id_jefe"])
llenar_lista("trabaja_en.txt", trabaja_en, ["id_empleado","id_depto","porcentaje_tiempo"])


# Se crean las tablas para modelar los datos y las relaciones descritas

# In[3]:


connection = sqlite3.connect("empresa.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Empleados(id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER, sueldo INTEGER)")
cursor.execute("CREATE TABLE Departamentos(id INTEGER PRIMARY KEY, nombre TEXT, presupuesto REAL, id_jefe INTEGER, FOREIGN KEY (id_jefe) REFERENCES Empleados)")
cursor.execute("CREATE TABLE TrabajaEn(id_empleado INTEGER, id_dpto INTEGER, porcentaje_tiempo INTEGER, FOREIGN KEY (id_empleado) REFERENCES Empleados, FOREIGN KEY (id_dpto) REFERENCES Departamentos)")

connection.commit()
connection.close()


# Ingresamos la data a la base

# In[4]:


def ingresar_datos(nombre_tabla, lista_valores):
    connection = sqlite3.connect("empresa.db")
    cursor = connection.cursor()
    for elemento in lista_valores:
        values = tuple(elemento.values())
        n = len(values)
        tupla = "(" + ",".join(["?"] * n) +")"
        cursor.execute("INSERT INTO " + nombre_tabla + " VALUES " + tupla, values)
    connection.commit()
    connection.close()
    
ingresar_datos("Empleados", empleados)
ingresar_datos("Departamentos", departamentos)
ingresar_datos("TrabajaEn", trabaja_en)


# Se generan las consultas solicitadas
# ### 1. Nombre y edad de cada empleado que trabaja en los departamentos de Software y Hardware

# In[5]:


connection = sqlite3.connect("empresa.db")
cursor = connection.cursor()

cursor.execute(
    """SELECT e.nombre, e.edad
    FROM Empleados e
    INNER JOIN TrabajaEn t
    ON e.id = t.id_empleado
    INNER JOIN Departamentos d
    ON t.id_dpto = d.id
    WHERE (d.nombre = 'Software' OR d.nombre = 'Hardware')
    GROUP BY e.id
    HAVING COUNT(*) = 2
    """
)
resultado_1 = cursor.fetchall()

connection.commit()
connection.close()

resultado_1


# ### 2. Nombre de los jefes que administran los departamentos de presupuesto máximo

# In[6]:


connection = sqlite3.connect("empresa.db")
cursor = connection.cursor()

cursor.execute(
    """SELECT e.nombre
    FROM Departamentos d
    INNER JOIN Empleados e
    ON d.id_jefe = e.id
    WHERE d.presupuesto = (SELECT presupuesto FROM Departamentos ORDER BY presupuesto DESC LIMIT 1)
    """
)
resultado_2 = cursor.fetchall()

connection.commit()
connection.close()

resultado_2


# ### 3. Nombre de los empleados cuyo sueldo excede el presupuesto de todos los departamentos en los que trabaja

# In[7]:


connection = sqlite3.connect("empresa.db")
cursor = connection.cursor()

cursor.execute(
    """SELECT e.nombre
    FROM Empleados e
    WHERE e.sueldo > (SELECT presupuesto
                        FROM Departamentos d
                        INNER JOIN TrabajaEn t
                        ON d.id = t.id_dpto
                        WHERE t.id_empleado = e.id
                        ORDER BY presupuesto DESC LIMIT 1)
    """
)
resultado_3 = cursor.fetchall()

connection.commit()
connection.close()

resultado_3


# ### 4. Nombre y cantidad de empleados de los departamentos con dedicación del personal equivalente a 20 jornadas completas

# In[8]:


connection = sqlite3.connect("empresa.db")
cursor = connection.cursor()

cursor.execute(
    """SELECT d.nombre, COUNT(*)
    FROM Departamentos d
    INNER JOIN TrabajaEn t
    ON t.id_dpto = d.id
    INNER JOIN Empleados e
    ON e.id = t.id_empleado
    WHERE d.id IN (SELECT t1.id_dpto
                    FROM TrabajaEn t1
                    GROUP BY t1.id_dpto
                    HAVING SUM(t1.porcentaje_tiempo) >= 2000)
    GROUP BY t.id_dpto
    """
)
resultado_4 = cursor.fetchall()

connection.commit()
connection.close()

resultado_4

