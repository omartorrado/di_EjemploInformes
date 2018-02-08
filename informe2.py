from reportlab.graphics.shapes import Image,Drawing
from reportlab.graphics import  renderPDF
from reportlab.lib.pagesizes import A4

imaxes =[]

imaxe = Image(400,0,130,150,"/home/local/DANIELCASTELAO/otorradomiguez/Descargas/classic car logo.jpg")

debuxo = Drawing(30,30)
debuxo.add(imaxe)
debuxo.translate(0,700)
imaxes.append(debuxo)

debuxo = Drawing(30,30)
debuxo.add(imaxe)
debuxo.translate(-90,300)
imaxes.append(debuxo)

debuxo = Drawing(30,30)
debuxo.add(imaxe)
debuxo.scale(0.9,0.9)
debuxo.translate(-90,300)
imaxes.append(debuxo)

debuxo = Drawing(30,30)
debuxo.add(imaxe)
debuxo.rotate(45)
debuxo.scale(1.5,0.5)
debuxo.translate(-90,300)
imaxes.append(debuxo)

debuxo = Drawing(30,30)
debuxo.add(imaxe)
debuxo.rotate(90)
debuxo.translate(-20,-110)
imaxes.append(debuxo)


folla = Drawing(A4[0],A4[1])
print("x",A4[0],"y",A4[1])
for aux in imaxes:
    folla.add(aux)

renderPDF.drawToFile(folla,"exemploDrawing.pdf")