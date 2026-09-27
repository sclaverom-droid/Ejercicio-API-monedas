import requests

# URL de la API proporcionada en el ejercicio
url = "https://api.exchangerate-api.com/v4/latest/EUR"

# Petición a la API y obtención de los datos en formato JSON
respuesta = requests.get(url)
datos = respuesta.json()

# Extraemos el diccionario de tipos de cambio
rates = datos["rates"]

# Inicializamos variables para calcular la moneda más económica
moneda_mas_economica = None
valor_minimo = float("inf")

# Recorremos el diccionario de tasas de cambio
for moneda, valor in rates.items():
    if valor < valor_minimo:
        valor_minimo = valor
        moneda_mas_economica = moneda

print(f"La moneda más económica respecto al EUR es: {moneda_mas_economica} con un valor de {valor_minimo}")
