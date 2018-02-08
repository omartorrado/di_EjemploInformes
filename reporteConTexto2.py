from reportlab.pdfgen import canvas

frase =["frase 1","frase 2","frase 3"]

aux = canvas.Canvas("exemploTexto2.pdf")

texto= aux.beginText()
texto.setTextOrigin(20,500)
texto.setFont("Courier",14)

for linea in frase:
    texto.textOut(linea)
    #desplazamientos en x e y (pixeles?)
    texto.moveCursor(0,15)

texto.setFillGray(0.5)

fraseMultilinea="""Esto es un
                parrafo de varias
                lineas"""

texto.textLines(fraseMultilinea)
aux.drawText(texto)

aux.showPage()
aux.save()