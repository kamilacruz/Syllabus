#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque
#encontrar la longitud máxima de secuencia de paréntesis balanceados
 
def calcular_max_long(str):  
    long = 0
    stack = deque()
    stack.append(-1) #manejar el caso donde el primer ( se encuentra en el índice 0 del string

    for i, k in enumerate(str): #fuente: https://www.bitdegree.org/learn/python-enumerate#how-enumerate-works
        if k == '(': #por abre paréntesis 
            stack.append(i)
        else: #por cierre paréntesis
            stack.pop()
            if not stack: #si el stack queda vacío después
                #inserte el índice en el que se encuentra actualmente la iteración
                stack.append(i)
                continue

            actual_longitud = i - stack[-1] #calcular la longitud de la secuencia actual
            #restándole al índice actual el valor en el tope del stack
 
            if long < actual_longitud: #comprar la longitud con el máx registrado hasta el momento 
                long = actual_longitud #actualice la variable en caso de ser mayor la nueva longitud
 
    return long 
 

parentesis= "(((()()"
max_long=calcular_max_long(parentesis)
print(max_long)                          # imprimirá 4


# In[ ]:




