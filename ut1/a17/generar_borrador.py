#!/usr/bin/env python3
"""Genera el PDF de trabajo (requiere reportlab). No sustituye las evidencias."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, Preformatted
from reportlab.platypus.tableofcontents import TableOfContents

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / 'MEMORIA_BORRADOR.pdf'
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Texto', fontName='Helvetica', fontSize=12, leading=18, spaceAfter=8))
styles.add(ParagraphStyle(name='Titulo', fontName='Helvetica-Bold', fontSize=22, leading=29, textColor=colors.HexColor('#17334A'), spaceAfter=18))
styles.add(ParagraphStyle(name='Seccion', fontName='Helvetica-Bold', fontSize=15, leading=21, textColor=colors.HexColor('#17334A'), spaceBefore=16, spaceAfter=12, keepWithNext=True))
styles.add(ParagraphStyle(name='Subseccion', fontName='Helvetica-Bold', fontSize=12, leading=18, spaceBefore=10, spaceAfter=8, keepWithNext=True))
styles.add(ParagraphStyle(name='CodigoPPS', fontName='Courier', fontSize=12, leading=18, backColor=colors.HexColor('#F2F4F6'), leftIndent=7, rightIndent=7, spaceBefore=6, spaceAfter=10))
styles.add(ParagraphStyle(name='IndicePPS', fontName='Helvetica', fontSize=12, leading=18, spaceAfter=10))

def inline(s):
    s=escape(s)
    s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'<a href="\2" color="#195A80">\1</a>',s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`([^`]+)`',r'<font name="Courier">\1</font>',s)
    return s

class Memoria(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name == 'Seccion':
            key = 'sec-' + str(self.seq.nextf('seccion'))
            self.canv.bookmarkPage(key)
            self.notify('TOCEntry', (0, flowable.getPlainText(), self.page, key))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#CCD5DC'))
    canvas.line(3*cm, 2*cm, A4[0]-3*cm, 2*cm)
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.HexColor('#53616D'))
    canvas.drawString(3*cm, 1.5*cm, 'UT1 · Actividad 4 | BORRADOR · faltan evidencias')
    canvas.drawRightString(A4[0]-3*cm, 1.5*cm, str(doc.page))
    canvas.restoreState()

doc=Memoria(str(OUTPUT), pagesize=A4, leftMargin=3*cm, rightMargin=3*cm,
    topMargin=2.5*cm, bottomMargin=2.5*cm, title='ACT_UT1_4 - Borrador de memoria', author='Albert Grigore')
frame=Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
doc.addPageTemplates(PageTemplate(id='normal',frames=frame,onPage=footer))
story=[Spacer(1,2*cm),Paragraph('PUESTA EN PRODUCCIÓN SEGURA',styles['Subseccion']),
       Paragraph('Solidity + Git',styles['Titulo']),Paragraph('ACT_UT1_4 · Unidad 1',styles['Subseccion']),
       Spacer(1,cm),Paragraph('Albert Grigore',styles['Texto']),Paragraph('NIA: pendiente',styles['Texto']),
       Paragraph('15 de noviembre de 2026',styles['Texto']),Spacer(1,cm),
       Paragraph('<b>BORRADOR DE TRABAJO</b>',styles['Texto']),
       Paragraph('Faltan las capturas de las seis lecciones y los 25 niveles, los artículos del aula y la comprobación de la plantilla. Este documento no acredita los cursos completados y no está listo para entregar.',styles['Texto']),PageBreak(),
       Paragraph('Índice',styles['Titulo'])]
toc=TableOfContents();toc.levelStyles=[styles['IndicePPS']];story += [toc,PageBreak()]
source=(BASE/'MEMORIA_BORRADOR.md').read_text().split('## Introducción',1)[1]
lines=('## Introducción'+source).splitlines();paragraph=[];in_code=False;code=[];table=[]
def flush():
    if paragraph:
        story.append(Paragraph(inline(' '.join(paragraph)),styles['Texto']));paragraph.clear()
def flush_table():
    if not table:return
    headers=table[0]
    for row in table[1:]:
        if all(re.fullmatch(r'[:\- ]+',c or '-') for c in row):continue
        text='; '.join(f'<b>{inline(headers[i])}:</b> {inline(cell)}' for i,cell in enumerate(row) if i<len(headers))
        story.append(Paragraph(text,styles['Texto']))
    table.clear()
for line in lines:
    if line.startswith('```'):
        flush();flush_table()
        if in_code:
            story.append(Preformatted('\n'.join(code),styles['CodigoPPS'],maxLineLength=52));code=[]
        in_code=not in_code;continue
    if in_code:code.append(line);continue
    if line.startswith('|'):
        flush();table.append([c.strip() for c in line.strip('|').split('|')]);continue
    flush_table()
    if line.startswith('## '):
        flush()
        if story and line != '## Introducción':story.append(PageBreak())
        story.append(Paragraph(inline(line[3:]),styles['Seccion']))
    elif line.startswith('### '):
        flush();story.append(Paragraph(inline(line[4:]),styles['Subseccion']))
    elif not line.strip():flush()
    elif line.startswith('- '):
        flush();story.append(Paragraph('• '+inline(line[2:]),styles['Texto']))
    else:paragraph.append(line.strip())
flush();flush_table();doc.multiBuild(story)
print(OUTPUT)
