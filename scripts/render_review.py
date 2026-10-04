from pathlib import Path
import fitz
from PIL import Image, ImageOps, ImageDraw
p=next(Path('courseware').glob('*v1.0.pdf'));d=fitz.open(p)
for block in range(0,len(d),20):
 sheet=Image.new('RGB',(1500,1100),'#cccccc');draw=ImageDraw.Draw(sheet)
 for k,i in enumerate(range(block,min(block+20,len(d)))):
  pix=d[i].get_pixmap(matrix=fitz.Matrix(.38,.38));im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((365,200));x=(k%4)*375;y=(k//4)*220;sheet.paste(im,(x,y+20));draw.text((x+5,y+3),str(i+1),fill='black')
 sheet.save(f'/tmp/c431-review/slides-{block+1}.png')
for pattern in ['LG-*.pdf','LP-*.pdf']:
 p=next(Path('courseware').glob(pattern));d=fitz.open(p);sheet=Image.new('RGB',(1200,1500),'#ccc')
 for k,i in enumerate([0,1,2,3,min(5,len(d)-1),len(d)-1]):
  pix=d[i].get_pixmap(matrix=fitz.Matrix(.55,.55));im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((395,745));sheet.paste(im,((k%3)*400,(k//3)*750))
 sheet.save('/tmp/c431-review/'+p.name[:2]+'.png')
