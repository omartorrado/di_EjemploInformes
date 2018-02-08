from reportlab.pdfgen import canvas

frase ="frase 1"

aux = canvas.Canvas("exemploTexto3.pdf")

texto= aux.beginText()
texto.setTextOrigin(20,800)
texto.setFont("Courier",14)

for linea in aux.getAvailableFonts():
    texto.setFont(linea, 14)
    texto.textLine(linea+" : "+frase)

texto.setFillGray(0.5)

aux.drawText(texto)

aux.showPage()
aux.save()