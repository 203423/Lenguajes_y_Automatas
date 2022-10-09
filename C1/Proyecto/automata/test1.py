import pandas as pd

with open('2.txt', 'w',encoding="utf-8") as ftemp:
    ftemp.write('CONTABILIDAD,AÑO DE COMPRA,CODIGO,CÓDIGO SISMOB WEB,DESCRIPCION DEL BIEN,VALOR EN LIBROS,PORCENTAJE DE DEPRECIACIÓN, AÑOS TRANSCURRIDOS, PRECIO DEPRECIADO, TOTAL CONTABLE')

with open('1.txt') as f:
    # my_imput_str=""
    i=0
    data_txt=[line for line in f.readlines()]
    for line in data_txt:
        data_str=(data_txt[i])
        my_input_str=data_str.strip("\n")
        print(i+1) 
        i=i+1   
        with open('2.txt','a',encoding="utf-8") as f:
            f.write("\n")
            f.write(my_input_str)
read_file = pd.read_csv ('2.txt')
read_file.to_csv ('1.csv', index=None, header=['CONTABILIDAD','AÑO DE COMPRA','CODIGO','CÓDIGO SISMOB WEB','DESCRIPCION DEL BIEN','VALOR EN LIBROS','PORCENTAJE DE DEPRECIACIÓN', 'AÑOS TRANSCURRIDOS', 'PRECIO DEPRECIADO', 'TOTAL CONTABLE'],encoding='latin1',mode='w')