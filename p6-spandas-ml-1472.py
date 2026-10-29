import pandas as pd
import numpy as np

serie_amigos=["jose","azul","brianna","scarlet","karla","alejandra","nicole"]
print("------serie lista de amigos NC 1472------")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print("--- serie listado valor de billetes MX NC 1472 ---")
amigos=pd.Series(serie_billetes)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
serie_bletras=["veinte","cincuenta","cien","doscientos","quinientos","mil"]
print("--- serie listado nombre y valor de billetes MX NC 1472 ---")
tablabilletes=pd.Series(serie_billetes, serie_bletras)
print(tablabilletes)

# diccionario dataframe
# diccionario de valor monedas y nombre
print("datos dediccionarioa dataframe en pandas")
dic_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras":["veinte","cincuenta","cien","doscientos","quinientos","mil"]
} 

tablabilletes=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)

print("casa de cambio de jose solis nc 1472")