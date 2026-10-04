from pathlib import Path
import re,zipfile
patterns=[r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY',r'\b(?:sk-[A-Za-z0-9]{20,}|gh[pousr]_[A-Za-z0-9]{20,})',r'(?i)(?:api[_-]?key|password|secret|token)\s*[:=]\s*[\"\x27][A-Za-z0-9/+_-]{12,}']
hits=[];count=0
for f in Path('.').rglob('*'):
 if not f.is_file() or any(x in f.parts for x in ['.git','reference','assessment','__pycache__','archive']):continue
 if f.suffix in ['.pptx','.docx']:
  with zipfile.ZipFile(f)as z:text='\n'.join(z.read(x).decode(errors='ignore')for x in z.namelist()if x.endswith('.xml'))
 else:
  if f.suffix not in ['.md','.py','.sh','.csv','.txt']:continue
  text=f.read_text(errors='ignore')
 count+=1
 for pat in patterns:
  if re.search(pat,text):hits.append(str(f))
print(f'Security scan: {count} files; {len(hits)} hits.');print('\n'.join(hits));raise SystemExit(bool(hits))
