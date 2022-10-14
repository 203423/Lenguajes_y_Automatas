from cProfile import label
from tkinter import filedialog
from tkinter import Tk,Frame, END, Label, CENTER, Button, Text
import os
import tabula
import test
def show_frame(frame):
    frame.tkraise()

window = Tk()
window.minsize(width=1200, height=720)
window.title("Verificador de items de inventario")
# window.iconbitmap('./icon.ico')

window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

w_entrada = Frame(window) #Pantalla de inicio
w_salida = Frame(window) #Pantalla para mostrar el .txt

for frame in (w_entrada, w_salida):
    frame.config(bg="#B60D0D")
    frame.grid(row=0, column=0, sticky="nsew")

def convertions(archivo):
    #Convert PDF into txt file, format csv
    tabula.convert_into(archivo, "./C1/Proyecto/automata/1.txt",output_format="csv", pages='all',area=[140,12.75,790.5,950])
    lineas_validadas.insert(END,"PDF convertido a txt")
    #Create headers
    with open('./C1/Proyecto/automata/2.csv', 'w',encoding="latin1") as ftemp:
        ftemp.write('CONTABILIDAD,AÑO DE COMPRA,CODIGO,CÓDIGO SISMOB WEB,DESCRIPCION DEL BIEN,VALOR EN LIBROS,PORCENTAJE DE DEPRECIACIÓN, AÑOS TRANSCURRIDOS, PRECIO DEPRECIADO, TOTAL CONTABLE')

def eliminacionDeTemps():
    if os.path.exists("./C1/Proyecto/automata/1.txt"):
        print("caché eliminada")
        os.remove("./C1/Proyecto/automata/1.txt")
    else:
        pass

def comprobacion():
    i=0
    j=0
    k=0
    
    #Read txt file and convert to csv
    with open('./C1/Proyecto/automata/1.txt') as f:
        # my_imput_str=""
        data_txt=[line for line in f.readlines()]
        for line in data_txt:
            cadena_aceptada =(str(k)+" Cadenas aceptadas")
            cadena_rechazada =(str(j)+" Cadenas rechazadas")
            data_str=(data_txt[i])
            my_input_str=data_str.strip("\n")
            print(i+1) 
            i=i+1   
            if test.dfa.accepts_input(my_input_str):
                print("Cadena aceptada")   
                k=k+1 
               # pass
            else:
                print('rejected')
                j=j+1     
            cadena_aceptada =(str(k)+" Cadenas aceptadas")
            cadena_rechazada =(str(j)+" Cadenas rechazadas")
            #Create temporal file
            with open('./C1/Proyecto/automata/2.csv','a',encoding="latin1") as f:
                f.write("\n")
                f.write(my_input_str)
        lineas_validadas.insert(END,"\n"+cadena_rechazada+"\n")        
        lineas_validadas.insert(END,cadena_aceptada+"\n")   
        lineas_validadas.insert(END,"Archivo validado" +"\n"+ "Archivo guardado en ./C1/Proyecto/automata/1.csv")
eliminacionDeTemps()

show_frame(w_entrada)
ruta_str = "Ruta: "

def abrir_archivo():
    archivo = filedialog.askopenfilename(title="Abrir", initialdir="./C1/Proyecto/automata/", filetypes=(("Archivos .pdf", "*.pdf"), ("Todos los archivos", "*.*")))
    file_dir["text"] = ruta_str+ archivo
    convertions(archivo)
    comprobacion()
    eliminacionDeTemps()
    



font_text = "Helvetica 12 bold"

label_title = Label(w_entrada,text="Verificador de inventario",justify=CENTER,font="Helvetica 24 bold").pack()
label_title = Label(w_salida,text="Verificador de inventario",justify=CENTER,font="Helvetica 24 bold").pack()
#Entrada
file_dir = Label(w_entrada,text="Ruta: ",font="Helvetica 12",bg="#91afc6",foreground="black")
file_dir.pack()

abrir_btn = Button(w_entrada,text="Abrir",command=abrir_archivo,borderwidth=0,width=10,font=font_text)
abrir_btn.pack()

lineas_validadas = Text(w_entrada)
lineas_validadas.pack(padx=30,pady=20)


guardar_btn = Button(w_entrada,text="Guardar",borderwidth=0,width=10,font=font_text)

#salida
consol_eon_screen=Label(w_salida,text="Consola EON",font="Helvetica 12 bold",bg="#91afc6",foreground="black")



window.mainloop()