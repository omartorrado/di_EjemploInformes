from reportlab.pdfgen import canvas

frase =["frase 1","frase 2","frase 3"]

aux = canvas.Canvas("exemploTextoEspaciado.pdf")

texto= aux.beginText()
texto.setTextOrigin(20,500)
texto.setFont("Courier",14)

espacioCaracteres=0

for linea in frase:
    texto.setCharSpace(espacioCaracteres)
    texto.textLine("Espacio %s : %s " %(espacioCaracteres,linea))
    espacioCaracteres=espacioCaracteres+2

texto.setFillGray(0.5)

fraseMultilinea="""Esto es un
                parrafo de varias
                lineas"""

texto.setWordSpace(8)
texto.textLines(fraseMultilinea)

texto.setWordSpace(24)
texto.textLines(fraseMultilinea)
aux.drawText(texto)

aux.showPage()
aux.save()