import pandas as pd

# Dataframe --> Es la información básica con el nombre de las piezas y centimetros para poder armar el CSV

data = {
    "pieza": ["Pata", "Tablero", "Puerta", "Estante", "Panel Laterar"],
    "centimetros": [40, 120, 60, 30,  180]
}

df = pd.DataFrame(data)

# Guardar el DataFrame enun archivo CSV
df.to_csv("muebles_medidas.csv", index=False)