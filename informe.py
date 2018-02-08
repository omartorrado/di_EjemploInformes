from reportlab.pdfgen import canvas

aux = canvas.Canvas("PrimeiroInforme.pdf")

aux.drawString(0,0,"Posición inicial (x,y) = (0,0)")
aux.drawString(50,100, "Posición (x,y) = (50,100)")
aux.drawString(150,20, "Posición (x,y) = (150,20)")


aux.drawImage("/home/local/DANIELCASTELAO/otorradomiguez/Descargas/classic car logo.jpg",30,60,300,300,None,True)
aux.drawString(300,600,"Exemplo de inserción de imaxe en pdf")

aux.showPage()
aux.save()