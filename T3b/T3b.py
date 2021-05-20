#!/usr/bin/env python
# coding: utf-8

# In[57]:


import sqlite3
import csv


# In[58]:


def query(query):
    connection = sqlite3.connect('data.db') 
    cursor = connection.cursor()
    cursor.execute(query)
    for r in cursor:
        print(r)
    connection.close()


# In[134]:


query("select *  From estudiantes ")


# In[128]:


query("select *  From profesores")


# In[129]:


query("select *  From cursos")


# In[130]:


query("select *  From inscritos")


# In[122]:


query("""select estudiantes.nombre From estudiantes
        left join inscritos
        on estudiantes.num = inscritos.num_est
        
        left join cursos 
        on cursos.nombre = inscritos.nombre_curso
        
        left join profesores
        on profesores.id = cursos.id_profesor
        
        where( profesores.nombre like '%Teach%'
                and estudiantes.nivel = 'JR')
        """)


# In[131]:


query("""select profesores.nombre
        From estudiantes
        left join inscritos
        on estudiantes.num = inscritos.num_est
        
        left join cursos 
        on cursos.nombre = inscritos.nombre_curso
        
        left join profesores
        on profesores.id = cursos.id_profesor
        
        where( cursos.sala = 'R128')
        """)


# In[133]:


query("""select estudiantes.nombre, max(estudiantes.edad) From estudiantes
        left join inscritos
        on estudiantes.num = inscritos.num_est
        
        left join cursos 
        on cursos.nombre = inscritos.nombre_curso
        
        left join profesores
        on profesores.id = cursos.id_profesor
        
        where( profesores.nombre ='Ivana Teach'
                and estudiantes.major = 'History')
        """)


# In[ ]:




