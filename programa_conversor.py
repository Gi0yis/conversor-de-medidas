import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.54

# Leer el archivo
df = pd.read_csv("muebles_medidas.csv")

# Añador una columna al DataFrame para las pulgadas y se rellene con el calculo de la función cm_a_pulgadas

df["pulgadas"] = df["centimetros"].apply(cm_a_pulgadas)

df.to_csv("muebles_medidas_2.csv", index=False)

print("Archivo guardado correctamente")