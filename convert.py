import pandas as pd 
from csv import reader
from os import listdir



def s(a,i,f): return a[i-1:f].strip()
def f(a,i,f): return float(a[i-1:f])/100
def i(a,i,f): return int(a[i-1:f])

dfs=[]
for arquivo in listdir('./input'):   
    regs=[]
    with open('./input/'+arquivo,'r',  encoding='ISO-8859-1') as file:
        for linha in file.readlines():
    
            TIPREG=i(linha,1,2)
            if TIPREG==0 or TIPREG==99: continue;
            
            reg={
            'DATE':i(linha,3,10),
            'CODBDI':i(linha,11,12),
            'CODNEG':s(linha,13,24),
            'TPMERC':s(linha,25,27),
            'NOMRES':s(linha,28,39),
            'ESPECI':s(linha,40,49).strip(),
            'PRAZOT':s(linha,50,52),
            'MODREF':s(linha,53,56),
            'PREABE':f(linha,57,69),
            'PREMAX':f(linha,70,82),
            'PREMIN':f(linha,83,95),
            'PREMED':f(linha,96,108),
            'PREULT':f(linha,109,121),
            'PREOFC':f(linha,122,134),
            'PREOFV':f(linha,135,147),
            'TOTNEG':i(linha,148,152),
            'QUATOT':i(linha,153,170),
            'VOLTOT':f(linha,171,188),
            'PREEXE':f(linha,189,201),
            'INDOPC':i(linha,202,202),
            'DATVEN':i(linha,203,210),
            'FATCOT':i(linha,211,217),
            'PTOEXE':f(linha,218,230),
            'CODISI':s(linha,231,242),
            'DISMES':i(linha,243,245)
            }
            
            regs+=[reg]
            
    dfs+=[pd.DataFrame(regs)]
    
df=pd.concat(dfs)

df.sort_values(by=['DATE', 'CODNEG'])

df.to_csv('BOVESPA.csv',index=False)
