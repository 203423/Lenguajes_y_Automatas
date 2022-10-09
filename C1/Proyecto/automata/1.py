from encodings import utf_8
import csv
import openpyxl
import PyPDF2
from automata.fa.dfa import DFA





#crear un archivo de texto
pdfFileObject= open('out.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

parts =[]

print(f"No of Pages: {pdfReader.numPages}")
i=0

with open('1.txt','w') as file:
    for page in pdfReader.pages:
        pageObject = pdfReader.pages[i]
        text = pageObject.extractText()
        file.writelines(text+"\n"+"-"*50+"\n")
        i+=1
pdfFileObject.close()


# dfa=DFA(
#     states= {'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14'},
#     input_symbols={'12','1','2','3','4','5','6','7','8','9','0','11','31','32','91','24','15','471','582','000','593',' ','00'},
#     transitions={
#         'q0':{'12':'q1'},
#         'q1':{'4':'q2','5':'q2'},
#         'q2':{'0':'q3','1':'q3','2':'q3','3':'q3','4':'q3','5':'q3','6':'q3','7':'q3','8':'q3','9':'q3'},
#         'q3':{' ':'q4'},
#         'q4':{'11':'q5','31':'q5','32':'q5','91':'q5','24':'q5','15':'q5'},
#         'q5':{'471':'q6','582':'q6','000':'q6','593':'q6'},
#         'q6':{'0':'q7','1':'q7','2':'q7','3':'q7','4':'q7','5':'q7','6':'q7','7':'q7','8':'q7','9':'q7'},
#         'q7':{'0':'q8','1':'q8','2':'q8','3':'q8','4':'q8','5':'q8','6':'q8','7':'q8','8':'q8','9':'q8'},
#         'q8':{'0':'q9','1':'q9','2':'q9','3':'q9','4':'q9','5':'q9','6':'q9','7':'q9','8':'q9','9':'q9'},
#         'q9':{' ':'q10'},
#         'q10':{'00':'q11'},
#         'q11':{'1':'q12','2':'q12','3':'q12','4':'q12','5':'q12','6':'q12','7':'q12','8':'q12','9':'q12','0':'q12'},
#         'q12':{'1':'q13','2':'q13','3':'q13','4':'q13','5':'q13','6':'q13','7':'q13','8':'q13','9':'q13','0':'q13'},
#         'q13':{' ':'q14'},
#         'q14':{''}
#     },
#     initial_state='q0',
#     final_states={'q14'}
# )
# if(dfa.accepts_input('1241 11582520 0002')):
#     print("aceptado")
# else:
#     print("no aceptado")






# crear un archivo csv
input_file ='1.txt'
output_file = '1.csv'

wb= openpyxl.Workbook()
ws =wb.worksheets[0]
with open(input_file, 'r') as data:
    reader = csv.reader(data, delimiter=' ')
    for row in reader:
        ws.append(row)

wb.save(output_file)