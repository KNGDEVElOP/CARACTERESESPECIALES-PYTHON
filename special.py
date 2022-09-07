import re
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from datetime import date

def specialCharacters(args):
    pattern = re.compile('[^A-Z0-9_.,Ñ/-]')
    res=pattern.search(args)==None
    return res


today=date.today();
Tk().withdraw
filename=askopenfilename(title="SELECCIONA ARCHIVO A ANALIZAR")
filenamesave=askdirectory(title="SELECCIONA LA RUTA DE GUARDADO")
print(filename)
print(filenamesave)
contador=0
path=filenamesave+"/"+str(today)+"_bitacora.txt"
text=open(path,'w')


with open(filename) as archivo:
    for linea in archivo:
        contador+=1
        res=specialCharacters(linea.strip())
        if (res==False):
            text.write(f'Caracter especial en linea: {contador} \n')
            print(f'Caracter especial en linea: {contador}')

text.close()

