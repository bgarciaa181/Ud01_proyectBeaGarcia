"""
Programa conversor de Euros a Dólares estadounidenses (USD). 
Autor: Tu Nombre
Fecha: 2026-10-19
Versión: 1.0
"""

RATE_EUR_USD = 1.08
euros = float(input("EUR: "))
usd = euros * RATE_EUR_USD
print(f"{euros:.2f} EUR = {usd:.2f} USD")
celsius = float(input("º C: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius:.2f} C = {fahrenheit:.2f} F")