from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit
from pathlib import Path
ROOT=Path(__file__).resolve().parent
p=ROOT/'poster.pdf';c=canvas.Canvas(str(p),pagesize=(1152,648))
ink=HexColor('#173D3B');teal=HexColor('#24736A');soft=HexColor('#E7F1EE');gray=HexColor('#3D4F4D')
def rect(x,y,w,h,color):c.setFillColor(color);c.rect(x,y,w,h,stroke=0,fill=1)
def txt(x,y,s,size=15,bold=False,color=gray):
 c.setFillColor(color);c.setFont('Helvetica-Bold' if bold else 'Helvetica',size);c.drawString(x,y,s)
def para(x,y,s,width,size=14,leading=19,color=gray):
 c.setFillColor(color);c.setFont('Helvetica',size)
 for line in simpleSplit(s,'Helvetica',size,width):c.drawString(x,y,line);y-=leading
 return y
rect(0,0,1152,648,HexColor('#FAFCFB'));rect(0,532,1152,116,soft)
txt(35,612,'Auditing Bias in AI Resume Screening',28,True,ink)
txt(35,580,'Does removing demographic information make LLM hiring decisions fairer?',19,False,ink)
txt(35,550,'Ahmad Bitar  |  Amanda Johnson  |  Sahel Rahman  |  Mahatheer Hamid',13)
txt(900,550,'ECE 4424 / CS 4824',12,True)
txt(35,501,'WHAT WE KNOW SO FAR',15,True,teal)
txt(35,465,'A matched-pair screening audit is implemented.',24,True,ink)
txt(35,435,'An actual LLM fairness conclusion is not yet supported.',16,True,teal)
txt(35,395,'THE EVIDENCE',15,True,teal)
rect(35,213,655,165,soft)
txt(56,348,'11',37,True,ink);txt(140,348,'matched pairs',17,True)
txt(56,314,'22',37,True,ink);txt(140,314,'synthetic resumes',17,True)
txt(56,280,'8',37,True,ink);txt(140,280,'held-out evaluation pairs',17,True)
txt(56,239,'OFFLINE SANITY TEST: 0 score gap; 48/48 skill-stress checks pass',13,True,ink)
txt(36,185,'Zero gap is expected because the offline heuristic ignores names.',13)
txt(36,165,'These results validate code behavior, not the fairness of an LLM.',13,True)
txt(745,501,'WHY IT MATTERS',15,True,teal)
para(745,471,'Recruiters use resume screening to decide who receives further human review. Job-related qualifications should matter more than demographic cues.',370,15,21)
txt(745,381,'HOW WE TESTED IT',15,True,teal)
para(745,355,'Baseline: identical screening prompt with named resume. Intervention: candidate name replaced by a neutral placeholder. Measures: paired score gaps, Yes/No differences, and qualification sensitivity.',370,14,20)
txt(745,227,'NEXT TEST + CLASS CONNECTION',15,True,teal)
para(745,201,'Run repeated actual LLM calls on held-out cases; compare indirect cues and weaker qualifications. Class theme: trust requires testing under changing conditions.',370,14,20)
rect(0,0,1152,112,soft)
txt(35,87,'WHERE THE CLAIM STOPS',15,True,teal)
para(35,64,'Small synthetic dataset, name as an imperfect proxy, no human ranking labels, and no completed LLM outcomes. Do not use to automate hiring.',1000,14,18)
txt(35,20,'Sources: EEOC (2024); Tripathi et al. (2026); Gerszberg et al. (2026). Code and report: see team project package.',11)
c.save();print(p)
