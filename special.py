import re
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from datetime import date
from io import open

def specialCharacters(args):
    pattern = re.compile('[^A-Z0-9_.,Ñ/ ;-]')
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
text=open(path,mode='w')


with open(filename) as archivo:
    for linea in archivo:
        contador+=1
        res=specialCharacters(linea.strip())
        if (res==False):
            print(f'Caracter especial en linea: {contador}')
            text.write(f'Caracter especial en linea: {contador} \n')
            sep=linea.split(";")
            for campo in sep:
                f=specialCharacters(campo.strip())
                if (f==False):
                    z=campo.split()

                    text.write(f'{campo} \n')
                    for i in z:
                        r=specialCharacters(i)
                        if(r==False):
                            text.write(f'error-->{i}<-- \n')
                            print(f'error-->{i}<--')

text.close()

