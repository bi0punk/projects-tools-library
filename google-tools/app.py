

from googlesearch import search
import googlesearch
import pandas as pd
print("ingrese a buscar\n")

consulta = input()

busqueda = []

for i in search(consulta, start=0 , stop=10):
    busqueda.append(i)  

    with open('busquedas.txt', 'w') as temp_file:
        for item in busqueda:
            temp_file.write("%s\n" % item)


file = open('busquedas.txt', 'r')
df = pd.DataFrame([busqueda])

print(df)
print(file.read())
    
