import base64, os, shutil
b=lambda p: base64.b64encode(open(p,'rb').read()).decode()
F='node_modules/@fontsource/'
NAME='Austin'
MENU=open('menu_snip.html').read()
s=open('src.html').read()
s=s.replace('%%BEBAS%%',b(F+'bebas-neue/files/bebas-neue-latin-400-normal.woff2'))
for w in ('400','500','700'): s=s.replace('%%M'+w+'%%',b(F+f'montserrat/files/montserrat-latin-{w}-normal.woff2'))
s=s.replace('%%PHOTO%%','data:image/webp;base64,'+b('assets/photo.webp'));s=s.replace('%%AVATAR%%','data:image/webp;base64,'+b('assets/avatar.webp'))
s=s.replace('%%LETTERS%%',''.join(f'<span class="enter" style="transition-delay:{.1+i*.06:.2f}s">{c}</span>' for i,c in enumerate(NAME.upper())))

s=s.replace('%%AGENCY_URL%%','#')
s=s.replace('%%MENU%%',MENU).replace('%%NAMEU%%',NAME.upper()).replace('%%NAME%%',NAME)
os.makedirs('dist/vendor',exist_ok=True); open('dist/index.html','w').write(s)
os.path.exists('vendor/three.module.js') and shutil.copy('vendor/three.module.js','dist/vendor/three.module.js'); print(len(s)//1024,'KB')

import json
WORKS=[["Eid Mubarak","D Gadgets",["social"]],["Monday Deals","D Gadgets",["flyer","social"]],["April, Fully Loaded","D Gadgets",["flyer","social"]],["Healthy Living @UNIZIK","UNIZIK Student Union",["party"]],["Karaoke Night","Luxe Skyside Hotel",["party"]],["City Rave — Jungle Invasion","City Rave",["party"]],["DJ BOIZ — Road2December Tour","DJ BOIZ",["party"]],["The Playmakers","The Playmakers",["party"]],["Face Off — Hotwater 1.0","Face Off",["party"]],["Dera The Plug","Dera The Plug",["flyer","social"]],["October / Independence Day","DEL Tech & Gadgets",["flyer","social"]],["Jeans for Kings & Queens","MJ Luxe Denim",["flyer"]],["Place Your Order","The Food Lab",["flyer"]],["MJ Luxe Denim","MJ Luxe Denim",["logo"]],["Dera The Plug","Dera The Plug",["logo"]],["The Bold Lens Podcast","The Bold Lens Podcast",["social"]]]
w=open('work_src.html').read()
w=w.replace('%%BEBAS%%',b(F+'bebas-neue/files/bebas-neue-latin-400-normal.woff2'))
for wt in ('500','700'): w=w.replace('%%M'+wt+'%%',b(F+f'montserrat/files/montserrat-latin-{wt}-normal.woff2'))
VIDEOS=[]
w=w.replace('%%MENU%%',MENU);w=w.replace('%%VIDEOS%%',json.dumps(VIDEOS)).replace('%%WORKS%%',json.dumps(WORKS)).replace('%%NAMEU%%',NAME.upper()).replace('%%NAME%%',NAME)
open('dist/work.html','w').write(w); print('work.html',len(w)//1024,'KB')
c=open('contact_src.html').read()
c=c.replace('%%BEBAS%%',b(F+'bebas-neue/files/bebas-neue-latin-400-normal.woff2'))
for wt in ('500','700'): c=c.replace('%%M'+wt+'%%',b(F+f'montserrat/files/montserrat-latin-{wt}-normal.woff2'))
c=c.replace('%%MENU%%',MENU).replace('%%NAMEU%%',NAME.upper()).replace('%%NAME%%',NAME)
open('dist/contact.html','w').write(c); print('contact.html',len(c)//1024,'KB')
v=open('cv_src.html').read()
v=v.replace('%%BEBAS%%',b(F+'bebas-neue/files/bebas-neue-latin-400-normal.woff2'))
for wt in ('500','700'): v=v.replace('%%M'+wt+'%%',b(F+f'montserrat/files/montserrat-latin-{wt}-normal.woff2'))
v=v.replace('%%MENU%%',MENU).replace('%%NAMEU%%',NAME.upper()).replace('%%NAME%%',NAME)
open('dist/cv.html','w').write(v); print('cv.html',len(v)//1024,'KB')
