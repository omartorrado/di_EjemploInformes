import os

from reportlab.platypus import Paragraph,Image,SimpleDocTemplate,Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table

import sqlite3 as dbap1
#import sqlite3 as DatabaseError
from sqlite3 import DatabaseError


#guion será una lista de los objetos que vamos a incluir en el informe
guion=[]

cabeceira=[["DNI","Nombre","Dirección"]]

#tabla= Table(cabeceira)
#tabla.setStyle((["BOX",(0,0),(-1,-1),0.25,colors.black],["INNERGRID",(0,0),(-1,-1),0.25,colors.black]))

#guion.append(tabla)

try:
    bd=dbap1.connect("pythonDB.db")
    cursor=bd.cursor()
    cursor.execute("SELECT * from usuarios")
    tabla =Table(cabeceira+cursor.fetchall())
    #el primer valor es la propiedad a cambiar
    #los valores entre parentesis son a que parte afecta el estilo (columna inicial ,fila inicial),(columna final,fila final)
    #el 4º valor es el grosor de la linea (en los de bordes) o el alineamiento (en el align) [dependerá de la propiedad]
    #el 5º valor es el color (en el align no hay 5º valor)
    tabla.setStyle((["BOX", (0, 0), (-1, 0), 2, colors.black], ["INNERGRID", (0, 0), (-1, 0), 2, colors.black],['ALIGN', (0,0), (-1,0), 'CENTER']))
    tabla.setStyle((["BOX",(0,1),(-1,-1),2,colors.black],["INNERGRID",(0,1),(-1,-1),0.25,colors.black],["LINEABOVE",(0,1),(-1,1),2,colors.black]))

except DatabaseError as e:
    print("Error")

guion.append(tabla)

doc=SimpleDocTemplate("EjemploPlatypusTabla.pdf",pagesize=A4,showBoundaries=True)
doc.build(guion)