import os

from reportlab.platypus import Paragraph,Image,SimpleDocTemplate,Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

follaEstilo=getSampleStyleSheet()

#guion será una lista de los objetos que vamos a incluir en el informe
guion=[]

cabeceira = follaEstilo["Heading4"]
cabeceira.pageBreakBefore=0
cabeceira.keepWithNext=0
cabeceira.backColor= colors.cyan


parrafo= Paragraph("CABECEIRA DO DOCUMENTO",cabeceira)
guion.append(parrafo)

cadea="patata "*1000
corpoTexto= follaEstilo["BodyText"]

parrafo2=Paragraph(cadea,corpoTexto)
guion.append(parrafo2)

guion.append(Spacer(0,20))

imagen = Image(os.path.realpath("/home/local/DANIELCASTELAO/otorradomiguez/Descargas/imagen1.jpg"),width=400,height=300)
guion.append(imagen)

doc=SimpleDocTemplate("EjemploPlatypus.pdf",pagesize=A4,showBoundaries=True)
doc.build(guion)