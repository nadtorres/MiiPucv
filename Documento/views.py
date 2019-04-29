from django.shortcuts import render


#Librerías para generar PDF
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, legal, A4
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Table, TableStyle, Image, Spacer, SimpleDocTemplate, Frame, PageTemplate, NextPageTemplate, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.lib import colors 
from reportlab.lib.colors import white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, PropertySet
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph , Preformatted
from django.http import FileResponse
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily 

import random
import datetime

# Create your views here.



def acta_interna(request):

    #GET Para obtener los datos de Alumno
    objeto1 = Alumno.objects.get(id=1)   
    nombre_Alumno = str(objeto1.nombre)+' '+str(objeto1.apellido_pat)+' '+str(objeto1.apellido_mat)

    objeto2 = Profesor.objects.get(id=1)   
    nombre_Profesor = str(objeto2.nombre)+' '+str(objeto2.apellido_pat)+' '+str(objeto2.apellido_mat)

    objeto3 = Profesor.objects.get(id=2)   
    nombre_Pro_Cotutor = str(objeto3.nombre)+' '+str(objeto3.apellido_pat)+' '+str(objeto3.apellido_mat)

    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] = 'attachment; filename=actaInterna.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    #Header 
    fecha = datetime.date.today().strftime("%d/%m/%Y")

    c.setLineWidth(.3)
    c.setFont('Helvetica', 20)
    c.drawString(30,750, 'Doctorado en Ingeniería Informática')

    c.setFont('Helvetica-Bold', 12)
    c.drawString(480,730, fecha)

    c.setFont('Helvetica-Bold', 14)
    c.drawString(250,700,'ACTA INTERNA')
    c.line(250,698,355,698)

    c.setFont('Helvetica-Bold', 14)
    c.drawString(220,685,'EVALUACION DE AVANCE')
    c.line(220,683,400,683)

    c.setFont('Helvetica-Bold', 14)
    c.drawString(216,670,'ASIGNATURA DII 795 TESIS')
    c.line(216,668,400,668)

    c.setFont('Helvetica', 12)
    c.drawString(30,615, 'ALUMNO:')
    c.drawString(90,615,nombre_Alumno)
    
    c.setFont('Helvetica', 12)
    c.drawString(30,595, 'PROF. GUIA:')
    c.drawString(105,595, nombre_Profesor)

    c.setFont('Helvetica', 12)
    c.drawString(30,575, 'PROF. COTUTOR o INVITADO:')
    c.drawString(205,575, nombre_Pro_Cotutor)

    c.setFont('Helvetica', 12)
    c.drawString(30,560, 'TEMA:')
    c.drawString(70,560, 'Software Programa Magister')

    #PIE DE FIRMA 
    c.setFont('Helvetica', 12)
    c.drawString(105, 159, nombre_Profesor)
    c.line(90,175,250,175)

    c.setFont('Helvetica', 12)
    c.drawString(360, 159, nombre_Pro_Cotutor)
    c.line(350,175,510,175)

    students = [{'Tipo Evaluacion': 'Avance 1 2 ó 3', 'Fecha': fecha , 'Nota':' '},]
               
    # Table Header
    style = getSampleStyleSheet()
    styleBH = style["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 10

    style = getSampleStyleSheet()
    styleBH2 = style["Normal"]
    styleBH2.alignment = TA_LEFT
    styleBH2.fontSize = 10


    tipo_evaluacion = Paragraph('''Tipo Evaluacion <br /> (Avance 1, 2 ó 3 )''',styleBH2)
    Fecha = Paragraph('''Fecha''', styleBH)
    Nota = Paragraph('''Nota''',styleBH)

    data = []
    data.append([tipo_evaluacion, Fecha, Nota])

    #Table 
    # styles = getSampleStyleSheet()
    styleN = style ["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 7


    width, height = letter
    high = 500
    for student in students:
        this_student = [student['Tipo Evaluacion'],student['Fecha'],student['Nota']]
        data.append(this_student)
        high = high - 18

    #table size 
    table = Table(data, colWidths=[9.0 * cm, 4.0 * cm, 5.0 * cm], rowHeights = 1 * cm)
    table.setStyle(TableStyle([ #estilo de la tabla
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 1.5, colors.black),
    ]))

    p = ParagraphStyle('parrafos')
    p.alignment = TA_JUSTIFY
    p.fontSize = 10
    p.fontName = "Times-Roman"
    obs = Paragraph("OBSERVACIONES Y RECOMENDACIONES: ", p)
    observaciones = [[obs]]
    tabla_observaciones = Table(observaciones, colWidths=[18 * cm], rowHeights = 8.6 * cm)
    tabla_observaciones.setStyle(TableStyle([
        ('GRID', (0, 0), (0, 2), 1.5, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('ALIGN',(0,0),(-1,-1),'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    obs = Paragraph("OBSERVACIONES;", p)
    #PDF size 
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, high)
    tabla_observaciones.wrapOn(c, width, height)
    tabla_observaciones.drawOn(c, 30, 237) 
    c.showPage() #save page

    #save PDF
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    # c.showPage()
    # c.save()
    return response

def switch_demo(argument):
    switcher = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    return switcher.get(argument, "Invalid month")

def certificado_Egreso(request):
    objeto = Profesor.objects.get(id=1)   
    nombre_Profesor = str.upper(objeto.nombre)+' '+str.upper(objeto.apellido_pat)+' '+str.upper(objeto.apellido_mat)
    rut_profesor = str.upper(objeto.rut)

    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    doc = canvas.Canvas(buffer, pagesize=letter)

    sample_style_sheet = getSampleStyleSheet()

    doc=SimpleDocTemplate(buffer, 
                        rightMargin=75,
                        leftMargin=75,
                        topMargin=20,
                        pagesize=letter, 
                        showBoundary=0,
                       )

    story = []
    style = sample_style_sheet["Normal"]
    style.fontName = 'Times-Roman'
    style.fontSize = 10

    cadena = 'FACULTAD DE INGENIERIA'
    parrafo_1 = Paragraph(cadena, style)
    cadena_2 = 'ESCUELA DE INGENIERIA INFORMATICA'
    parrafo_2 = Paragraph(cadena_2, style)

    Style2 = getSampleStyleSheet()
    style_2 = Style2["Normal"]
    style_2.fontName = 'Helvetica-Bold'
    style_2.fontSize = 10
    cadena_3 = '<u>DOCTORADO EN INGENIERIA INFORMATICA</u>'
    parrafo_3 = Paragraph(cadena_3, style_2)

    style3 = getSampleStyleSheet()
    style_3 = style3["Normal"]
    style_3.fontName = 'Helvetica-bold'
    style_3.alignment = TA_CENTER
    style_3.fontSize = 18
    cadena_4 = '<br /><br /><br /><br /><br /><br /><u><i> CERTIFICADO DE EGRESO</i></u>'
    parrafo_4 = Paragraph(cadena_4, style_3)

    fecha_dia = datetime.date.today().strftime("%d")
    fecha_mes = int(datetime.date.today().strftime("%m"))
    fecha_anio = datetime.date.today().strftime("%Y")

    style4 = getSampleStyleSheet()
    style_4 = style4["Normal"]
    style_4.alignment = TA_JUSTIFY
    style_4.fontSize = 12
    style_4.fontName= 'Times-Roman'
    style_4.leading = 25
    style_4.spaceAfter = -10
    cadena_5 = '<br /> <br /><br /><strong>' + nombre_Profesor + '</strong>, Director de Doctorado en Ingeniería Informática de la Escuela de Ingeniería Informática de la Facultad de Ingeniería de la Pontificia Universidad Católica de Valparaíso, certifica que Don <strong>' + nombre_Profesor + ', ' + rut_profesor + '</strong> ha cumplido con todos los requisitos académicos contemplados en el <strong>Plan de Estudios del  Programa de Doctorado en Ingeniería Informática.</strong>'
    parrafo_5 = Paragraph(cadena_5, style_4)
    cadena_6 = '<br />El presente documento se extiende para efectos internos y a fin de ser  presentado ante la <u><i>Dirección de Estudios Avanzados</i></u> de esta Universidad, dentro del proceso de la obtención de grado.'
    parrafo_6 = Paragraph(cadena_6, style_4)
    cadena_7 ='<br /><br /><br /><br />VALPARAISO,  ' + ' ' + fecha_dia + ' de ' + switch_demo(fecha_mes) + ' de ' + fecha_anio + ' '
    parrafo_7 = Paragraph(cadena_7, style_4)

    style5 = getSampleStyleSheet()
    style_5 = style5["Normal"]
    style_5.alignment = TA_LEFT
    style_5.fontName = 'Times-Roman'
    style_5.fontSize = 12
    style_5.spaceAfter = 0
    style_5.spaceBefore = -50
    style_5.leading = 10
    cadena_8 = '004/' + fecha_anio + '/INF-DOC'
    parrafo_8 = Paragraph(cadena_8, style_5)

    story.append(parrafo_1)
    story.append(parrafo_2)
    story.append(parrafo_3)
    story.append(parrafo_4)
    story.append(parrafo_5)
    story.append(parrafo_6)
    story.append(parrafo_7)
    story.append(parrafo_8)

    doc.build(story)
 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificado2.pdf"'
    pdf = buffer.getvalue()
    response.write(pdf)
    return response

def actaExamenGrado(request):

    buffer = BytesIO()
    doc = canvas.Canvas(buffer, pagesize=legal)

    sample_style_sheet = getSampleStyleSheet()

    doc=SimpleDocTemplate(buffer, 
                        rightMargin=65, 
                        leftMargin=65,
                        bottomMargin= 0,
                       )

    story = []
    style = sample_style_sheet["Normal"]
    style.fontName = 'Times-Roman'
    style.fontSize = 10
    style.alignment = TA_RIGHT

    cadena = 'FACULTAD DE INGENIERIA'
    parrafo_1 = Paragraph(cadena, style)
    cadena_2 = 'ESCUELA DE INGENIERIA INFORMATICA'
    parrafo_2 = Paragraph(cadena_2, style)
    cadena_3 = '<u>DOCTORADO EN INGENIERIA INFORMATICA</u>'
    parrafo_3 = Paragraph(cadena_3, style)

    Style2 = getSampleStyleSheet()
    style_2 = Style2["Normal"]
    style_2.fontName = 'Courier-Bold'
    style_2.fontSize = 16
    style_2.alignment = TA_CENTER
    cadena_4 = '<br /><u>ACTA INTERNA EXAMEN DE GRADO. (1)</u>'
    parrafo_4 = Paragraph(cadena_4, style_2)

    style3 = getSampleStyleSheet()
    style_3 = style3["BodyText"]
    style_3.fontName = 'Times-Roman'
    style_3.fontSize = 14
    style_3.alignment = TA_JUSTIFY
    style_3.leading = 25
    cadena_5 = '<br /> Considerando que la alumna TANIA ELIZABETH PIZARRO RUBILAR,  ha completado el currículum del programa de <strong>Magíster en Ingeniería Informática</strong>,  y cumple con los requisitos administrativos prescritos por la Unidad Académica, la Dirección del Programa de Magíster en Ingeniería Informática de la Pontificia Universidad Católica de Valparaíso,  ha fijado el Examen final para el día <strong>MIÉRCOLES 14 DE NOVIEMBRE DE 2018</strong>, ante la Comisión integrada por los señores profesores:'
    parrafo_5 = Paragraph(cadena_5, style_3)

    style4 = getSampleStyleSheet()
    style_4 = style4["Normal"]
    style_4.fontName = 'Times-Roman'
    style_4.fontSize = 14

    presidente = 'PRESIDENTE' + '&nbsp;' * 17 + ':'  
    name_Presi = 'JOSE CERON DIAZ'
    decano = 'Decano de la Facultad de Ingenieria<br /><br />'

    P_name_Presi = Paragraph(name_Presi, style_4)
    P_decano = Paragraph(decano, style_4)
    P_president = Paragraph(presidente, style_4)

    director = 'DIRECTOR DE TESIS' + '&nbsp;' * 3 + ':'  
    name_director = 'CLAUDIO CUBILLOS FIGUEROA<br /><br />' 
    P_director = Paragraph(director, style_4)
    P_name_director = Paragraph(name_director, style_4)

    examinador_exter = 'EXAMINADOR' + '&nbsp;' * 14 + ':'  
    name_examin_exter = 'RAFAEL MELLADO SILVA'
    externo = 'EXTERNO<br /><br />'
    P_examinador_exter = Paragraph(examinador_exter, style_4)
    P_name_examin_exter = Paragraph(name_examin_exter, style_4)
    P_externo = Paragraph(externo, style_4)

    examinador = 'EXAMINADOR' + '&nbsp;' * 14 + ':'
    name_examin = 'SILVANA RONCAGLIOLO DE LA HORRA<br /><br />'
    P_examinador = Paragraph(examinador, style_4)
    P_name_examin = Paragraph(name_examin, style_4)

    examinador2 = 'EXAMINADOR' + '&nbsp;' * 14 + ':'
    name_examin2 = 'GUILLERMO CABRERA GUERRERO<br />'
    P_examinador2 = Paragraph(examinador2, style_4)
    P_name_examin2 = Paragraph(name_examin2, style_4)

    
    story.append(parrafo_1)
    story.append(parrafo_2)
    story.append(parrafo_3)
    story.append(parrafo_4)
    story.append(parrafo_5)


    t=Table(
        data=[
            [P_president, P_name_Presi],
            [ ' ' , P_decano],
            [P_director, P_name_director],
            [P_examinador_exter, P_name_examin_exter],
            [P_externo, ' '],
            [P_examinador, P_name_examin],
            [P_examinador2, P_name_examin2]
        ],
        style=[('ALIGN',(1,1),(-1,-1),'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        
        ]
    )
    story.append(t)

    style_tema = getSampleStyleSheet()
    style_temas = style_tema["BodyText"]
    style_temas.fontName = 'Times-Roman'
    style_temas.fontSize = 14
    style_temas.leading = 15
    style_temas.alignment = TA_JUSTIFY


    tema = '<br /> La alumna dispondrá de 30 minutos para presentar su tema:'
    P_tema = Paragraph(tema, style_3)   
    story.append(P_tema)

    name_tema = '<strong>“DESARROLLO DE UNA PLATAFORMA E-LEARNING PARA LA ORIENTACIÓN A OBJETOS UTILIZANDO ESTILOS DE APRENDIZAJE DE VARK”,</strong>'
    P_name_tema = Paragraph(name_tema, style_temas)
    story.append(P_name_tema)

    preguntas = '<br /> después de los cuales deberá contestar las preguntas de la Comisión.'
    P_preguntas = Paragraph(preguntas, style_3)   
    story.append(P_preguntas)

    palabra = getSampleStyleSheet()
    style_palabra = palabra["BodyText"]
    style_palabra.fontName = 'Times-Roman'
    style_palabra.fontSize = 14
    style_palabra.alignment = TA_CENTER
    
    T_palabra = '<br /> <strong>TIENE LA PALABRA</strong>'
    P_palabra = Paragraph(T_palabra, style_palabra)   
    story.append(P_palabra)

    fecha_dia = datetime.date.today().strftime("%d")
    fecha_mes = int(datetime.date.today().strftime("%m"))
    fecha_anio = datetime.date.today().strftime("%Y")
  
    fecha ='<br /><br /><br />VALPARAISO,  ' + '<strong>' + fecha_dia + ' DE ' + switch_demo(fecha_mes).upper() + ' DE ' + fecha_anio + ' </strong>'
    P_fecha = Paragraph(fecha, style_4)
    story.append(P_fecha)

    story.append(PageBreak())

    facultad = 'FACULTAD DE INGENIERIA'
    P_facultad = Paragraph(facultad, style)
    escuela = 'ESCUELA DE INGENIERIA INFORMATICA'
    P_escuela = Paragraph(escuela, style)
    doctorado = '<u>DOCTORADO EN INGENIERIA INFORMATICA</u>'
    P_doctorado = Paragraph(doctorado, style)

    acta = '<br /><u>ACTA INTERNA EXAMEN DE GRADO. (2)</u>'
    P_acta = Paragraph(acta, style_2)

    alumna = '<br /> Dado que la alumna <strong>TANIA ELIZABETH PIZARRO RUBILAR,</strong> del programa de MAGISTER EN INGENIERIA INFORMATICA ha obtenido:'
    P_alumna = Paragraph(alumna, style_3)

    S_nota = getSampleStyleSheet()
    style_nota = S_nota["BodyText"]
    style_nota.fontName = 'Times-Roman'
    style_nota.fontSize = 14
    style_nota.alignment = TA_LEFT
    style_nota.leftIndent = 10
    style_nota.leading =  25

    nota = '-' + '&nbsp;' * 14 + 'nota de presentación de sus estudios (50%):&nbsp; __________'
    nota2 ='-' + '&nbsp;' * 14 + 'nota de tésis de magíster (25%):&nbsp; __________'
    nota3 = 'y que esta Comisión ha aprobado la presentación con nota (25%):&nbsp; __________<br />'

    P_nota = Paragraph(nota, style_nota)
    P_nota2 = Paragraph(nota2, style_nota)
    P_nota3 = Paragraph(nota3, style_3)

    styleText = getSampleStyleSheet()
    style_texto2 = styleText["BodyText"]
    style_texto2.fontName = 'Times-Roman'
    style_texto2.fontSize = 14
    style_texto2.alignment = TA_JUSTIFY
    style_texto2.leading = 35
    text2= '<br /> La Escuela de Ingeniería   Informática de la Pontificia Universidad Católica de Valparaíso, solicitará a través del  Decanato de la Facultad de Ingeniería, que la UNIVERSIDAD le otorgue el <strong>GRADO DE MAGISTER EN INGENIERIA INFORMATICA,</strong>'
    P_text2 = Paragraph(text2,style_texto2)

    notafinal ='con nota final:'+  '&nbsp;'*5+ '__________(_________________________________).'
    calificacion='con calificación: ____________________________________________.'
    P_notafinal = Paragraph(notafinal, style_3)
    P_calificacion = Paragraph(calificacion, style_3)

    firmas = '<u><i>Firmas de la Comisión:</i></u><br /><br />'
    P_firmas = Paragraph(firmas, style_3)

    styles = getSampleStyleSheet()
    styleTable = styles['BodyText']
    styleTable.alignment = TA_CENTER
    styleTable.fontSize = 10
    styleTable.fontName = 'Times-Roman'

    Presi = Paragraph('''JOSE CERONI DIAZ''', styleTable)
    Dire = Paragraph('''CLAUDIO CUBILLOS FIGUEROA''', styleTable)
    Exa_Ext = Paragraph('''RAFAEL MELLADO SILVA''', styleTable)
    Exam = Paragraph('''SILVANA RONCAGLIOLO DE LA HORRA''', styleTable)
    Exam2 = Paragraph('''GUILLERMO CABRERA GUERRERO''', styleTable)
    t2=Table(
        data=[
            [Presi, ' ' , Dire],
            [ Exa_Ext,Exam,Exam2],

        ], colWidths=140, rowHeights=70,
        style=[('ALIGN',(1,1),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        
        ] )

    fecha2 ='<br /><br />VALPARAISO,  ' + '<strong>' + fecha_dia + ' DE ' + switch_demo(fecha_mes).upper() + ' DE ' + fecha_anio + ' </strong>'
    P_fecha2 = Paragraph(fecha2, style_4)

    story.append(P_facultad)
    story.append(P_escuela)
    story.append(P_doctorado)
    story.append(P_acta)
    story.append(P_alumna)
    story.append(P_nota)
    story.append(P_nota2)
    story.append(P_nota3)
    story.append(P_text2)
    story.append(P_notafinal)
    story.append(P_calificacion)
    story.append(P_firmas)
    story.append(t2)
    story.append(P_fecha2)


    doc.build(story)
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename = "ExamenGrado.pdf"'
    pdf = buffer.getvalue()
    response.write(pdf)
    return response

def crear_expediente(request):
    buffer = BytesIO()
    doc = canvas.Canvas(buffer, pagesize=letter)

    doc = SimpleDocTemplate(buffer,
                            rightMargin=65,
                            leftMargin=65,
                            )
#///////////////STYLE//////////////////

    estiloHoja = getSampleStyleSheet()
    cabecera = estiloHoja['Heading4']
    story = []
    cabecera.pageBreakBefore=0
    cabecera.keepWithNext=0
    cabecera.fontSize=8

    EstiloNormal = getSampleStyleSheet()
    TextoNormal = EstiloNormal['Normal']
    TextoNormal.fontSize=10

    EstiloNormalPequeño = getSampleStyleSheet()
    TextoNormalPequeño = EstiloNormalPequeño['BodyText']
    TextoNormalPequeño.fontZise= 6

    style22 = getSampleStyleSheet()
    #style22.add(ParagraphStyle(name="cadena44", alignment = TA_LEFT, borderPadding = 1, borderColor = 'black'))
    style_22 = style22['Normal']
    style_22.spaceBefore = 5
    style_22.spaceAfter = 5
    #style_22.borderPadding = 10
    #style_22.borderWidth = 2
    #style_22.borderColor = 'black'

    estilo = getSampleStyleSheet()
    firmastyle = estilo['Normal']
    firmastyle.alignment = TA_RIGHT
    firmastyle.spaceBefore = 15
    firmastyle.rigthIndent = 60

    Aderecha = getSampleStyleSheet()
    alineadoderecha = Aderecha['Normal']
    alineadoderecha.alignment=TA_RIGHT

    Aizquierda = getSampleStyleSheet()
    alineadoizq=Aizquierda['Normal']
    alineadoizq.alignment=TA_LEFT

    AcentradoT = getSampleStyleSheet()
    centradoTitulo= AcentradoT['Heading1']
    centradoTitulo.alignment=TA_CENTER
    centradoTitulo.fontZise= 15

    Acentrado = getSampleStyleSheet()
    centrado = Acentrado['Normal']
    centrado.alignment=TA_CENTER


#//////////////////////////////imagenes//////////////////////
    fichero_imagen = "PUCV.jpg"
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=50,height=50)
    imagen_logo.hAlign = 'LEFT'

#//////////////////////////////Parrafos y texto//////////////////////
#GLOBAL
    fechad= Paragraph("VALPARAÍSO, dia* de mes* de anio*",alineadoderecha)

    fechai=Paragraph("VALPARAÍSO, dia* de mes* de anio*",alineadoizq)
#pagina1
    #cabecera
    p = Paragraph("PONTIFICIA<br />UNIVERSIDAD<br />CATÓLICA DE<br />VALPARAÍSO ",cabecera)
    p1 = Paragraph("Expediente Nº:"+'<u></u>'+'<br />'+"Instituto Escuela"+'<u></u>'+'<br />'+"Grado"+'<u></u>'+'<br />'+"Título"+'<u></u>',alineadoderecha)
    #primer parrafo
    cadena = "Señor Director:"+"<br />"+"<strong>Nombre Alumno u Alumna*</strong>"+'<br />'+"Alumno egresado*"+" del Programa de Magíster en Ingeniería Informática, solicita que se le autorice rendir el Examen para optar al Grado de Magíster en Ingeniería Informática según DRA. 39/2006.<br />"+"<br />"+"<br />"
    firma = "__________________<br />Firma"+'&nbsp;'*13+"<br />"
    director = "__________________<br />Director"+'&nbsp;'*11+"<br />"
    secretario = "__________________<br />Secretario Academico"+'&nbsp;'*1+"<br />"
    p2 = Paragraph(firma,firmastyle)
    p5 = Paragraph(director,firmastyle)
    p6 = Paragraph(secretario,firmastyle)
    p2_1 = Paragraph(cadena, TextoNormal)
    #2do parrafo
    cadena2 ="El Postulante cumple con los requisitos para rendir el Examen de grado."+'<br />'+"Ingresó al Programa de Magíster en Ingeniería Informática en calidad de alumno el "+" de "+" y egresó el "+" de "+"."+'<br />'+"Antecedentes del ingreso:<br />"+"Promedio General de sus estudios en el Programa:<br />"+"Fecha del Examen de Grado:"+".<br />"+"<br />"+"<br />"
    p3 = Paragraph(cadena2,TextoNormal)
    #3r parrafo
    cadena3 ="Autorizo para rendir el Examen de grado de Magíster en Ingeniería Informática, en la fecha y ante la Comisión que el Secretario Académico de la Escuela determine."+'<br /><br />'
    p4 = Paragraph(cadena3,TextoNormal)   
#pagina2
    #cabecera
    w = Paragraph("<strong>MEMORIA</strong>",centradoTitulo)
    w1 = Paragraph("Tema:"+'&nbsp;'*2+"<strong>Titulo del tema*</strong>",TextoNormal)
    pguia= Paragraph("Profesor Guia: ",TextoNormal)
    w2 = Paragraph("texto de prueba",TextoNormalPequeño)

    w3 = Paragraph("<strong>EXAMEN DE GRADO O TÍTULO</strong>",centradoTitulo)
    w4 = Paragraph("Tema: "+"<strong> nombre del tema*</strong><br />",TextoNormal)
    w5 = Paragraph("Comisíon: Sres.: <br />",TextoNormal)
    w67 = Paragraph("columna1"+'&nbsp;'*16+"columna2"+'<br />'+"columna1"+'&nbsp;'*16+"columna2"+'<br />'+"columna1"+'&nbsp;'*16+"columna2"+'<br />'+"columna1"+'&nbsp;'*16+"columna2"+'<br />',alineadoderecha)
    w8= Paragraph('<br />'+"Informe:<br />"+"El alumno rindió su examen de grado y respondió satisfactoriamente las preguntas de la comisión.<br />"+"Calificacíon:<br />",TextoNormal)
    w9 = Paragraph("firma1"+'&nbsp;'*10+"firma2"+'&nbsp;'*10+"firma3"+'<br />'+"firma4"+'&nbsp;'*10+"firma5<br />",centrado)
    w10=Paragraph("Firmas de la Comisíon",centrado)
#pagina3
    z=Paragraph("La Facultad de Ingeniería de esta Universidad, vistos los antecedentes, propone al señor Rector otorgar a "+"<strong>nombre*</strong>",TextoNormal)
    z1=Paragraph("El grado de Magíster en Ingeníeria Informática<br />"+"con la calificacion final "+'nota*'+"(nota texto*)",TextoNormal)
    z2=Paragraph("<br /><br />",TextoNormal)
    z3=Paragraph("Rut: 11111111-1*",TextoNormal)
    z4=Paragraph("Vº.Bº. Vicerrector de Investigación y Estudios Avanzados",centrado)
    z5= Paragraph("Vº.Bº. Secretario General",centrado)
    z6=Paragraph("<br /><br /><br /><br /><br /><br /><br />",TextoNormal)
    z7=Paragraph('<br /><br /><br /><br /><br /><br />'+"________________________<br />"+"Vº.Bº. Contraloría"+'&nbsp;'*10+'<br /><br /><br /><br /><br />',alineadoderecha)

#///////////////////////////////tabla///////////////////////
    t=Table(
        data=[
            [[imagen_logo,p],[p1]],
        ],
        style=[
            
        ]
        )
    t2=Table(
        data=[
            [p2_1],
            [fechai],
            [p2],
        ],
        style=[
            ('BOX',(0,0),(-1,-1),0.5,colors.black),
        ]
    )
    t3=Table(
        data=[
            [fechai],
            [p3],
            [p6],
        ],
        style=[
            ('BOX',(0,0),(-1,-1),0.5,colors.black),
        ]
    )
    t4=Table(
        data=[
            [fechai],
            [p4],
            [p5],
        ],
        style=[
            ('BOX',(0,0),(-1,-1),0.5,colors.black),
        ]
    )
    t5=Table(
        data=[
            [w1],
            [pguia],
            [w2],
            [fechad],
            [p6],
        ],
        style=[
            ('BOX',(0,0),(-1,-1),0.5,colors.black),
        ]
    )
    t6= Table(
        data=[
            [w4],
            [w5],
            [w67],
            [w8],
            [w9],
        ],
        style=[
            ('BOX',(0,0),(-1,-1),0.5,colors.black),
        ]
    )
    t7=Table(
        data=[
            [w10],
        ],
        style=[
            ('BOX',(0,0),(-1,-1),0.5,colors.black),
        ]
    )
    t8=Table(
        data=[
            [z],
            [z1],
            [z2],
            [z3],
        ],
        style=[
            ('BOX',(0,0),(-1,-1),0.5,colors.black),
        ]
    )
    t9=Table(
        data=[
            [[z4],[z5]],
            [z6],
        ],
        style=[
            ('BOX',(0,0),(-1,-1),0.5,colors.black),
        ]
    )
    t10=Table(
        data=[
            [z7],
        ],
        style=[
            ('BOX',(0,0),(-1,-1),0.5,colors.black),
        ]
    )
#//////////////////story////////////////////////////////////////////
#pagina1
    story.append(t)
    story.append(Spacer(0,20))
    story.append(t2)
    story.append(Spacer(0,20))
    story.append(t3)
    story.append(Spacer(0,20))
    story.append(t4)
    story.append(Spacer(0,20))
    story.append(PageBreak())
#pagina2
    story.append(w)
    story.append(Spacer(0,10))
    story.append(t5)
    story.append(Spacer(0,10))
    story.append(w3)
    story.append(Spacer(0,15))
    story.append(t6)
    story.append(t7)
    story.append(PageBreak())
#pagina3
    story.append(t8)
    story.append(Spacer(0,10))
    story.append(t9)
    story.append(Spacer(0,10))
    story.append(t10)


    doc=SimpleDocTemplate(buffer,pagesize=letter,showBoundary=0)
    doc.build(story)


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificado.pdf"'
    pdf = buffer.getvalue()
    response.write(pdf)
    buffer.close()
    return response