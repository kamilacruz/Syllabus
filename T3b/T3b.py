#!/usr/bin/env python
# coding: utf-8

# In[ ]:


connection = sqlite3.connect(‘data.db’) 
cursor = connection.cursor()
sqlStatement = ‘SELECT NIVEL, AVG(EDAD) FROM ESTUDIANTES WHERE NIVEL <> 'JR' GROUP BY NIVEL’ 
cursor.execute(sqlStatement)
connection.close()


# In[ ]:


connection = sqlite3.connect(‘data.db’) 
cursor = connection.cursor()
sqlStatement = ‘SELECT EST.NOMBRE FROM ESTUDIANTES EST LEFT OUTER JOIN INSCRITOS INS ON EST.NUM = INS.NUM.ESTWHERE INS.NUM.EST IS NULL’ 
cursor.execute(sqlStatement)
connection.close()

