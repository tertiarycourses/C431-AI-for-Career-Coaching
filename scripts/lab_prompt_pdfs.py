from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT
from xml.sax.saxutils import escape
styles=getSampleStyleSheet();styles['BodyText'].fontSize=10;styles['BodyText'].leading=15
for folder in sorted(Path('labs').glob('lab-*')):
 for name,filename in [('prompts.md','PROMPTS.pdf'),('README.md','LAB-GUIDE.pdf')]:
  story=[]
  for para in (folder/name).read_text().split('\n\n'):
   para=para.replace('```text','').replace('```','').strip()
   if not para:continue
   heading=para.startswith('#');para=para.lstrip('# ').strip()
   story += [Paragraph(escape(para).replace('\n','<br/>'),styles['Heading2'] if heading else styles['BodyText']),Spacer(1,8)]
  SimpleDocTemplate(str(folder/filename),rightMargin=42,leftMargin=42,topMargin=42,bottomMargin=42).build(story)
print('Created 8 prompt PDFs and 8 standalone lab guide PDFs.')
